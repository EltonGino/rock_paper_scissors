import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

# Welcome msg
print("Welcome to the Rock, Paper and Scissors game")
# User choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You enter a wrong choice, you lost everything you rebel scum")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print(f"The Computer chose: ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif user_choice == computer_choice:
        print("It`s a Draw")

