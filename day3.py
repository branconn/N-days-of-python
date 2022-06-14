# NOTES
# = is assignment, == is parity comparison
# != >= <= ==
# modulo (%) computes remainder 7 % 2 = 1

# CHALLENGES
# for x in range(len("five")):
#     if x == 3:
#         print(f"yes {x}")
#     else:
#         print(f"no {x}")
# print(range(len("five")))

# y = input("Give me an integer: ")
# try:
#     x = int(y)
# except ValueError:
#     print("This is not an integer")
# else:
#     if (int(x) % 2) == 0:
#         print("This is an even number.")
#     else:
#         print("This is an odd number.")

# y = float(input("What is your height? "))
# age = int(input("What is your age? "))
# if y < 120:
#     print("Sorry shorty")
# else:
#     if age > 18:
#         print("$17, please")
#     elif age == 12 | age > 13:
#         print("Whatever")

# y = float(input("What is your height in m? "))
# m = float(input("What is your mass in kg? "))
# bmi = round(m / y**2)
# if bmi < 18.5:
#     print(f"{bmi} Skinny bitch")
# elif bmi < 25:
#     print(f"{bmi} Normy")
# elif bmi < 30:
#     print(f"{bmi} Chonk")
# elif bmi < 35:
#     print(f"{bmi} Heckin' chonker")
# else:
#     print(f"{bmi} OH LAWD HE COMIN'")

# year = int(input("Enter a year to see if it's a leap year: "))
# if (year % 4 == 0) & (year % 100 != 0 | ((year % 100 == 0) & (year % 400 == 0))):
#     print("Yep. That's a leap year")
# else:
#     print("Nope")

# you = input("What is your full name? ").lower()
# them = input("What is your crush's full name? ").lower()
# docked = you + them
# tens = "true"
# tensScore = 0
# ones = "love"
# onesScore = 0
# for i in range(len(tens)):
#     tensScore += docked.count(tens[i])
# for i in range(len(ones)):
#     onesScore += docked.count(ones[i])
# print(f"You are a {tensScore * 10 + onesScore}% match!")

# PROJECT: TREASURE ISLAND
# No.
