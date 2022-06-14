# Day 10: Functions with Outputs
# CHALLENGES & NOTES
# def function():
#    result = blah
#    return result
# result replaces the function call after running
# def format_name(first, last):
#     f_first = first.title()
#     f_last = last.title()
#     return f"{f_first} {f_last}"
#
#
# output = format_name("bRAndoN", "cONNEr")
# print(f_string)

# more than one return in same statement:
# def format_name(first, last):
#     if first == "" | last == "":
#         return "Did not provide valid inputs"
#     f_first = first.title()
#     f_last = last.title()
#     return f"{f_first} {f_last}"
#
#
# output = format_name("bRAndoN", "cONNEr")

# Leap year revisit:
# def is_leap(yr):
#     if (yr % 4 == 0) & (yr % 100 != 0 | ((yr % 100 == 0) & (yr % 400 == 0))):
#         return True
#     else:
#         return False
#
#
# def days_in_month(y, m):
#     """Find the days in the month for any
#     given month and year."""  # docstring
#     if m > 12 or m < 1:
#         return "Not a valid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(y):  # the return statement replaces the function in this if statement
#         month_days[1] = 29
#     return month_days[m-1]
#

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(f"There are {days} days in {month}, {year}")

# PROJECT: Calculator App
import asciiArt as aA
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(aA.homer)
    more = True
    num1 = float(input("What is your first number? "))
    while more:
        op = input("What is your operation (+, -, *, /)? ")
        num2 = float(input("What is your second number? "))
        funct = operations[op]
        answer = funct(num1, num2)
        print(f"{num1} {op} {num2} = {answer}")
        more_more = input("Keep going? [y/n/refresh] ")
        if more_more == "y":
            more = True
            num1 = answer
        elif more_more == "refresh":
            more = False
            calculator()
        else:
            more = False
            print("K fine. Have fun.")
calculator()
