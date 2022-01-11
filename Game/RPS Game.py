import random

def Mygame(computer,you):
    if computer==you:
        print("The Game is Tie!")
    elif computer=="r":
        if you=="p":
            print("You Won!")
        elif you=="s":
            print("You Lose!")
    elif computer=="p":
        if you=="s":
            print("You Won!")
        elif you=="r":
            print("You Lose!")
    elif computer=="s":
        if you=="r":
            print("You Won!")
        elif you=="p":
            print("You Lose!")

computer=random.randint(1,3)
print("Computer Turn: Choose one from it Rock(r), Paper(p), Scissor(s) \nComputer has chosen !")
you=input("You'r Turn: Choose one from it Rock(r), Paper(p), Scissor(s):")
if computer==1:
    computer="r"
elif computer==2:
    computer="p"
elif computer==3:
    computer="s"

print(f"Computer Choose {computer}")
print(f"You Choose {you}")

Mygame(computer,you)