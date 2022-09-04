import random


def win():
  print ('You win!')

def lose():
  print ('You lose!')

while True:
    moves = ['rock', 'paper', 'scissors']
    player_choice = input('What do you pick? (rock, paper, scissors)')
    # player_choice.strip()
    computer_choice = random.choice(moves)

    if player_choice==computer_choice:
        print ('Draw!')
    elif player_choice=='rock' and computer_choice == 'scissors':
       win()
    elif player_choice== 'paper' and computer_choice == 'scissors':
      lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
      win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
      lose()
    elif player_choice== 'paper' and computer_choice == 'rock':
       win()
    elif player_choice=='rock'and computer_choice=='paper':
      lose()
    again = input('Do you want to play again? (y or n)')
    if again == 'n':
        break