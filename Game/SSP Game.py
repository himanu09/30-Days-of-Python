import random

def Mygame(computer,you):
    if computer==you:
        print("The Game is Tie!")
    elif computer=="S":
        if you=="p":
            print("You Won!")
        elif you=="s":
            print("You Lose!")
    elif computer=="p":
        if you=="s":
            print("You Won!")
        elif you=="S":
            print("You Lose!")
    elif computer=="s":
        if you=="S":
            print("You Won!")
        elif you=="p":
            print("You Lose!")

computer=random.randint(1,3)
print("Computer Turn: Choose one from it Stone(S), Paper(p), Scissor(s):")
you=input("You'r Turn: Choose one from it Stone(S), Paper(p), Scissor(s):")
if computer==1:
    computer="S"
elif computer==2:
    computer="p"
elif computer==3:
    computer="s"

print(f"Computer Choose {computer}")
print(f"You Choose {you}")

Mygame(computer,you)