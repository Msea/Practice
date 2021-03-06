from random import randint

def print_board(board):
    for row in board:
        print " ".join(row)
def stealth_print(board):
    for row in board:
        for thing in row:
            if not(ord(thing)>=97)or not(ord(thing)<116):
                print thing,
            else:
                print "O",
        print ""

def hide(ship, board, leng, i):#human hides ship
    v = False #tests whether input is on board
    valid = 0 #tests whether input is repetitive
    print "Next you must hide your " + ship
    while valid<1:#Keep running until nonrepetitive input
        valid=0
        v=False
        while v==False:#keep running until valid orientation
            ornt = raw_input("Do you wish your " + ship + " to be hidden vertically (enter v) or horizontally (enter h) ")
            if ((ornt == "v") or (ornt =="h")):
                v=True
            else:
                print "Invalid Position"
        v=False
        while v==False:#keep running until valid col
            col=(raw_input("In what column (0-"+str(boardsize-1)+") do you wish to begin hiding your " + ship + "? " ))
            try:
               col = int(col)
               temp = True
            except ValueError:
               temp = False
               print "Your underlings do not understand your secret code."
            if temp:#if int then check if on board
                if (ornt == "v"):
                   if ((col>=0) and (col<boardsize)):
                        v=True
                   else:
                        print "That's beyond our waters. You must never hide ships there, Simba."
                else:
                   if ((col>=0) and (col+leng<=boardsize)):
                       v=True
                   else:
                       print "Are you trying to get your men killed! You can't hide your ship beyond the bounds of your ocean."
        v=False
        while v==False:#valid row?
            row=(raw_input("In what row (0-"+str(boardsize-1)+") do you wish to begin hiding your " + ship + "? " ))
            try:
               row = int(row)
               temp = True
            except ValueError:
               temp = False
               print "Yes of course, but what row?"
            if temp:
                if ornt == "h":
                    if ((row>=0) and (row<boardsize)):
                        v=True
                    else:
                        print "Invalid hiding place"
                else:
                    if ((row>=0) and (row+leng<=boardsize)):
                        v=True
                    else:
                        print "There is no water there. Ship cannot stay hidden well if it is on dry land."
        if ornt == "v":#Now heck that doesn't overlap other ship for each orient
            for j in range(row, row+leng):
                if (not (board[j][col] == 'O')):
                    valid = -1
        if ornt == "h":
            for j in range(col, col+leng):
                if (not (board[row][j]=='O')):
                    valid = -1
        if (valid == 0):#Nowput ship there
            if ornt == "v":
                for j in range(row, row+leng):
                    board[j][col] = i
            else:
                for j in range(col, col+leng):
                    board[row][j] = i
                    
            valid = 2
        else:
            print "You have already hidden something there. Hide elsewhere"
   
    print "Your "+ship+ " has been hidden."
    print_board(board)
    return board

def hidden(ship, board, leng, i):#Computer hides ship
    valid = False
    valids=0
    ornt="n"#random initiation. will be used for orientation
    startingrow=20#random initiation. will be used for row in which ship starts
    startingcol=20#random initiation. will be used for col in which ship starts
    while (valid ==False or valids<=0):
        valids = 0
        valid = False
        location = [randint(0, boardsize-1), randint(0, boardsize-1), randint(0, 1)]
        startingrow = location[0]
        startingcol=location[1]
        if location[2] == 1:
            ornt = "v"
            if (startingrow+leng<=boardsize):#check fits
                valid =True
        else:
            ornt = "h"
            if (startingcol+leng<=boardsize):#check fits
                valid =True
        if valid ==True:#Once fits, determine that doesn't overlap
            if ornt == "h":
                for j in range(startingcol, startingcol+leng):
                    if(not(board[startingrow][j] == 'O')):
                        valids =-1
            else:
                for j in range(startingrow, startingrow+leng):
                    if(not(board[j][startingcol]=='O')):
                        valids =-1
            if valids == 0:
                valids = 1
    if ornt == "v":#Hide ship
        for j in range(startingrow, startingrow+leng):
            board[j][startingcol] = i
    else:
        for j in range(startingcol, startingcol+leng):
            board[startingrow][j]=i
    apple = raw_input("Press Enter for Computer to hide "+ship)
    print "An intelligence report has come in that computer has hidden "+ship+" Why did you press Enter??"
    return board

def win(board):
    winned = True
    for row in board:
        for point in row:
            if (97<=ord(point)<116):#no more lowercase a-s on board. All turned to upper.
                winned=False
    return winned

def sunk(board, i):
    sunked = True
    for row in board:
        for point in row:
            if (point == i):
                sunked = False
    return sunked

def nameize(letter):
   ships={"a":"Aircraft Carrier", "b": "Battleship", "c":"Cruiser", "d": "Destroyer", "s": "Submarine"}
   return ships[letter]

def guess(board, guess):#What happens once a valid guess has been made
    new = False#Checks that guess is not a repeat
    if (97<=ord(board[guess[0]][guess[1]])<116):#What was there is a-s letter
        new = True#not repeat
        print nameize(board[guess[0]][guess[1]])+" has been hit!"#ship has been hit
        board[guess[0]][guess[1]]=board[guess[0]][guess[1]].upper()#Switches to upper. Will now print in stealth
        if sunk(board, board[guess[0]][guess[1]].lower()):
          print nameize(board[guess[0]][guess[1]].lower())+" has been sunk"
    elif (board[guess[0]][guess[1]] == 'O'):#What was there was blank
        new = True#not repeat
        board[guess[0]][guess[1]] = 'X'#Becomes X.
        print "Splash!!"
    return(board, new)


def humanguess(board):#Procedure for human guessing
    validguess = False#Remembers if repeat
    validsguess = False#Remembers if valid guess
    while (validsguess ==False):
        validguess = False
        print "Here is what the enemy ocean looks like thus far:"
        stealth_print(board)
        launch = []
        temp = raw_input("To which row coordinate (0-"+str(boardsize-1)+") do you wish to launch this missile? ")
        try:
           temp = int(temp)
           temp2 = True
        except ValueError:
           temp2 = False
           print "Low level missiles cannot reach that hyperplane."
        if temp2:#Once col is int, try row
           launch.append(temp)
           temp = raw_input("To which column coordinate (0-"+str(boardsize-1)+") do you wish to launch this missile? ")
           try:
               temp = int(temp)
               temp2 = True
           except ValueError:
               temp2 = False
               print "You hit the treasury for your missile supplier and caused confusion. You get a free additional launch."
           if temp2:#Once have col and row, make sure is on board
               launch.append(temp)
               if (launch[0]<0 or launch[0]>=boardsize or launch[1]<0 or launch[1]>=boardsize):
              
                    print "That is beyond the scope of our missiles. Command a launch to somewhere else."
                    apple = raw_input("Press Enter to continue...")
               else:
                    validguess = True
        if validguess ==True:#Once know on board, check that it is a new guess
            validsguess = (guess(board, launch))[1]#the new variable
            if validsguess == False:
                print "You have already directed a missile launch to those coordinates. Your supervisor won't let you direct a launch there again." 
                print "You must choose different coordinates."
            apple = raw_input("Press Enter to continue...")
    board = (guess(board, launch))[0]
    stealth_print(board)
    return(board)

def compguess(board): #what happens when computer guesses
    print "An enemy missile is heading for your ocean!!"
    apple = raw_input("Press Enter to see what your ocean looks like thus far...")
    print_board(board)
    apple = raw_input("Press Enter to continue...")
    validsguess = False
    while (validsguess ==False):#While not not repeat
        launch = [randint(0,boardsize-1), randint(0,boardsize-1)]
        validsguess = (guess(board, launch))[1]#The new checker
    board = (guess(board, launch))[0]
    print "Enemy missile made contact at coordinate ("+str(launch[0])+", "+str(launch[1])+")"
    print_board(board)
    apple = raw_input("Press Enter to continue...")
    return board

print "Hello Human"

if (raw_input("Type 'a' to play an abridged game. Type any other key to play a regular game. ") == 'a'):
   abridge = True
   boardsize = 4
   num = "one"
else:
   abridge = False
   boardsize=10
   num="five"


board1 = []
board2 = []
#make board
for x in range(boardsize):
   board1.append(["O"] * boardsize)
for x in range(boardsize):
   board2.append(["O"]*boardsize)

print "Congratulations. You have just been promoted to naval Commander."
print "With war imminent, we are taking all the precautions we must."
print "We have counted our supplies, trained the troops, and secured "+num+" whole ships."
#Hide ships
board1 = hide("battleship", board1, 4, "b")
if not abridge:
   board1 = hide("aircraft carrier", board1, 5, "a")
   board1 = hide("submarine", board1, 3, "s")
   board1 = hide("cruiser", board1, 3, "c")
   board1 = hide("destroyer", board1, 2, "d")

if not abridge:
   board2 = hidden("aircraft carrier", board2, 5, "a")
board2 = hidden("battleship", board2, 4, "b")
if not abridge:
   board2 = hidden("submarine", board2, 3, "s")
   board2 = hidden("cruiser", board2, 3, "c")
   board2 = hidden("destroyer", board2, 2, "d")

#Get ready to play
print "The sun sets in the east over a cold sky while a green breeze hovers below the treetops. The winds are changing...war will soon be upon us."
print "You are entrusted with the anti-ship missiles, the P-800 Oniks."
print "Your mission - to command the launch team to send them to the sectors where you believe there are enemy ships. Don't ask questions - we are totally a legit organization."
print "Anyway, based on your intel they have the same ships that you do. You must sink theirs before they sink yours."
print "You are entrusted with this task."
print ""
apple = raw_input("Press Enter to continue...")

while ((win(board1) ==False) and (win(board2)==False)):
    board2 = humanguess(board2)
    if (win(board2)):
      break
    board1 = compguess(board1)
#Win conditions
if (win(board2)):
   print ""
   print "The adrenaline of victory surges through your veins. You are the Master Commandant."
   print "Soon you will be commander of everyone because of your superior skills."
   print "There is a rumor going around that counter-intelligence hacked their launcher to make it shoot at random."
   print "You don't believe in rumors..."
   print ""
   print "Counter-intelligence is all brain and no brawn. What do they know?"
   print "They are just scared of how awesome you are."
elif (win(board1)):
   print ""
   print "You detect another enemy missile being launched, but it does not appear to be headed to your ocean."
   print "You assume this means they have given up."
   print "The shadow above your head grows as the missile starts falling down."
   print ""
   print "Darkness..."
else:
   print "Well this is awkward"
