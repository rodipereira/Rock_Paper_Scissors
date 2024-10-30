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

game_image = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(game_image[player_choice])

robot_game = random.randint(0,2)
print(game_image[robot_game])

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You lose!")
elif player_choice == 0 and robot_game == 2:
    print("You win!")
elif robot_game == 0 and player_choice == 2:
    print("You lose!")
elif robot_game > player_choice:
    print("You lose!")
elif player_choice > robot_game:
    print("You win!")
elif robot_game == player_choice:
    print("It's a draw!")