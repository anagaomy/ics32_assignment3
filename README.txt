# Assignment2 README

# Name: Ana Gao
# Email: gaomy@uci.edu
# Student ID: 26384258


This program provides the basic file management and user interface aspects of your new program 
while you add new features to support basic journaling and journal management functionality.

The File System Inspector should have a fully functional command line program that allows user to 
find, create, read, and delete files on your computer.

Also, this program will allow the user to publish individual posts to a remote server where 
others can read what they have to say. The journal entries will be stored locally (on the computer) 
with an option to be shared on the Internet, any server that supports the ICS32 DSP. 

To use this tool, simply enter a command and specify the directory or file you wish to inspect. 

The program should enter into administrator mode when receiving the user input 'admin'. 

The user input for admin mode in this program will take the following format:

    [COMMAND] [INPUT] [[-]OPTION] [INPUT]


Available program commands:

    'PO'    - Publish a post online
    'C'     - Create a new file in the specified directory.
    'O'     - Open an existing file of the type DSU
    'L'     - List the contents of the user specified directory.
    'D'     - Delete the file.
    'R'     - Read the contents of a file.
    'Q'     - Quit the program.


Options of the 'L' command:
    
    '-r' - Output directory content recursively.
    '-f' - Output only files, excluding directories in the results.
    '-s' - Output only files that match a given file name.
    '-e' - Output only files that match a given file extension.


Options of the 'C' and 'O' command:

    '-n' - Specify the name to be used for a new file
    'E'  - Edit the DSU file
    'P'  - Print data stored in the DSU file


'E' command feature:

    -svr [SERVER IP ADDRESS]
    -usr [USERNAME]
    -pwd [PASSWORD]   
    -bio [BIO] 
    -addpost [NEW POST] 
    -delpost [ID] 
    -publish


'P' command feature:

    '-usr'      - Prints the username stored in the profile object
    '-pwd'      - Prints the password stored in the profile object
    '-bio'      - Prints the bio stored in the profile object
    '-posts'    - Prints all posts stored in the profile object with their ID
    '-post'     - Prints post identified by ID
    '-all'      - Prints all content stored in the profile object
    '-publish'  - Publish a post from a list of all entries

When an error occurs, the program will inform the user by printing ‘ERROR’ and wait for additional input from the user.