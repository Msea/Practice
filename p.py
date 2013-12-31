def createboard():
   board = []
   for x in range(3):
      board.append(["O"] * 3)
   return board


def smoothjoin(A, B, C, D):
   bigboard = []
   for i in range(3):
      temp = []
      for j in range(3):
         temp.append(A[i][j])
      for j in range(3):
         temp.append(B[i][j])
      bigboard.append(temp)
   for i in range(3):
      temp = []
      for j in range(3):
         temp.append(C[i][j])
      for j in range(3):
         temp.append(D[i][j])
      bigboard.append(temp)
   return bigboard

def sepboards(board):
   A = []
   B = []
   C = []
   D = []
   for i in range(3):
      temp=[]
      for j in range(3):
         temp.append(board[i][j])
      A.append(temp)
   for i in range(3):
      temp=[]
      for j in range(3):
         temp.append(board[i][j+3])
      B.append(temp)
   for i in range(3):
      temp=[]
      for j in range(3):
         temp.append(board[i+3][j])
      C.append(temp)
   for i in range(3):
      temp=[]
      for j in range(3):
         temp.append(board[i+3][j+3])
      D.append(temp)
   return (A, B, C, D)
   
def joinboards(board):
   A=sepboards(board)[0]
   B=sepboards(board)[1]
   C=sepboards(board)[2]
   D=sepboards(board)[3]
   bigboard = []
   bigboard.append(["  ", "a", "b", "c", " ", "d", "e", "f"])
   bigboard.append(["  ", " ", " ", " ", " ", " ", " ", " "])
   for i in range(3):
      temp = [str(i+1)+" "]
      for j in range(3):
         temp.append(A[i][j])
      temp.append("|")     
      for j in range(3):
         temp.append(B[i][j])
      bigboard.append(temp)
   bigboard.append("  ------")
   for i in range(3):
      temp = [str(i+4)+" "]
      for j in range(3):
         temp.append(C[i][j])
      temp.append("|")
      for j in range(3):
         temp.append(D[i][j])
      bigboard.append(temp)
   return bigboard
      
def quadboards(board):
   A=sepboards(board)[0]
   B=sepboards(board)[1]
   C=sepboards(board)[2]
   D=sepboards(board)[3]
   bigboard = []
   bigboard.append(["  ", "A", "A", "A", " ", "B", "B", "B"])
   bigboard.append(["  ", " ", " ", " ", " ", " ", " ", " "])
   for i in range(3):
      temp = ["A "]
      for j in range(3):
         temp.append(A[i][j])
      temp.append("|")     
      for j in range(3):
         temp.append(B[i][j])
      temp.append(" B")
      bigboard.append(temp)
   bigboard.append("  ------")
   for i in range(3):
      temp = ["C "]
      for j in range(3):
         temp.append(C[i][j])
      temp.append("|")
      for j in range(3):
         temp.append(D[i][j])
      temp.append(" D")
      bigboard.append(temp)
   bigboard.append(["  ", " ", " ", " ", " ", " ", " ", " "])
   bigboard.append(["  ", "C", "C", "C", " ", "D", "D", "D"])
   return bigboard

def print_board(board):
    for row in board:
         print " ".join(row)
    return board

def to_num(a):
   if a == "a":
      a=1
   elif a == "b":
      a=2
   elif a == "c":
      a=3
   elif a == "d":
      a=4
   elif a == "e":
      a=5
   elif a == "f":
      a=6
   else:
      a=0
   return a


def placement(user, color, board):
    show = joinboards(board)
    validplace = False
    validsplace = False
    validrow = False
    print "This is what the game board looks like now"
    print""
    print_board(show)
    while (validsplace ==False):
        validrow=False
        validplace = False
        pl = []
        temp = raw_input(user+", in which row (1-6) do you wish to place your marble? ")
        if not((temp=="1")or(temp=="2")or(temp=="3")or(temp=="4")or(temp=="5")or(temp=="6")):
            print "Not an option"
            stuffs = raw_input("Press Enter to try again.")
        else:
            validrow = True
            pl.append(int(temp))
        if validrow:
           temp = raw_input(user+", In which column (a-f) do you wish to place your marble? ")
           if not((temp=="a")or(temp=="b")or(temp=="c")or(temp=="d")or(temp=="e")or(temp=="f")):
               print "Not an option"
               stuffs = raw_input("Press Enter to try again.")
           else:
               temp = to_num(temp)
               pl.append(temp)
               validplace = True
        if validplace==True:
            if ((board[pl[0]-1][pl[1]-1])=="O"):
               validsplace = True
            else:
               print "There is already a marble there."
               stuffs = raw_input("Press Enter to try again.")
            
    board[pl[0]-1][pl[1]-1]=color
    return board

def rotateboard(board, user):
   A=sepboards(board)[0]
   B=sepboards(board)[1]
   C=sepboards(board)[2]
   D=sepboards(board)[3]
   validplace = False
   print "This is what the game board looks like now"
   print""
   print_board(quadboards(board))
   while (validplace==False):
        quad = raw_input(user+", which quadrant (A-D) do you wish to rotate? ")
        if not((quad=="A")or(quad=="B")or(quad=="C")or(quad=="D")):
            print "Not an option"
            stuffs = raw_input("Press Enter to try again.")
        else:
            dir = raw_input("Do you wish to rotate "+quad+" clockwise (cw) or counter-clockwise (cc)? ")
            if not((dir=="cw")or(dir=="cc")):
               print "Not an option"
               stuffs = raw_input("Press Enter to try again.")
            else:
               validplace=True
               if quad =="A":
                  Q=A
               if quad =="B":
                  Q=B
               if quad =='C':
                  Q=C
               if quad=='D':
                  Q=D
               if (dir=="cw"):
                  temp = Q[0][0]
                  Q[0][0] = Q[2][0] 
                  Q[2][0] = Q[2][2]
                  Q[2][2] = Q[0][2]
                  Q[0][2] = temp
                  temp = Q[0][1]
                  Q[0][1] = Q[1][0]
                  Q[1][0] = Q[2][1]
                  Q[2][1] = Q[1][2]
                  Q[1][2] = temp
               elif (dir=="cc"):
                  temp = Q[0][0]
                  Q[0][0] = Q[0][2] 
                  Q[0][2] = Q[2][2]
                  Q[2][2] = Q[2][0]
                  Q[2][0] = temp
                  temp = Q[0][1]
                  Q[0][1] = Q[1][2]
                  Q[1][2] = Q[2][1]
                  Q[2][1] = Q[1][0]
                  Q[1][0] = temp
               else:
                  print"this should not print"
   if quad =='A':
      board = smoothjoin(Q, B, C, D)
   elif quad =='B':
      board = smoothjoin(A, Q, C, D)
   elif quad =='C':
      board = smoothjoin(A, B, Q, D)
   else:
      board = smoothjoin(A, B, C, Q)
   return board

def win5(five):
   winned=False
   if ((five[0]=='R')or(five[0]=='G')):
      if ((five[0]==five[1])and(five[2]==five[1])and(five[2]==five[3])and(five[3]==five[4])):
         winned=True
   return winned

def checkwin(board):
   winned=False
   initals = []
   for i in range(6):
      for j in range(2):
         temp = []
         for k in range(5):
            temp.append(board[i][j+k])
         if(win5(temp)):
            winned = True
            initals.append([[i, j], "hors"])
   for i in range(6):
      for j in range(2):
         temp = []
         for k in range(5):
            temp.append(board[j+k][i])
         if(win5(temp)):
            winned = True
            initals.append([[j, i], "ver"])
   for i in range(2):
      for j in range(2):
         temp=[]
         for k in range(5):
            temp.append(board[i+k][j+k])
         if(win5(temp)):
            winned = True
            initals.append([[i, j], "neg"])
   for i in range(2):
      for j in range(2):
         temp=[]
         for k in range(5):
            temp.append(board[i+k][j+4-k])
         if(win5(temp)):
            winned = True
            initals.append([[i, j+4], "pos"])
   return (winned, initals)

def whenwin(board, init):
   for point in init:
      if point[1]=="hors":
         for j in range(5):
            board[ (point[0])[0] ] [ (point[0])[1]+j ]=board[(point[0])[0]][(point[0])[1]+j].lower()
      if point[1]=="ver":
         for j in range(5):
            board[(point[0])[0]+j][(point[0])[1]]=board[(point[0])[0]+j][(point[0])[1]].lower()
      if point[1]=="neg":
         for j in range(5):
            board[(point[0])[0]+j][(point[0])[1]+j]=board[(point[0])[0]+j][(point[0])[1]+j].lower()
      if point[1]=="pos":
         for j in range(5):
            board[(point[0])[0]+j][(point[0])[1]-j]=board[(point[0])[0]+j][(point[0])[1]-j].lower()
   return board
   
A = createboard()
B = createboard()
C = createboard()
D = createboard()
b=smoothjoin(A, B, C, D)
   


print"Hello Human"
print""

if (raw_input("To read the instructions press <r> folloed by <enter>. Otherwise press any key. ")=='r'):
   print"This is a 2 player game."
   print"Virtual contents:"
   print"The game board is a 6x6 grid made up of 4 removable 3x3 grids arranged in a 2x2 grid, like so:"
   a=raw_input("Press enter to view...")
   print_board(joinboards(smoothjoin(A, B, C, D)))
   print"Each spot on the board is a hole into which one marble can be placed. Each player has 250 marbles of their own colour"
   a=raw_input("Press enter to continue...")
   print""
   print"Game Play:"
   print"Players take turns taking turns."
   print "On a players turn he or she will place a marble of his or her own colour on an unoccupied hole in the grid."
   print "Then he or she will choose one of the 4 removable 3x3 boards to rotate 90 degrees in clockwise or counterclockwise around the z axis."
   a=raw_input("Press enter to continue...")
   print""
   print"Win Condition:"
   print"In general when a player has 5 marbles of his or her colour in a row he or she wins the game."
   print"These marbles can be along one of the streight axises or along either diagonal."
   print"Note that the 5-in-a-row can span 2 or 3 of the removable 3x3 boards."
   print"For example the following is a valid 5-in-a-row:"
   a=raw_input("Press enter to view...")
   print_board(joinboards(smoothjoin([["O", "O", "O"], ["R", "O", "O"], ["O", "R", "O"]], [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]], [["O", "O", "R"], ["O", "O", "O"], ["O", "O", "O"]], [["O", "O", "O"], ["R", "O", "O"], ["O", "R", "O"]])))
   a=raw_input("Press enter to continue...")
   print"A win can occur during either the palcement phase or rotating phase of a turn."
   print"If a win occurs during the placement phase, the player placing wins teh gam and does not rotate that turn."
   print"Sometimes a rotation can cause two players to get 5-in-a-row. In these instances the game is a draw."   
   a=raw_input("Press enter to get started!")
print""
nam1=raw_input("Player 1, enter your name.")
nam2=raw_input("Player 2, enter your name.")

bestest = False
player=False
while (bestest==False):
   if player == False:
      name=nam1
      mar='R'
   else:
      name=nam2
      mar='G'
   b = placement(name, mar, b)
   if (checkwin(b))[0]:
      bestest=True
      break
   b = rotateboard(b, name)
   if (checkwin(b))[0]:
      bestest=True
   player = not player

b=(whenwin(b, checkwin(b)[1]))
print_board(joinboards(b))
onwon=False
towon=False
for x in b:
   for y in x:
      if y=="r":
         onwon=True
      elif y=="g":
         towon=True
if(onwon and towon):
   print "Game is a tie."
elif(onwon):
   print nam1 + " wins."
elif(towon):
   print nam2 + " wins."
print "The lower-case letters indicate winning 5 in a row."
