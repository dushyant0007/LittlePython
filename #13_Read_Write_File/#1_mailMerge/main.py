PLACEHOLDER = "[name]"
with open("name_list.txt", mode='r') as names_file:
    # readLines function is going to convert
    # every value of line to a list element
    #  extra lines in names_file count a empty element in list <DON'T do this Mistake>
    names = names_file.readlines()
#     name is a list

with open("starting_latter.txt", mode='r') as latter_file:
    latter_contents = latter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = latter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"output_letters/Invitation_Of_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)
