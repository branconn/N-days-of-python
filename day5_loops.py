# CHALLENGES & NOTES: loops
# fruits = ["apple", "peach", "pear"]
# for fruit in range(0, len(fruits)):
#     # if I loop by doing fruit in fruits the changes I make to fruit do not affect fruits
#     fruits[fruit] = (fruits[fruit] + " pie")
#     print(fruit)
# print(fruits)

#  Averaging without using sum or len
# heights = input("Input a list of heights").split()
# print(heights)
# i = 0
# total2 = 0
# for height in heights:
#     heights[i] = int(heights[i])
#     total2 += heights[i]
#     i += 1
# print(heights)
# print(total2)
# print(round(total2 / i))

# High score
# sevenYears = [78, 65, 89, 55, 91, 64, 89]
# topBoi = 0
# for score in sevenYears:
#     if score > topBoi:
#         topBoi = score
# print(f"Top score is {topBoi}")

# Range function: Adding 1 to 100
# g_unit = 0
# for number in range(1, 101):
#     g_unit += number
# print(g_unit)

# Range(): sum 1 to 100 even only
# g_unit = 0
# g_unit2 = 0
# for number in range(2, 101, 2):
#     g_unit += number
# print(g_unit)
# for number in range(1, 101):
#     if number % 2 == 0:
#         g_unit2 += number
# print(g_unit2)

# FizzBuzz Exercise
# for i in range(1, 101):
#     if (i % 3 == 0) & (i % 5 == 0):
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

# PROJECT: password generator
import random
numL = int(input("How many letters would you like in your password? "))
numS = int(input("How many symbols? "))
numN = int(input("How many numbers? "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

unscrambled = []
scrambled = ""
for i in range(0, numL):
    unscrambled.append(random.choice(letters))  # += works for lists too
for i in range(0, numS):
    unscrambled.append(random.choice(symbols))
for i in range(0, numN):
    unscrambled.append(random.choice(numbers))
print(unscrambled)
for i in range(0, len(unscrambled)):
    cherry = random.choice(unscrambled)
    unscrambled.remove(cherry)
    scrambled += cherry
print(scrambled)

# after considering it, the below code is not a good scramble since the selection is not weighted. ...
# This is clear when one type has many more values than the rest"
# scrambled = ""
# charTypes = ["let", "sym", "num"]
# for i in range(0, (numL + numS + numN)):
#     pick = random.choice(charTypes)
#     if pick == "let":
#         scrambled += random.choice(letters)
#         numL += -1
#         if numL == 0:
#             charTypes.remove("let")
#     elif pick == "sym":
#         scrambled += random.choice(symbols)
#         numS += -1
#         if numS == 0:
#             charTypes.remove("sym")
#     elif pick == "num":
#         scrambled += random.choice(numbers)
#         numN += -1
#         if numN == 0:
#             charTypes.remove("num")
