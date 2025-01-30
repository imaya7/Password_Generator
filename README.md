# Password_Generator
Generates a random 1000 passwords combinations either memorable or random 


## a) Purpose 
The password generator is a code developed in Python to be able to generate two different kinds of passwords random passwords or memorable passwords. The purpose of this project was to create an easy and fast way to generate passwords that are secure for a user to potentially use. The passwords are created in an easy-to-read format and note the time the password was created for the user. The generator prompts the user a question and asks if the user wants to generate passwords or not. If yes is selected the program with randomly select between random or memorable and then return a file containing 1000 generated passwords of one of the two types. 

## b) Libraries/Modules Used 
os - The os library is used for seeing if directories exist and if they don't exist os creates them

random - The random library is used for generating random numbers, characters, and words 

string - The string library contains a collection of strings 

datetime - The datetime library is used for manipulating dates and time 


## c) How to use 
once the code is downloaded and run in Python a message will pop up in the terminal asking the user if they wish to generate a password. If the user answers no a message will pop up in the terminal saying no passwords were generated. If the user says yes Python will randomly choose between random and memorable and develop 1000 passwords for the user, once it's done a message confirming the action will pop up saying which type of password was generated for the user. 


## d) Inputs/ outputs 
Inputs: 
memorable password -type of word (uppercase, lowercase, both) and amount of words 
random password - length, symbols, and exclude characters from the passwords

Outputs: 
generated password txt file for both memorable and random passwords, and a time stamp containing the time passwords were created 

