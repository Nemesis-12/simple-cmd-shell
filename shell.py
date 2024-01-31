'''
This is a simple program that replicates some of the CMD commands used commonly 
on Windows by using the subprocess and os libraries. It performs operations such 
as creating directory, listing current directory content, and so on.
'''

import subprocess
import os
import sys

# Define Menu function that offers user options to execute commands
def menu():
    print(''' 
Select an action to perform
[dir]   List Current Directory
[cd]    Change Directory
[mkdir] Create New Directory
[echo]  Display Message
[type]  Concatenate and Display File Content
[q]     Exit
    ''')

# Define Switch function using match-case to help with the option chosen by the 
# user
def switch(usrInput):
    # Match the option selected by the user with the case given below
    match usrInput:
        # Print the contents of current directory
        case "dir":
            try:
                print("Listing directory contents...\n")
                subprocess.run(['dir'], shell = True)
            # If error occurs, print a message to user
            except Exception as e:
                error(e)

        # Print the current directory and ask user input to change directory
        case "cd":
            try:
                print("Current directory: {} \nChange directory to?".format(os.getcwd()))
                usrCmd = input("> ")
                os.chdir(usrCmd)
                print("Current directory: {}".format(os.getcwd()))
            # If error occurs, print a message to user
            except Exception as e:
                error(e)

        # Create a new directory in the current path
        case "mkdir":
            try:
                usrCmd = input("Enter directory name:\n> ")
                os.mkdir(usrCmd)
                print("Created {}".format(usrCmd))
            # If error occurs, print a message to user
            except Exception as e:
                error(e)

        # Display a user written message
        case "echo":
            usrCmd = input("Enter message:\n> ")
            print(usrCmd)

        # The 'type' command helps user create, display and concatenate files
        # It also provides the user an option to write the file names and content
        case "type":
            print('''
            [1] Create File
            [2] Display File
            [3] Concatenate and Display Files
            ''')
            usrCmd = input("> ")

            # Match the option selected by the user with the case given below
            match usrCmd:
                # Create and write to user's file
                case "1":
                    try:
                        fileName = input("Enter file name: ")
                        usrTxt = input("Enter text to write: ")

                        # Write content to the file
                        with open(fileName, 'w') as file:
                            file.write(usrTxt)

                        print("File created")
                    # If error occurs, print a message to user
                    except Exception as e:
                        error(e)

                # Display file contents of the given file
                case "2":
                    try:
                        fileName = input("Enter file name: ")
                        subprocess.run(['cmd', '/c', 'type', fileName], shell = True)
                        print('\n')
                    # If error occurs, print a message to user
                    except Exception as e:
                        error(e)

                # Ask user for files to concatenate, and the file name to
                # store it in. It then displays the contents of created file.
                case "3":
                    try:
                        fileName = input("Enter first file name: ")
                        fileName2 = input("Enter second file name: ")
                        fileName3 = input("Enter file name to concatenate contents to: ")

                        content1 = readFile(fileName)
                        content2 = readFile(fileName2)

                        with open(fileName3, 'w') as file:
                            file.write(content1)
                            file.write('\n')
                            file.write(content2)
                            file.write('\n')

                        print("File created. Displaying file.\n")
                        subprocess.run(['cmd', '/c', 'type', fileName3], shell = True)
                    # If error occurs, print a message to user
                    except Exception as e:
                        error(e)
        # Exit the program
        case "q":
            print("Exiting Program...")
            sys.exit()

# Define function to read given file
def readFile(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
        return content
    # Raise an error if there is an issue when reading files such as permission
    # or file not being found
    except Exception as e:
        error(e)

# Define function to handle any errors
def error(e):
    match e:
        # If file or directory is not found, raise an error
        case FileNotFoundError():
            print("The file(s) or directory does not exist!")

        # If file or directory already exists, raise an error
        case FileExistsError():
            print("The file(s) or directory already exists!")

        # Raise an error if user does not have permissions
        case PermissionError():
            print("You do not have permission to perform this action!")

        # Raise an error if the path specified by user is not a directory
        case NotADirectoryError():
            print("The specified path is not a directory!")

        # Raise error for system related issues such as disk full
        case OSError():
            print(f"An OS error ocurred: {e}")

        # If there is an issue with input or output, raise an error
        case IOError():
            print(f"An unexpected IO error ocurred: {e}")

# Create an infinite loop showing the menu and stop the program once user asks
# to quit
while True:
    menu()
    usrInput = str(input("> "))
    switch(usrInput)