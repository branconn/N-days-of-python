# NOTES:Randomization and python lists
# askPython to check for modules
# split complex code into modules: this allows specialization and organization
# creating a module is easy: create a new file, import it
#
#############################
# CHALLENGES
import random

# rand_float = random.random()
# print(rand_float * 5)
# love_Score = random.randint(1, 100)

# Heads or Tails
# h = 0
# t = 0
# for i in range(0, 4999):
#     # rec = random.random()
#     rec = random.randint(0, 1)
#     # if rec < 0.5:
#     if rec == 1:
#         # print("You should choose Heads")
#         h += 1
#     else:
#         # print("You should choose Tails")
#         t += 1
# print(f"H: {h}\nT: {t}")

# Lists: data structures
# syntax matters: square brackets, delimited by commas
# states = ["Delaware", "Pennsylvania", "Georgia"]
# print(states[0])
# # why start counting at 0? because you're not counting, you're stating the offset from the start of the list
# print(states[-1])  # index from back with negative
# states[-1] = "Doghead"
# states.append("Crazyland")
# states.insert(2, "Middle")
# print(states)

# Bill Roulette
# namesString = input("Who is participating in bill roulette?\n")
# names = namesString.split(", ")
# chosenOneName = random.choice(names)
# chosenOne = random.randint(0, len(names)-1)
# print(f"{names[chosenOne]} is the chosen one")

# Nested Lists
# fruits = ["apple", "banana"]
# vegetables = ["tomato", "zucchini"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

# Treasure Map
# row0 = ["O", "0", "0"]
# row1 = ["O", "0", "0"]
# row2 = ["O", "0", "0"]
# map = [row0, row1, row2]
# rc = input("Where do you want your treasure? (row+column):\n")
# map[int(rc[0])-1][int(rc[1])-1] = "X"
# print(f"{row0}\n{row1}\n{row2}")


#########################################
# PROJECT: Rock, Paper, Scissors
import asciiArt
yourChoice = int(input("Choose 0 (rock), 1 (paper) or 2 (scissors): "))
compChoice = random.randint(0, 2)
art = [asciiArt.homer, asciiArt.bart, asciiArt.lisa]
choice = ["rock", "paper", "scissors"]
if (yourChoice < 0) | (yourChoice > 2):
    print("Invalid choice. You Lose")
else:
    print(f"You choose {choice[yourChoice]}:")
    print(art[yourChoice])
    print(f"Your opponent chooses {choice[compChoice]}:")
    print(art[compChoice])
    if choice[yourChoice-1] == choice[compChoice]:
        print("You win!")
    elif choice[yourChoice] == choice[compChoice]:
        print("Tie!")
    else:
        print("You lose!")
