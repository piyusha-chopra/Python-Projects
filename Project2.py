import random

print("WELCOME TO SNAKE-WATER-GUN GAME:")
choices=("snake","water","gun")
you=input("Enter your choice(snake/water/gun):").lower()
computer=random.choice(choices)

print(f"You choose {you}\nComputer chooses {computer} ")

if(computer==you):
    print("It's a Tie!")

else:
    if(computer=="snake" and you=="water"):
        print("You loose!")
    elif(computer=="snake" and you=="gun"):
        print("You win!")

    elif(computer=="gun" and you=="snake"):
        print("You loose!")
    elif(computer=="gun" and you=="water"):
        print("You win!")

    elif(computer=="water" and you=="snake"):
        print("You win!")
    elif(computer=="water" and you=="gun"):
        print("You loose!")

  




