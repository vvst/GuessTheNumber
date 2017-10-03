# Computer guesses the user number game

import random

UserNumber = int(input("Write a number 1-100: "))

NumberOfTries = 0
CompGuess = 0

a = 1
b = 100

while CompGuess != UserNumber:
    CompGuess = random.randint(a,b)
    if CompGuess > UserNumber:
        b = CompGuess-1
    elif CompGuess < UserNumber:
        a = CompGuess+1
    NumberOfTries += 1
    print(CompGuess)
    
print("\nTries: ", NumberOfTries)
    
