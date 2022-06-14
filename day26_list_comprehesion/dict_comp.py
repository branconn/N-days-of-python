# Day 26 cont.:
# DICTIONARY COMPREHENSION
import random as r
import pandas as pd
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items())}
#   loops through all keys and values in a dict
#   ".items()" part is crucial
# new_dict = {new_key:new_value for (key, value) in dict.items()) if test}
#   added conditional

# assign random scores to students
names = ["Alex", "Beth", "Caroline", "Dave", "Edith", "Freddie"]
grades = {name: r.randint(0, 100) for name in names}

# who passed?
passed_students = {name: grade for (name, grade) in grades.items() if grade > 59}
print(passed_students)

# Dictionary Comprehension Challenge 1: count letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow"
result = {name: len(name) for name in sentence.split()}

# Dictionary Comprehension Challenge 2: convert a dict of F temps to C
weather_c = {
    "M": 12,
    "T": 14,
    "W": 15,
    "Th": 14
}
weather_f = {day: (temp * 1.8 + 32) for (day, temp) in weather_c.items()}

# Iterate over Pandas DataFrame ########
grades_other = {
    "student": ["Brandon", "Wesley", "Lily"],
    "score": [56, 79, 12]
}
student_df = pd.DataFrame(grades_other)

# Loop through dictionaries:
for (key, value) in grades_other.items():
    pass

# Loop through DataFrame:
for (key, value) in student_df.items():
    pass  # gives data in each of the columns

# Loop through rows of DataFrame
for (index, row) in student_df.iterrows():
    pass  # row.student or row.score (column headers)





