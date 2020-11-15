"""
Project #1: A Simple Game


Details:
 
Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. In this project, your task is create a Connect 4 game in 
Python. Before you get started, please watch this video on the rules of Connect 4:

https://youtu.be/utXzIFEVPjA

Once you've got the rules down, your assignment should be fairly straightforward. You'll want to draw the board, and allow two players to take 
turns placing their pieces on the board (but as you learned above, they can only do so by choosing a column, not a row). The first player to 
get 4 across or diagonal should win!

Normally the pieces would be red and black, but you can use X and O instead.


Extra Credit:

Want to try colorful pieces instead of X and O? First you'll need to figure out how to import a package like termcolor into your project. 
We're going to cover importing later in the course, but try and see if you can figure it out on your own. Or you might be able to find unicode 
characters to use instead, depending on what your system supports. Here's a hint: print(u'\u2B24')


Submitted by:  Jansen Gomez

"""
from termcolor import colored, cprint

# draw a dynamic board size... just for experimental purposes
def drawField(Field,rows,columns):
    for row in range(rows*2):
        if row % 2 == 0: # 0,2,4
                         # 0,1,2
            practicalRow = int(row/2)
            for column in range(columns*2-1): # 0,1,2,3,4
                                    # 0,.,1,.,2
                if column % 2 == 0: 
                    practicalColumn = int(column/2)
                    if column != (columns-1)*2:
                        print(Field[practicalColumn][practicalRow], end="")
                    else:    
                        print(Field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-"*(columns*2-1))

    return True


nrOfRows = 6
nrOfColumns = 7

currentField1 = []
currentField2 = []
for row in range(nrOfRows):
    currentField1.append(" ")
for column in range(nrOfColumns):
    currentField2.append(currentField1)

cprint("\nCONNECT 4 GAME about to start --- Players ready!!!","yellow",attrs=['bold'])
print("Player 1 ->", colored("O","yellow",attrs=['bold']) ," Player 2 ->", colored("X","red",attrs=['bold']), "\n")
drawField(currentField2,nrOfRows,nrOfColumns)


currentField =[[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],
                 [" "," "," "," "," "," "],[" "," "," "," "," "," "]]


# Check column's availability
def checkColumn(columnSelected):
    for i in range(5,-1,-1):
        if currentField[columnSelected-1][i] == " ":
            return i

    if currentField[columnSelected-1][i] != " ":
        cprint("THE COLUMN YOU SELECTED IS FULL! PLEASE SELECT ANOTHER COLUMN..\n","red",attrs=['bold'])
        return 8 # to represent full stack


# Check for complete 4 across, vertical or diagonal
def checkAcross(column,row,shape):
    counter = 0
    for i in range(0,7):
        if currentField[i][row] == shape:
            counter = counter + 1
            if counter == 4:
                break
        else:
            counter = 0
    
    if counter == 4:
        return "Winner"
    else:
        return "Continue"

def checkVertical(column,row,shape):
    counter = 0
    for i in range(0,6):
        if currentField[column][i] == shape:
            counter = counter + 1
            if counter == 4:
                break
        else:
            counter = 0
    
    if counter == 4:
        return "Winner"
    else:
        return "Continue"

def checkDiagonal(column,row,shape):
    counter = 0
    start = 0
    total=column+row
    if total > 5:
        start = total - 5
    #Diagonal to upper right
    for i in range(0,total-start+1):
        if i+start > 6:
            break
        if currentField[i+start][total-start-i] == shape:
            counter = counter + 1
            if counter == 4:
                break
        else:
            counter = 0
    
    if counter == 4:
        return "Winner"
    else:

        #Diagonal to lower right
        if column <= row:
            y = row-column
            limit = 6 - y
            x=0
        else:
            x = column - row
            limit = 7 - x
            y=0
        for i in range(0,limit):
            if currentField[i+x][i+y] == shape:
                counter = counter + 1
                if counter == 4:
                    break
            else:
                counter = 0

        if counter == 4:
            return "Winner"

        return "Continue"

def isWinner(column,row,shape):

    if checkAcross(column,row,shape) == "Winner":
        return True
    elif checkVertical(column,row,shape) == "Winner":
        return True
    elif checkDiagonal(column,row,shape) == "Winner":
        return True
    else:
        False


def selectColumn():
    while(True):
        columnSelected = input("Please select column(1-7 only):")
        #print("\n")
        if not columnSelected.isdigit() : 
            cprint("YOU HAVE NOT ENTERED ANY NUMBER! PLEASE TRY AGAIN!\n","red",attrs=['bold'])
        elif int(columnSelected) > 7:
            cprint("PLEASE ENTER NUMBERS 1 - 7 ONLY! THANK YOU! \n","red",attrs=['bold'])
        else:
            return int(columnSelected)

Player = 1
while(True):
    if Player == 1:
        symbol =colored("O","yellow",attrs=['bold'])
        Players = " 1-[" + symbol + "]"
    else:
        symbol =colored("X","red",attrs=['bold'])
        Players = " 2-[" + symbol + "]"

    print("\nPlayer" + Players + ", it's your turn!\n")

    columnSelected = selectColumn()

    #check column
    EmptyRow = checkColumn(columnSelected)
    while (EmptyRow == 8):
        EmptyRow = selectColumn()

    if Player == 1:
        #make move for player 1
        currentField[columnSelected-1][EmptyRow]=colored("O","yellow",attrs=['bold'])
        Player = 2
    else:
        #make move for player 2
        currentField[columnSelected-1][EmptyRow]=colored("X","red",attrs=['bold'])
        Player = 1

    # Show Result
    drawField(currentField,nrOfRows,nrOfColumns)   

    if isWinner(columnSelected-1,EmptyRow,currentField[columnSelected-1][EmptyRow]):

        if currentField[columnSelected-1][EmptyRow] == colored("X","red",attrs=['bold']):
            winner = "2"
        else:
            winner = "1"
        
        result1 = colored("\n... AND THE WINNER IS PLAYER ","yellow",attrs=['bold'])  
        result2 = colored( winner + "!!! CONGRATULATIONS!!!\n\n","yellow",attrs=['bold'])
        print(result1,end="")
        print(result2)
        break