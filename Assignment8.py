"""
Homework Assignment #8: Input and Output (I/O)


Details:
 
Create a note-taking program. When a user starts it up, it should prompt them for a filename.

If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, 
it should save the file and exit.

If they enter a file name that already exists, it should ask the user if they want:

A) Read the file

B) Delete the file and start over

C) Append the file

If the user wants to read the file it should simply show the contents of the file on the screen. If the user wants to start over then the file 
should be deleted and another empty one made in its place. If a user elects to append the file, then they should be able to enter more text, and 
that text should be added to the existing text in the file. 



Extra Credit:

Allow the user to select a 4th option:

D) Replace a single line

If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:

1) The line number they want to update.

2) The text that should replace that line.


Submitted by: Jansen Gomez

"""

import os.path

filename = input("\nPlease enter the filename: ")

#Check if filename entered already exists
fileExists = os.path.exists(filename)

#print("fileExists = ", fileExists)

if fileExists == False:
    NoteFile = open(filename,"w")
    content = input("\nNew file detected! Please enter text you want to write in the file: ")
    NoteFile.write(content + "\n")
    NoteFile.close
    print("\nYour text is now saved to the file! Congratulations!\n")

else:
    choice = input("\nFile exists! Please enter what do you want to do with this file: \n"
                   "     A) Read the file \n"
                   "     B) Delete the file and start over  \n"
                   "     C) Append the file  \n"
                   "     D) Replace a single line \n"
                   " \n"
                   "Please enter the letter of your choice: ")
                
    if choice == 'A' or choice == 'a':
        with open(filename,"r") as NoteFile:
            print("\nYour choice is... A) Read the file\n\nYour file is read as follows:", NoteFile.read())

    if choice == 'B' or choice == 'b': 
        print("\nYour choice is... B) Delete the file and start over\n\nNow deleting file and starting over... \n")
        os.remove(filename)
        NoteFile = open(filename,"w")
        NoteFile.close()

    if choice == 'C' or choice == 'c':
        print("\nYour choice is... C) Append the file \n")
        moreText = input("Please enter additional text you may want to add to the file: ")
        with open(filename,"a") as NoteFile:
            NoteFile.write("\n"+moreText)
            print("\nAdditional text of '" + moreText + "' has now been added to the file.\n")
        with open(filename,"r") as NoteFile:
            print("Result:\n", NoteFile.read())

    if choice == 'D' or choice == "d":
        lineToBeReplaced = int(input("Please enter the line nr to be replaced: "))-1
        lineText = input("Please enter the text to replace the existing one: ")
        
        with open(filename,'r') as NoteFile:
            data=NoteFile.readlines()
		
        data[lineToBeReplaced]=lineText+"\n"
        print("\nLine number",lineToBeReplaced+1,"of the file has been replaced with the text: ",lineText)

        with open(filename,'w') as NoteFile:
            NoteFile.writelines(data)
        with open(filename,'r') as NoteFile:
            print("\nResult:\n", NoteFile.read())



