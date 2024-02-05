# Program to generate a random password
import string 
import random

characters = list ( string.ascii_letters + string.digits + "!@#$%^&*()_+" )

def generatePassword():

    pass_length = int(input("What must be the lenght of your password :"))

    random.shuffle(characters)
    password = []
    
    for i in range(pass_length):
        password.append(random.choice(characters))
    random.shuffle(password)

    password = "".join(password)
    print("Here's your password ==> ",password)

option = input("Do you want to generate a strong password? (Yes/No)")

if option == "Yes":
    generatePassword()
elif option == "No":
    print("GoodBye")
else :
    print("Invalid input")