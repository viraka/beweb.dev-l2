import random

def roll_dice():
    return random.randint(1, 6)

num_rolls = int(input("How many times do you want to roll the dice? "))

for i in range(num_rolls):
    print(f"Roll {i + 1}: {roll_dice()}")
