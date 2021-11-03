#  List comprehension
from random import randint

number = [1, 2, 3]
new_numbers = [n + 1 for n in number]
print(new_numbers)

name = "Dushyant"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

nums = [2, 7, 6, 4, 10, 9, 15, 35]
new_nums = [num for num in nums if int(num) % 2 == 0]
print(new_nums)

#  -------------------------+++++++++++++++++++++----------------------+++++++++++++++++++++++----------

#  Dictionary comprehension
# <Type One> => new_dict = {new_key : new_value for item in list}
#  <Type Tow> => new_dict = {new_key : new_value for (key,value) in dict.items() }

cities = [" New York", "London", "San Francisco", "Las vegas", "Washington", "Boston,Boston", "Paris"]

# evey key should be unique otherwise it would not register
new_cities = {randint(0, 20): city for city in cities}
print(new_cities)

new_cities_point = {city: randint(0, 10) for city in cities}
print(new_cities_point)

passed_score = {city: score for (city, score) in new_cities_point.items() if score >= 5}
print(f"Passed Score = {passed_score}")

# Making a dict in which key = world value is the len of world
sen = " Hello my name is dushyant jakhar i live in london"
# for word in sen.split():
#     print(f"List of word from a sen => {word}")

result = {word: len(word) for word in sen.split()}
print(result)

#  ------------------_________________-----------------__________---------

student_dict = {
    "student": ["S1", "S2", "S3", "S4"],
    "score": [56, 76, 98, 64]
}

print("Student data frame")
for (key, value) in student_dict.items():
    print( f"key : {key}" , f"value : {value}")


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#  Loop through a data frame
print("Looping in dataframe wity .items() ")
for (key, value) in student_data_frame.items():
    print(f" key : {key}  Value : {value} ")

print("Looping in dataframe wity .iterrows() ")
for (index, row) in student_data_frame.iterrows():
    print(f" Index : {index}  Row : {row} ")
    print(f"row.score : {row.score}")






