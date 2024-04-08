import random

""" first we make a function that will generate a random choice between rock, paper or scissors """


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


""" second we make a function that will get input form player """


def get_player_choice():
    user_input = input("\nenter rock, paper or scissors (or enter 'q' to Exit): ").lower()
    while user_input not in ['rock', 'paper', 'scissors', 'q']:
        user_input = input("\n invalid input please enter rock, paper, or scissors (or enter 'q' to Exit): ").lower()
    return user_input


""" third we make a function that will defien the winner of the game """


def game_roles(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "\n Game tai Tray agin"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "\n YOU WIN Game "
    else:
        return "\n YOU LOSE Game "

def play():
    while True:
        user_choice = get_player_choice()
        if user_choice == 'q':
            break
        computer_choice = get_computer_choice()
        print(f'\n your choice is {user_choice} and computer choice is {computer_choice}')
        result = game_roles(user_choice, computer_choice)
        print(result)


play()
