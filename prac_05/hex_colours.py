HEXADECIMAL_COLOURS = {"AliceBlue": '#f0f8ff', 'beige': 'f5f5dc', 'black': '000000', 'blue': '#0000ff',
                       'brown': '#a52a2a', 'chocolate': '#d2691e', 'coral': '#ff7f50',
                       'cyan1': '#00ffff', 'DarkGreen': '#006400', 'firebrick': '#b22222'}

colour_name = input("Please enter a colour name: ")
while colour_name != "":
    if colour_name in HEXADECIMAL_COLOURS:
        print("{} has code: {}".format(colour_name, HEXADECIMAL_COLOURS[colour_name]))
    else:
        print("Invalid colour")
    colour_name = input("Please enter a colour name: ")