# Day 26: List and Dictionary Comprehension
import pandas as pd
# NOTES
# List comprehension is unique to Python
# shortens code and makes it more concise
#
# you create a list from a new list
# rather than looping through to reassign items to a new list you would:
# new_list = [new_item for item in list]
# !
nums = [1, 2, 3]

# Old Method:
new_list = []
for n in nums:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension:
new_list = [n + 1 for n in nums]

# Splits up a sequence (string, tuple, list) into a list
name = "Brandon"
new_list = [letter for letter in name]
# print(new_list)

# Manipulating a range
new_range = [step * 2 for step in range(1,5)]

# Conditional List Comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Edith", "Freddie"]
short_names = [n for n in names if len(n) < 5]
cap_names = [n.upper() for n in names if len(n) >= 5]

# List "Challenge" 1: Squared
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]

# List Challenge 2: Evens
result = [num for num in numbers if num % 2 == 0]

# List Challenge 3:
# my solution:
list_1 = pd.read_csv("file1.txt", header=None)
list_1.columns = ["a"]
real_list_1 = list_1["a"].to_list()
list_2 = pd.read_csv("file2.txt", header=None)
list_2.columns = ["a"]
real_list_2 = list_2["a"].to_list()
result = [item for item in real_list_1 if item in real_list_2]
print(result)
# their solution:
with open("file1.txt") as file1:
    file_1_data = file1.readlines()
with open("file2.txt") as file2:
    file_2_data = file2.readlines()
result = [int(num) for num in file_1_data if num in file_2_data]
# their solution was better

# DICTIONARY COMPREHENSION
# another file


