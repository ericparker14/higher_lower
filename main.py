# TODO 1: print logo
import art
import random
from game_data import data
from os import system, name


def clear():
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('clear')


def compare():
    """Compares the two choices and evaluates players answer"""
    if choice_a['follower_count'] > choice_b['follower_count']:
        return 1 
    elif choice_a['follower_count'] < choice_b['follower_count']:
        return 0

def choice(player_choice):
    if player_choice.lower() == "a":
        return 1 
    if player_choice.lower() == "b":
        return 0


print(art.logo)
# get the first two choices out of the way
choice_a, choice_b = random.choices(data, k = 2)


def game():
    clear()
    SCORE = 0
    is_game_over = False
    while  not is_game_over:
        global choice_a, choice_b
        # to give the user info about choices
        print(f"Compare A: {choice_a['name']} a {choice_a['description'].lower()}, from {choice_a['country']}.")
        print(art.vs)
        print(f"Against B: {choice_b['name']} a {choice_b['description'].lower()}, from {choice_b['country']}.")

        # storing inputs to variables to use later
        answer = compare()
        player_answer = input("Who has more followers? Type 'A' or 'B':\n")
        player_choice = choice(player_choice=player_answer)

        # to compare return values of both functions and see their relationship
        if player_choice == answer:
            print("You are correct")
            SCORE += 1
            print(f"Your score is {SCORE}!")
            choice_a = choice_b
            choice_b = random.choice(data)
            # to fix duplicate bug
            if choice_b == choice_a:
                choice_b = random.choice(data)
        else:
            print("You are wrong. You lose")
            is_game_over = True


play_game = input("Would you like to play the higher or lower game? Enter 'y' for yes and 'n' for no.")
if play_game == "y":
    game()



