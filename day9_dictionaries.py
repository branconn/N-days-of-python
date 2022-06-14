# DAY 9: Dictionaries, Nesting
# CHALLENGES & NOTES
# dictionaries tag and group together related pieces of information
# comprised of a key and a value

first_dic = {
    "key": "value", "mike": "dick", "dog": "bounty hunter", "age": 28,
    "something_new": "new_value",
}  # this is the preferred format

# print(first_dic["dog"])
# print(first_dic)

# loop through a dict:
# for key in first_dic:
#     print(f"{key} : {first_dic[key]}")

# grading program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for student in student_scores:
    if student_scores[student] < 70:
        student_grades[student] = "Failure"
    elif student_scores[student] < 80:
        student_grades[student] = "Average -"
    elif student_scores[student] < 90:
        student_grades[student] = "Average +"
    else:
        student_grades[student] = "Actually decent"
    # print(f"{student}: {student_grades[student]}")

# Nesting: you guessed it
# test = {
#     "key": ["list", "of", "things"],
#     "key2": {"value_key": "value_value"}
# }
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
#     "Germany": {"cities_avoided": ["berlin", "Hamburg", "Stuttgart"], "germans_scoffed_at": 43},
# }

# Nesting Challenge
travel_log = [
    {
      "country": "France",
      "visits": 12,
      "cities": ["Paris", "Lille", "Dijon"]
    },
    {
      "country": "Germany",
      "visits": 5,
      "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# travel_log += 5


# def add_new_country(state, tours, cities):
#     new_entry = {
#         "country": state,
#         "visits": tours,
#         "cities": cities,
#     }
#     travel_log.append(new_entry)
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# PROJECT: Silent Auction
import os
import asciiArt
others = True
bids = {}
print(asciiArt.homer)
print('"Welcome to the silent auction" - Homer')
while others:
    name = input("What is your name? ")
    bid = float(input("What is your bid? "))
    more_ppl = input("Any participants after you? [y/n]: ").lower()
    if more_ppl != "y":
        others = False
    bids[name] = bid
    os.system('cls' if os.name == 'nt' else 'clear')
winning_bid = 0
winner = ""
for name in bids:
    if bids[name] > winning_bid:
        winning_bid = bids[name]
        winner = name
    elif bids[name] == winning_bid:
        winner += f" & {name}"
print("The results are in...")
print(f"The winner is {winner} with a bid of {winning_bid}")
