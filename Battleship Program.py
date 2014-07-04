#This program was created using Python 2.7
import string
import random

gameboard=[]
game=False
print "Please set the pieces according to row and column, such as B2h for horizontal or C4v for vertical placement"

#The AI creates a choice and then a counter using a divide and conquer approach
#If it his the area that it has specified in the row and column, it will attack
#The same area again using a divide and conquer approach
def compAI():
    #I have global ints that do the counter so that if the area is hit in a certain section, it will shoot the shot in the area that is designated and it should shoot one more time.
    #Hits keep track of the total hits, which should be three because we only have to hit a battleship once in order for it to sink.
    #Steps keep track of how many steps that this program has taken in order to solve the battleship program.
    global counter
    global hits
    global steps
    #Choice is random because you have to start in a random section before you find the battleships in the other sections
    choice=random.choice(range(1,7))
    if (counter==0):
        #These ranges represent the divide and conquer part that I am implementing for the gameboard.
        if(choice==1):
            row=random.choice(range(0,2))
            column=random.choice(range(0,10))
        elif(choice==2):
            row=random.choice(range(2,4))
            column=random.choice(range(0,10))
        elif(choice==3):
            row=random.choice(range(4,6))
            column=random.choice(range(0,10))
        elif(choice==4):
            row=random.choice(range(5,7))
            column=random.choice(range(0,10))
        elif(choice==5):
            row=random.choice(range(7,9))
            column=random.choice(range(0,10))                 
        elif(choice==6):
            row=random.choice(range(8,10))
            column=random.choice(range(0,10))
        try:
            #If the space is not blank, the computer hits.
            if gameboard[row][column] != " ":
                gameboard[row][column] = " "
                print "Computer shot: %s%d" %(translaterow(row),column)
                print "Computer:Hit"
                hits=hits+1
                counter=choice
                steps=steps+1
                print "Steps: %s" % steps
                printboard()
            else:
                print "Computer shot: %s%d" %(translaterow(row),column)
                counter=0
                steps=steps+1
                print "Steps: %s" % steps
        except:
            compAI()
            #Almost the same thing as above, except if there is a hit, the counter will go to the same area the hit was in, which is another part of the divide and conquer approach
    else:
        choice=counter
        if(counter==1):
            row=random.choice(range(0,2))
            column=random.choice(range(0,10))
        elif(counter==2):
            row=random.choice(range(2,4))
            column=random.choice(range(0,10))
        elif(counter==3):
            row=random.choice(range(4,6))
            column=random.choice(range(0,10))
        elif(counter==4):
            row=random.choice(range(5,7))
            column=random.choice(range(0,10))
        elif(counter==5):
            row=random.choice(range(7,9))
            column=random.choice(range(0,10))               
        elif(counter==6):
            row=random.choice(range(8,10))
            column=random.choice(range(0,10))
        try:
            if gameboard[row][column] != " ":
                gameboard[row][column] = " "
                print "Computer shot: %s%d" %(translaterow(row),column)
                print "Computer:Hit"
                hits=hits+1
                counter=choice
                steps=steps+1
                print "Steps: %s" % steps
                printboard()
            else:
                print "Computer shot: %s%d" %(translaterow(row),column)
                counter=0
                steps=steps+1
                print "Steps: %s" % steps
        except:
            compAI()
#This class prompts the user to place his battleships, and will throw an
#Exception if it doesn't work
def prompt(piece):
    if piece=="b":
        inpt=list(raw_input("Set Battleship At: "))
        try:
            row=findrow(inpt[0].upper())
            column=string.atoi(inpt[1])
            oren=inpt[2]
            placepieces(gameboard,"b",row,column,oren)
            printboard()
        except:
            print "Can't play there"
            prompt(piece)


#This will find a row that the battleship will be placed on        
def findrow(a):
    if a=="A":
        return 0
    elif a=="B":
        return 1
    elif a=="C":
        return 2
    elif a=="D":
        return 3
    elif a=="E":
        return 4
    elif a=="F":
        return 5
    elif a=="G":
        return 6
    elif a=="H":
        return 7
    elif a=="I":
        return 8
    elif a=="J":
        return 9
 #This actually is the handler for the pieces that the user will put down   
def placepieces(board,piece,row,column,oren):
    if piece=="b":
        if oren=="h":
            try:
                if board[row][column]==" " and board[row][column+1]==" " and board[row][column+2]==" " and board[row][column+3]==" " and board[row][column+4]==" ":
                    for i in range(0,5):
                        board[row][column+i]="B"
                    return
                #If placement is invalid, will throw a cannot place it here
                else:
                    print "Cannot place it there"
                    prompt(piece)
            except:
                print "Cannot place it there"
                prompt(piece)
        if oren=="v":
            try:
                if board[row][column]==" " and board[row+1][column]==" " and board[row+2][column]==" " and board[row+3][column]==" " and board[row+4][column]==" ":
                    for i in range(0,5):
                        board[row+i][column]="B"
                    return
                else:
                    print "Cannot place it there"
                    prompt(piece)
            except:
                print "Cannot place it there"
                prompt(piece)
#This will translate the row that the user places his pieces on
def translaterow(a):
    if a==0:
        return "A"
    elif a==1:
        return "B"
    elif a==2:
        return "C"
    elif a==3:
        return "D"
    elif a==4:
        return "E"
    elif a==5:
        return "F"
    elif a==6:
        return "G"
    elif a==7:
        return "H"
    elif a==8:
        return "I"
    elif a==9:
        return "J"
#This will create the board rows and columns 0-9
def createboard():
    for i in range(0,10):
        gameboard.append([])
        for j in range(0,10):
            gameboard[i].append(" ")            


#This will print the board when the computer hits
def printboard():
    print "   0   1   2   3   4   5   6   7   8   9  "
    print "A| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[0][0],gameboard[0][1],gameboard[0][2],gameboard[0][3],gameboard[0][4],gameboard[0][5],gameboard[0][6],gameboard[0][7],gameboard[0][8],gameboard[0][9])
    print "B| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[1][0],gameboard[1][1],gameboard[1][2],gameboard[1][3],gameboard[1][4],gameboard[1][5],gameboard[1][6],gameboard[1][7],gameboard[1][8],gameboard[1][9])
    print "C| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[2][0],gameboard[2][1],gameboard[2][2],gameboard[2][3],gameboard[2][4],gameboard[2][5],gameboard[2][6],gameboard[2][7],gameboard[2][8],gameboard[2][9])
    print "D| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[3][0],gameboard[3][1],gameboard[3][2],gameboard[3][3],gameboard[3][4],gameboard[3][5],gameboard[3][6],gameboard[3][7],gameboard[3][8],gameboard[3][9])
    print "E| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[4][0],gameboard[4][1],gameboard[4][2],gameboard[4][3],gameboard[4][4],gameboard[4][5],gameboard[4][6],gameboard[4][7],gameboard[4][8],gameboard[4][9])
    print "F| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[5][0],gameboard[5][1],gameboard[5][2],gameboard[5][3],gameboard[5][4],gameboard[5][5],gameboard[5][6],gameboard[5][7],gameboard[5][8],gameboard[5][9])
    print "G| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[6][0],gameboard[6][1],gameboard[6][2],gameboard[6][3],gameboard[6][4],gameboard[6][5],gameboard[6][6],gameboard[6][7],gameboard[6][8],gameboard[6][9])
    print "H| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[7][0],gameboard[7][1],gameboard[7][2],gameboard[7][3],gameboard[7][4],gameboard[7][5],gameboard[7][6],gameboard[7][7],gameboard[7][8],gameboard[7][9])
    print "I| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[8][0],gameboard[8][1],gameboard[8][2],gameboard[8][3],gameboard[8][4],gameboard[8][5],gameboard[8][6],gameboard[8][7],gameboard[8][8],gameboard[8][9])
    print "J| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" %(gameboard[9][0],gameboard[9][1],gameboard[9][2],gameboard[9][3],gameboard[9][4],gameboard[9][5],gameboard[9][6],gameboard[9][7],gameboard[9][8],gameboard[9][9])


#This will begin the game and handles the different classes and game logic
def begingame():
    global gameboard
    gameboard=[]
    createboard()
    printboard()
    prompt("b")
    prompt("b")
    prompt("b")
    global game
    game=True
begingame()
#initalize the global variables that shall be initalized for the game
hits=0
counter=0
steps=0
#If the hits for the ships are not three, it would end the while loop.
while(hits != 3):
    compAI()
