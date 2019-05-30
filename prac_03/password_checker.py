
def main():

    password = get_password()

    password = check_length(password)

    print_asterisks(password)


def print_asterisks(entered_pass):
    print("*" * len(entered_pass))


def check_length(entered_pass):
    while len(entered_pass) < 2:
        entered_pass = str(input("Enter Valid Password: "))
    return entered_pass


def get_password():
    return str(input("Entered Password: "))


main()
