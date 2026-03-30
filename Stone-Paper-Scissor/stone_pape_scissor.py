
import random
print("Welcome to Stone Paper Scissor game")

choices=["stone","paper","scissor"]

user=input("Enter stone,paper or scissor:").lower()
computer=random.choice(choices)

print("computer:",computer)


# Tie case
if user==computer:
    print("this is tie")

# Your winning cases
elif user=="stone" and computer=="scissor":
    print("You win")
elif user=="paper" and computer=="stone":
    print("You win")
elif user=="scissor"and computer=="paper":
    print("You won")

# computer winning cases
elif computer=="stone" and user=="scissor":
    print("Computer win")
elif computer=="paper" and user=="stone":
    print("Computer win")
elif computer=="scissor"and user=="paper":
    print("Computer win")
else:
    print("Invalide choice! Please enter the Stone, paper or scissor")
