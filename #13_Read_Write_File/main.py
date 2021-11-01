#  mode = 'r' or 'w' or 'a' append
#  'r' is the default mode
file = open("my_file.txt", mode='r')
contents = file.read()
print(contents)
print(file)
file.close()

#  previous text text get deleted and  "New text" gat written
with open("my_file.txt", mode='w') as file:
    file.write("New text ")

#  Now we appending to are previous text
with open("my_file.txt", mode='a') as file:
    file.write("Now Open With append ('a') ")
