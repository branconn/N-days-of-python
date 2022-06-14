# PROJECT
print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
numPpl = int(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
due = total*(1+tip/100)/numPpl
print(f"Each person should pay: ${round(due, 2)}")


# NOTES
# string: str() a string of characters, uses double quotes
# integer: int() positive and negative whole numbers
# float: floating point numbers
# boolean: True or False
# division always outputs a float
# ** is an exponent
# // is floor (round down to integer)
# /= += *= -= etc to affect a variable directly
# f-string: e.g. f"your score is {score}"

# CHALLENGES
# x = input("Input your two-digit number: ")
# x0 = x[0]
# x1 = x[1]
# y = int(x0) + int(x1)
# print("Your number smashes to " + str(y))

# mass = input("How fat are you?")
# height = input("How giraffe are you?")
# BMI = round(float(mass) / float(height)**2)
# print("You are this chubby:")
# print(BMI)

# your life in weeks
# ageLeft = 90- int(input("What is your current age? "))
# mons = ageLeft*12
# wks = ageLeft*52
# days = ageLeft*365
# print(f"You have {days} days, {wks} weeks, {mons} months left")


