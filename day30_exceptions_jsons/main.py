# Day 30: Handling Errors, Exceptions, and Using JSON Files

"""
NOTES
with open("text.txt") as file:
    file.read()

^^^ this errors out (404) if there's no file text.txt

a_dictionary = {key: value}
value = a_dictionary["non_existent_key"]

^^^ a key error

other popular ones: Index Errors and Type Errors


We need to plan for exceptions and manage them

try:
    something that might cause an exception
except:
    do this if there is an exception
else:
    do this if there are no exceptions
finally:
    do this no matter what happens
raise:
    raise our own exception
    why use raise? if a situation has valid code but provides an incorrect result

JSON files
    first implementing this retroactively in the password manager (day29)
    JavaScriptObjectNotation
    Similar to dictionaries
    Nested Key: Value pairs

    There's an in-built json library where we can
    json.dump() write
    json.load() read
    json.update() and update

"""
# example:
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["dog-boy"])
# except FileNotFoundError:
#     # best practice is to never have bare except clauses
#     file = open("a_file.txt", "w")
#     file.write("Something")
#     print("new file created")
# except KeyError as error_message:
#     # ?! as error_message has inconsistent behavior
#     print(f"The key {error_message} not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File closed")
#     raise TypeError
#     not often used

# Raising Exceptions
# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
# bmi = weight / height ** 2
# print(bmi)

# Error Handling Exercise 1 (index error):
fruits = ["apple", "pear", "orange"]


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError as error_m:
#         # ?! as error_message has inconsistent behavior
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(2)

# Error Handling Exercise 2 (key error):

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

# total_likes = 0
# key_errors = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError as message:
#         key_errors += 1
#         print(message)
#
#
# print(f"Likes: {total_likes}")
# print(f"Key Errors: {key_errors}")