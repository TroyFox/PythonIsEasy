"""
Homework Assignment #6: Advanced Loops


Details:
 
Create a function that takes in two parameters: rows, and columns, both of which are integers. The function should then proceed to draw a 
playing board (as in the examples from the lectures) the same number of rows and columns as specified. After drawing the board, your function 
should return True.


Extra Credit:

Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. If someone passes a value 
greater than either maximum, your function should return False.

Submitted by: Jansen Gomez
"""

# Function board with 2 parameters: rows and columns
def board(rows,columns):

    # Maximum height and width of my terminal and screen without wrapping
    maxHeight = 8
    maxWidth = 85

    # Start drawing the board
    for row in range(rows*2-1):
        if row%2 == 0:
              for column in range(1,columns*2):
                  if column%2 == 1:
                      if column != columns*2-1:
                          print(" ", end="")
                      else:
                          print(" ")
                  else:
                      print("|",end="")
        else:
            print("-"*(columns*2-1))
        
    # return True if maxHeight and maxWidth have not been exceeded, otherwise return False    
    if rows > maxHeight:
        return False
    elif columns > maxWidth:
        return False
    else:
        return True

# user inputs number of rows and columns inside board function --- board(rows,columns)
result = board(7,90)

print(result)