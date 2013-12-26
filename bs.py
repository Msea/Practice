from random import randint
#boardsize=9

def print_board(board):
    for row in board:
        print " ".join(row)
def stealth_print(board):
    for row in board:
        for thing in row:
            if (not(thing =="a") and (not(thing =="b")) and (not(thing =="c")) and (not(thing =="d")) and (not(thing =="s"))):
                print thing,
            else:
                print "O",
        print ""

def hide(ship, board, leng, i):
    v = False
    valid = 0
    print "Next you must hide your " + ship
    while valid<1:
        valid=0
        v=False
        while v==False:
            ornt = raw_input("Do you wish your " + ship + " to be hidden vertically (enter v) or horizontally (enter h) ")
            #location = [col, row, ornt]
            if ((ornt == "v") or (ornt =="h")):
                v=True
            else:
                print "Invalid Position"
        v=False
        while v==False:
            #col = int(raw_input("In what column (0-"+str(boardsize-1)+") do you wish to begin hiding your " + ship + "? " ))
            col=(raw_input("In what column (0-"+str(boardsize-1)+") do you wish to begin hiding your " + ship + "? " ))
            try:
               col = int(col)
               temp = True
            except ValueError:
               temp = False
               print "Your underlings do not understand your secret code."
            if temp:
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
        while v==False:
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
        #print valid    
        if ornt == "v":
            for j in range(row, row+leng):
                if (not (board[j][col] == 'O')):
                    #board[j][col] = i
                    valid = -1
        if ornt == "h":
            for j in range(col, col+leng):
                if (not (board[row][j]=='O')):
                    #board[row][j] = i
                    #print "this this"
                    #print valid
                    valid = -1
        if (valid == 0):
            if ornt == "v":
                for j in range(row, row+leng):
                    #if (board[j][col] == 'O'):
                    board[j][col] = i
            else:
                for j in range(col, col+leng):
                    #if (board[row][j]=='O'):
                    board[row][j] = i
                    
            valid = 2
        else:
            #valid=0
            print "You have already hidden something there. Hide elsewhere"
   
    print "Your "+ship+ " has been hidden."
    print_board(board)
    return board

def hidden(ship, board, leng, i):
    valid = False
    valids=0
    ornt="n"
    startingrow=20
    startingcol=20
    while (valid ==False or valids<=0):
        valids = 0
        valid = False
        location = [randint(0, boardsize-1), randint(0, boardsize-1), randint(0, 1)]
        #print location
        startingrow = location[0]
        startingcol=location[1]
        if location[2] == 1:
            ornt = "v"
            #print "this is executing"
            if (startingrow+leng<=boardsize):
                valid =True
                #print i + " vertical fits on board"
        else:
            ornt = "h"
            #print "this is executing this time"
            if (startingcol+leng<=boardsize):
                valid =True
                #print i+"horizontal fits on board"
        if valid ==True:
            #print location
            if ornt == "h":
                for j in range(startingcol, startingcol+leng):
                    #print j
                    if(not(board[startingrow][j] == 'O')):
                        valids =-1
                        #print board[j][startingcol]
                        #print i+"overlapps as many times as this"
                        #apple = raw_input("In")
                    #else:
                        #print board[j][location[1]] +"is O"
            else:
                for j in range(startingrow, startingrow+leng):
                    #print j
                    if(not(board[j][startingcol]=='O')):
                        valids =-1
                        #print board[location[0]][j]
                        #print j
                        #print location[0]
                        #print i+"overlapps as many times as this"
                        #apple = raw_input("In")
                    #else:
                        #print board[location[0]][j] +"is O"
            if valids == 0:
                valids = 1
                #print "doesn't overlap"
    if ornt == "v":
        for j in range(startingrow, startingrow+leng):
            #print board[j][location[1]] +"is O"
            board[j][startingcol] = i
            #print board
            #print ornt
    else:
        for j in range(startingcol, startingcol+leng):
            #print board[location[0]][j] +"is O"
            board[startingrow][j]=i
            #print board
            #print ornt
    apple = raw_input("Press Enter for Computer to hide "+ship)
    print "An intelligence report has come in that computer has hidden "+ship+" Why did you press Enter??"
    return board

def win(board):
    #print "this is working"
    winned = True
    for row in board:
        #print "still working (shuld prnt 10 times)"
        for point in row:
            if (point == "a"):
                winned = False
                #print "should print 5/4 times"
            elif (point =='b'):
                winned = False
                #print "no probs here"
            elif (point =='c'):
                winned = False
                #print "this is tedious"
            elif (point =='d'):
                winned = False
                #print "stuffs"
            elif (point =='s'):
                winned = False
                #print "should print"
    #print str(winned) + "T/F value that should be returnable / calculatable"
    return winned

def sunk(board, i):
    sunked = True
    for row in board:
        for point in row:
            if (point == i):
                sunked = False
    return sunked

def guess(board, guess):
    #winned = False
    new = False
    if (board[guess[0]][guess[1]] == 'O'):
        new = True
        board[guess[0]][guess[1]] = 'X'
        print "Splash!!"
    elif (board[guess[0]][guess[1]] == 'a'):
        new = True
        board[guess[0]][guess[1]] = 'A'
        print "Aircraft Carrier has been hit!"
        if sunk(board, 'a'):
            print "Aircraft Carrier has been sunk"
            #if win(board):
                #winned = True
    elif (board[guess[0]][guess[1]] == 'b'):
        new = True
        board[guess[0]][guess[1]] = 'B'
        print "Battleship has been hit!"
        if sunk(board, 'b'):
            print "Battleship has been sunk"
            #if win(board):
                #winned = True
    elif (board[guess[0]][guess[1]] == 'c'):
        new = True
        board[guess[0]][guess[1]] = 'C'
        print "Cruiser has been hit!"
        if sunk(board, 'c'):
            print "Cruiser has been sunk"
            #if win(board):
                #winned = True
    elif (board[guess[0]][guess[1]] == 'd'):
        new = True
        board[guess[0]][guess[1]] = 'D'
        print "Destroyer has been hit!"
        if (sunk(board, 'd')):
            print "Destroyer has been sunk"
            #if (win(board)):
                #winned = True
    elif (board[guess[0]][guess[1]] == 's'):
        new = True
        board[guess[0]][guess[1]] = 'S'
        print "Submarine has been hit!"
        if sunk(board, 's'):
            print "Submarine has been sunk"
            #if (win(board)):
                #winned = True
    #return(board, winned, new)
    #print_board(board)
    return(board, new)

def humanguess(board):
    validguess = False
    validsguess = False
    #humwin = False
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
        if temp2:
           launch.append(temp)
        #print "To what coordinates (0-9) do you wish to launch this missle? Input as (row, column)"
           temp = raw_input("To which column coordinate (0-"+str(boardsize-1)+") do you wish to launch this missile? ")
           try:
               temp = int(temp)
               temp2 = True
           except ValueError:
               temp2 = False
               print "You hit the treasury for your missile supplier and caused confusion. You get a free additional launch."
           if temp2:
               launch.append(temp)
        #launch.append(int(raw_input("To which column coordinate (0-"+str(boardsize-1)+") do you wish to launch this missile? ")))
               if (launch[0]<0 or launch[0]>=boardsize or launch[1]<0 or launch[1]>=boardsize):
              
                    print "That is beyond the scope of our missiles. Command a launch to somewhere else."
                    apple = raw_input("Press Enter to continue...")
               else:
                    validguess = True
        if validguess ==True:
            validsguess = (guess(board, launch))[1]
            if validsguess == False:
                print "You have already directed a missile launch to those coordinates. Your supervisor won't let you direct a launch there again." 
                print "You must choose different coordinates."
            apple = raw_input("Press Enter to continue...")
    board = (guess(board, launch))[0]
    stealth_print(board)
    #humwin = (guess(board, launch))[1]
    #return (board, humwin)
    return(board)

def compguess(board): 
    print "An enemy missile is heading for your ocean!!"
    apple = raw_input("Press Enter to see what your ocean looks like thus far...")
    print_board(board)
    apple = raw_input("Press Enter to continue...")
    validsguess = False
    while (validsguess ==False):
        launch = [randint(0,boardsize-1), randint(0,boardsize-1)]
        validsguess = (guess(board, launch))[1]
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

for x in range(boardsize):
   board1.append(["O"] * boardsize)
for x in range(boardsize):
   board2.append(["O"]*boardsize)

print "Congratulations. You have just been promoted to naval Commander."
print "With war imminent, we are taking all the precautions we must."
print "We have counted our supplies, trained the troops, and secured "+num+" whole ships."

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
#print_board(board2)


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