def snake_water_gun_game():
    """It has to be referred that above game depends on random module. The user
    will be asked to input between snake(s), gun(g) and water(w). Based on random
    module, computer will randomly choose its option. The game has maximum 10 chances"""

print(snake_water_gun_game.__doc__)
import random
print("\t\t\t\t\t _SNAKE-WATER-GUN-GAME_ \t\t\t\n")
from playsound import playsound
playsound('welcometosnake.mp3')



print("HELLO, WATER, SNAKE AND GUN GAME WELCOMES YOU\n")


list = ["s", "w", "g"]
chance = 10
num_of_chances = 0
computer_points = 0
human_points = 0


print("Kindly enter 's' for Snake and 'g' for Gun and 'w' for water\n")


while num_of_chances<chance:
    me = input("Choose between Snake(Type s), Water(Type w), Gun(type g) : \n ")
    # kindly enter s for snake, g for gun and s for snake
    com = random.choice(list)
    # if both enter same
    if me==com:
        print("tie, zero points to both\n")
        playsound('zeropoints.mp3')
    #     if me enter s
    elif me=="s" and com=="g":
        computer_points = computer_points+1
        print("Dammn, Computer earned one point\n")
        playsound('computerearnedpoint.mp3')
        print(f"Computer has earn 1 point. computer's points are {computer_points} and your points are {human_points}")
    elif me=="s" and com== "w":
        human_points = human_points+1
        print("Woah, you earn one point\n")
        playsound('youearnedpoint.mp3')
        print(f"your points are {human_points} and ccomputer's points are {computer_points}")
    #     if me enter w
    elif me=="w" and com=="g":
        human_points = human_points+1

        print("Woah, you won 1 point\n")
        playsound('youearnedpoint.mp3')
        print(f"Your points are {human_points} and computer's points are {computer_points}")
    elif me=="w" and com=="s":
        computer_points = computer_points+1
        print("Computer has earned one point\n")
        playsound('computerearnedpoint.mp3')
        print(f"Computer's points are {computer_points} and your points are {human_points}")
#         if me enter g
    elif me=="g" and com=="s":
        human_points= human_points+1
        print("You've won 1 point\n")
        playsound('youearnedpoint.mp3')
        print(f"your points are {human_points} and computer's points are {computer_points}")
    elif me=="g" and com=="w":
        computer_points= computer_points+1
        print("computer earned 1 point\n")
        playsound('computerearnedpoint.mp3')
        print(f"your points are {human_points} and computer's points are {computer_points}")
    else:
        print("Wrong Input. Caps lock off please and try again!!")

    num_of_chances = num_of_chances+1
    print(f"chances left {chance - num_of_chances}")

print("game over")
playsound('gameover.mp3')
# now
if computer_points == human_points:
    print("You both have same points. Therefore, It's a tie\n")
elif computer_points>human_points:
    print("Computer won and you loose")
    playsound('computerwon.mp3')

else:
    print("You won yayy and computer lost!!")
    playsound('youwon.mp3')

print(f"Your points are {human_points}\n")
print(f"Computer's points are {computer_points}\n")
print("THANKS FOR PLAYING...")
