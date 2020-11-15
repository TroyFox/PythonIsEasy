"""
Homework Assignment #2: Functions

Song attributes based from Assignment #1
SongTitle: Don't Stop Believin'

by: Jansen Gomez

"""

def Artist():
    Artist = "Journey"
    return Artist

def Album():
    return "Escape"
    
def Recorded():
    Recorded = 1981 
    return Recorded

var1 = Artist()
var2 = Album()
var3 = Recorded()

print(var1)
print(var2)
print(var3)

# Using booleans
var4 = var1 == var2
var5 = var3 == 1981

print(var4) # result will be 'False'
print(var5) # result will be 'True'

# Using a function to return a Boolean
def BoolResult(var6):

    return var6

ArtistIsJohn = False

var7 = BoolResult(ArtistIsJohn)

print(var7)

