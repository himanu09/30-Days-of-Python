import random

randNum= random.randint(1,100)
userGuess=0
guess=0

print("Welcome to the game \nChoose Right Number ")
while ( userGuess != randNum):
    userGuess = int(input("Enter You'r guess here: "))
    guess += 1
    if (userGuess == randNum):
        print("You have guessed it right !")
    else:
        if (userGuess> randNum):
            print("You guessed it wrong ! Enter a  smaller number")
        else:
            print("You guessed it wrong ! Enter larger number")
print(f"You guess the number in {guess} guesses")