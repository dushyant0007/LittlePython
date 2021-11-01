import pandas

data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Red"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

data_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel]
    }

pandas.DataFrame(data_dictionary).to_csv("squirrel_count.csv")