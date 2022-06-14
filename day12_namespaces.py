# Day 12: Namespaces: global & local variables
# CHALLENGES & NOTES
enemies = 1

def increase_enemies():
    enemies = 2
    print(enemies)

# increase_enemies()
# print(enemies)

# local scope exists within functions
# global scope is accessible everywhere
# need to be mindful of where variables are assigned
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

# there is no block scope in Python
# block scope: only accessible in indent
# scope is only fenced by functions, not indented blocks
# game_level = 3
# enemies = ["skeleton", "zombie", "alien"]
# if game_level < 5:
#     new_enemy = enemies[0]
# print(new_enemy)

enemies = 1

def crease_enemies():
    # enemies = 2  # don't call local and global the same thing
    # global enemies  # you don't want to do this very often - complicated and possibly buggy
    # read and use, don't modify
    return enemies + 1  # this is preferred
    print(enemies)

# crease_enemies()
# print(enemies)

# global constants should be all uppercase
# these are good for items that shouldn't be modified

# drink_potion()
# print(player_health)

# PROJECT: Guess the number
# 1 to 100
# easy (10 attempts) or hard (5) difficulty
# says too high or too low

# tasks to solve:
# choose a number
# for loop with length determined by difficulty selection
# determine high or low
# if match, stop loop
import random
import asciiArt
def guessing_game():
    print(asciiArt.homer)
    print("'Welcome to the guess-a-number game!' - Homer")
    wins = 0
    losses = 0
    again = True
    while again:
        guesses = 10
        match = False
        hard = input("Play on easy or type 'hard' for fewer guesses: ") == "hard"
        if hard:
            guesses = 5
        hidden_num = random.randint(1, 100)
        print("'I've chosen a number between 1 and 100' - still Homer")
        while not match and guesses > 0:
            attempt = int(input("What is your guess? "))
            if (type(attempt) != int) or (attempt > 100) or (attempt < 1):
                print("You need to input an integer between 1 and 100")
                guesses -= 1
            elif attempt < hidden_num:
                print("Too low!")
                guesses -= 1
            elif attempt > hidden_num:
                print("Too high")
                guesses -= 1
            elif attempt == hidden_num:
                match = True
                guesses -= 1
            print(f"{guesses} guesses left")
        if match:
            print(f"You guessed it! The number was {hidden_num}!")
            wins += 1
        elif guesses < 1:
            print(f"You ran out of guesses! The number was {hidden_num}")
            losses += 1
        again = input(f"Wins: {wins}  Losses: {losses}\nPlay again? [y/n]: ") == "y"

guessing_game()





