# Day 14: Higher / Lower game
# say who has more followers on IG
# the winner stays and challenger is replaced
# your streak is tallied
# most likely this will involve dictionaries (it does)

# import game data
from day14_data import data  # data is a list of dictionaries
import asciiArt
import random

# user guess

# compare scores
# outputs winning choice or loss flag


def compare(accounts):
    """checks the highest choice and compares it to the user answer"""
    if accounts[0]['follower_count'] > accounts[1]['follower_count']:
        top_dog = "a"
    elif accounts[0]['follower_count'] < accounts[1]['follower_count']:
        top_dog = "b"
    else:
        top_dog = "wash"
    if top_dog == accounts[2]:
        print("You're right! Next round:")
        win = True
    elif top_dog == "wash":
        print("They have the same number of followers, but we'll give it to ya")
        win = True
    else:
        print("You lost!")
        win = False
    return win

# refresh contestants
# choose one from last time and make it option A


def refresh(option_a):
    """refreshes and prints the choices"""
    option_b = random.choice(data)
    while option_a == option_b:
        option_b = random.choice(data)
    print(f"Compare A: {option_a['name']}, a {option_a['description']} from {option_a['country']}")
    print(f"Against B: {option_b['name']}, a {option_b['description']} from {option_b['country']}")
    answer = input("Who has more followers, A or B? ").lower()
    return [option_a, option_b, answer]

# game start
# include play again prompt (and high score)
# include game loop
# include streak tally


def higher_lower():
    """main function for the game higher/lower"""
    print(asciiArt.homer)
    print("Homer: 'Welcome to Higher / Lower!'\n'You have to guess which IG account has the biggest following'")
    high_score = 0
    playing = True
    while playing:
        opt1 = random.choice(data)
        streak = 0
        winning = True
        while winning:
            print(f"\n    Streak: {streak}    High Score: {high_score}\n")
            options = refresh(opt1)
            winning = compare(options)
            opt1 = options[random.randint(0, 1)]
            if winning:
                streak += 1
                high_score = max(high_score, streak)
            else:
                streak = 0
        wanna_play = input("Do you want to go again? [y/n] ").lower()
        if wanna_play == "y":
            playing = True
        else:
            playing = False
            print("Goodbye!")


higher_lower()
# an_option = random.choice(data)
# print(an_option)
# a_name = an_option["name"]
# for i in range(10):
#     print(random.randint(0, 1))
# print(max(1, 2, 3, 4))

