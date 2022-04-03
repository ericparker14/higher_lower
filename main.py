# TODO 1: print logo
from datetime import date
import art
import random
from game_data import data


print(art.logo)
SCORE = 0
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


#TODO 2 : pull 2 random choices from the game_data file and display their info

choice_a, choice_b = random.choices(data, k = 2)


def game():
    game_is_playing = False
    while game_is_playing:
        print(f"Compare A: {choice_a['name']} a {choice_a['description'].lower()}, from {choice_a['country']}.")
        print(art.vs)
        print(f"Against B: {choice_b['name']} a {choice_b['description'].lower()}, from {choice_b['country']}.")

        

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
        else:
            print("You are wrong. You lose")
            game_is_playing = False




play_game = input("Would you like to play the higher or lower game? Enter 'y' for yes and 'n' for no.")
if play_game == "y":
    game()



