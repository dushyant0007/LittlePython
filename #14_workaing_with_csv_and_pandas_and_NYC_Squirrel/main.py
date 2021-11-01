# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     strip_data = []
#     for value in data:
#         strip_data.append(value.strip())
#
#     print(strip_data)


# The batter way to work with csv
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


#  Working with pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

#  Avg temp in column of temperature
avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# or
# print(data.temp.mean())
# or
# print(data["temp"].mean())
# print(data.temp.max())


#  Get data in column
# print(data["condition"])

# Gent data in row
# print(data[data.day == "Monday"])

# Finding row having max temperature
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday.condition)

#  Create a data frame from scratch

data_dictionary = {
    "students": ["Amy", "James", "Aryan"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dictionary)
# or
data.to_csv("new_data.csv")
