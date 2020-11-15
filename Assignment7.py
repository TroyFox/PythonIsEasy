"""
Homework Assignment #7: Dictionaries and Sets


Details:
 
Return to your first homework assignments, when you described your favorite song. Refactor that code so all the variables are held as dictionary 
keys and value. Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's 
key and then it's value.


Extra Credit:

Create a function that allows someone to guess the value of any key in the dictionary, and find out if they were right or wrong. This function 
should accept two parameters: Key and Value. If the key exists in the dictionary and that value is the correct value, then the function should 
return true. In all other cases, it should return false.


Submitted by: Jansen Gomez
"""


MyFavSong = {"SongTitle": "Don't Stop Believin'", "Artist": "Journey", "Album": "Escape", "Released": "October 1981", "Recorded": 1981, 
"Studio": "Fantasy Studios, Berkeley, California", "Genre": "Rock", "Length": 4.18333, "Label": "Columbia", "Songwriters": 
"Steve Perry, Jonathan Cain, Neal Schon", "Producers": "Kevin Elson, Mike ''Clay'' Stone"}

SongAttributesList = ["SongTitle","Artist","Album","Released","Recorded","Studio","Genre","Length","Label","Songwriters","Producers"]

LengthOfMyFavSong = len(MyFavSong)

# just a heading
print("")
print("''My Favorite Song''")
print("")

# Show attributes and its values
for i in range(11):
    print(SongAttributesList[i],end=": ") 
    print(MyFavSong[SongAttributesList[i]])

print("") # to insert space

# Function to determine result of the inputted answers
def GuessTheValue(SongAttribute,SongValue):
    if SongAttribute not in MyFavSong: # attribute entered not found in the list
        return 'False , no such attribute in the list.'
    elif MyFavSong[SongAttribute] == SongValue:
        return True
    else:
        return False

# Ask the user to input data
print("Select and Type the song's attribute from the list and guess the attribute's value:")
print("Attribute list", SongAttributesList)
print("")
SongAttribute=input("Enter Attribute: ")
SongValue = input("Enter Value: ")
print("")

# Show result 
print("Result: ",end="")
print(GuessTheValue(SongAttribute, SongValue))
print("")