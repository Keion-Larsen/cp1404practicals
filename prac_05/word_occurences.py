string = input("Please enter a string of text: ")
string_dict = {}
for word in string:
    space = word.split(" ")
    string_dict.update(space, len(space))

print(string_dict)