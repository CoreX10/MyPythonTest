#This is a Collatz Program

import sys
import os

#defind a collatz function
def collatz(number):
    if number % 2 == 0:
        return int(number/2)
    elif number % 2 == 1:
        return int(3 * number + 1)
    else:
        return 

#defind a restart_program.
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#type a number 
print ('Please type a number:')
#Avoid input ValueError
try:
    type_number = int(input())
except ValueError:
    #when type Error data, Prompt and restart program.
    print ('Value Error, please try again.')
    restart_program()
else:
    #begin loop
    while True:
        type_number = collatz(type_number)
        print(type_number)
        collatz(type_number)
        if type_number == 1:
            break

