
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# example
for (indexOfTheRow,row) in data.iterrows():
    print(indexOfTheRow)
    print(row)
    #This .iterrows() return a tupple of two values the first one is for the index and the second one for row

print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
