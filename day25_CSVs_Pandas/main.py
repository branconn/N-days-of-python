# DAY 26
# We'll be working with Pandas, a really popular package for working with data
# The project wil be a name-the-states map game
# Comma Separate Values!

# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

# Using native CSV package
# import csv
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)  # data is an object of the csv_reader class
#     temperatures = []
#     # print(data[0]) # data is not subscriptable,
#     for row in data:  # but is iterable
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         # print(row)
#     print(temperatures)

# Using Pandas package
import pandas
import pandas as pd
import numpy as np
data = pd.read_csv("weather_data.csv")
# print(type(data))  # data is a pandas DataFrame object
# print(type(data["temp"]))  # data row is a series object

# Converting to List
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list)/len(temp_list)

# Using Panda methods for a Series
# avg_temp = data["temp"].mean()
# max_temp = data["temp"].max()
# # print(max_temp)
#
# # Getting Data in Columns
# # data.temp == data["temp"]
#
# # Getting Data in Rows
xing_qi_yi = data[data.day == "Monday"]
monday_f = int(xing_qi_yi.temp) * 1.8 + 32
print(monday_f)
print(xing_qi_yi)
hot_boy = data[data.temp == data.temp.max()].day
print(type(hot_boy.values))
#
# # Create a DataFrame
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

# Create a CSV that counts out the populations of fur colors
# sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color_list = sq_data["Primary Fur Color"]

# fur_dict = {}
# for fur in color_list:
#     if fur == "nan":
#         pass
#     elif fur not in fur_dict:
#         fur_dict[str(fur)] = [1]
#     else:
#         fur_dict[str(fur)][0] += 1

# grey_squirrels_count = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
# grey_squirrels_count = len(color_list[color_list == "Gray"])  # filtering by its own values
# black_squirrels_count = len(sq_data[sq_data["Primary Fur Color"] == "Black"])
# cinnamon_squirrels_count = len(sq_data[sq_data["Primary Fur Color"] == "Cinammon"])
# # print(grey_squirrels_count)
#
# fur_dict = {
#     "Fur Color": ["Grey", "Cinammon", "Black"],
#     "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
# }
# # print(fur_dict)
# fur_data = pd.DataFrame(fur_dict)
# fur_data.to_csv("squirrel_data.csv")



