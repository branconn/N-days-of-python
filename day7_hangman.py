# Day 7: Hangman

# CHALLENGES & NOTES

# PROJECT: Hangman
import asciiArt
import random
wordBank = ["banana", "Barbara Streisand", "elephant", "hangman", "LaCroix", "Amelia", "Gone are the days",
            "What the fuck are you looking at"]
word = random.choice(wordBank)
lowerWord = word.lower()
playState = []
numLet = 0
numWrong = 0
guessBank = []
for i in range(len(word)):
    if word[i] == " ":
        playState += " "
    else:
        playState += "_"
        numLet += 1
print(f"Welcome to Hangman!\nWe've already got a word selected for you,"
      f" it's {numLet} letters long:")
print(" ".join(playState))
while (numWrong < 7) & ("_" in playState):
    guess = input("What is your letter guess? ").lower()
    if guess in guessBank:
        guess = input(f"You already guessed {guess}, choose another: ")
    if guess in lowerWord:
        i = 0
        while i < len(lowerWord):
            if guess in lowerWord[i:len(lowerWord)]:
                i = lowerWord[i:len(lowerWord)].index(guess) + i
                playState[i] = word[i]
                i += 1
            else:
                i = len(lowerWord)
        print("you got it!")
    else:
        numWrong += 1
        print("Ooo not even close!")
        guessBank += guess
    if numWrong > 0:
        print(asciiArt.hangmanPics[numWrong - 1])
    print(" ".join(playState))
    print("Wrong guesses: " + " ".join(guessBank))
    print(f"Lives: {7 - numWrong}/7")
if numWrong >= 7:
    print("You lost!!!")
else:
    print("You did it, champ!")







