import os
import random

player_options = ['rock', 'paper', 'scissors']
cpu_options = ['rock', 'paper', 'scissors']

player_score = [0]
cpu_score = [0]

def clear():
    os.system('cls||clear')

def title():
    print(f'+{'-' * 21}+')
    print('| Rock Paper Scissors |'.upper())  # rps
    print(f'+{'-' * 21}+')

def display_options():
    print("\nPlayer's turn:")
    print('1 - Rock')
    print('2 - Paper')
    print('3 - Scissors')
    print('-' * 12)

def get_number_of_rounds():
    while True:
        print('\nHow many rounds do you want to play?')
        print('-' * 35)
        rounds = input('>  ')

        if not rounds.isdigit():
            continue
        else:
            return int(rounds)
                  

def display_score(player, cpu):
    print(f'\nScore')
    print(f'Player {player} x {cpu} Computer')

def battle(player_score, cpu_score):
    rounds_left = get_number_of_rounds()
    while rounds_left > 0:
        clear()
        print(f'Rounds left: {rounds_left}')
        display_score(player_score, cpu_score)
        
        display_options()
        player_input = input('>  ')

        if not player_input.isdigit() or player_input not in ['1', '2', '3']:
            continue
        else:
            player_input = int(player_input)

        player_input -= 1

        player_choice = player_options[player_input]
        cpu_choice = random.choice(cpu_options)
        
        if player_choice == cpu_choice:
            print(f'\n(Player) {player_choice.upper()} x {cpu_choice.upper()} (Computer)')

        elif (player_choice == 'rock' and cpu_choice == 'scissors') or \
            (player_choice == 'scissors' and cpu_choice == 'paper') or \
            (player_choice == 'paper' and cpu_choice == 'rock'):
            
            print(f'\n(Player) {player_choice.upper()} x {cpu_choice.upper()} (Computer)')
            player_score[0] += 1
        
        else:
            print(f'\n(Player) {player_choice.upper()} x {cpu_choice.upper()} (Computer)')
            cpu_score[0] += 1
            
        rounds_left -= 1
        input('\nPress Enter to continue...')
        

def determine_winner(player_score, cpu_score):
    print(f'Final Score \n\nPlayer {player_score} x {cpu_score} Computer\n')

    if player_score == cpu_score:
        print("It's a Draw!")
    elif player_score > cpu_score:
        print('You Win!')
    else:
        print('You Lose!')


def play():
    while True:
        clear()
        title()
        
        battle(player_score, cpu_score)
       
        clear()
        determine_winner(player_score, cpu_score)
       
        quit()


play()