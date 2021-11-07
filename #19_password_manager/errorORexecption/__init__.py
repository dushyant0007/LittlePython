try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["asd"])
except FileNotFoundError:
    file = open("a_file.txt", "w")  # This going to create a new file
    file.write("writing in file")
except KeyError as error_message:
    # error_message going to hold the value of error
    print(f" The key {error_message} dose note exist.")
else:
    # if try block is goose successful
    # then this will be executed
    content = file.read()
    print(content)
    print("This in the else block")
finally:
    # This going to run no matter what happens
    print("We are in finally block")
    file.close()
    # raise FileNotFoundError("The file is not found I made up")
    # Adding massage is completely optional
    # you also can do <- raise FileNotFoundError ->




