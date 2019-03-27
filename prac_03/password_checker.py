
def main():

    entered_pass = get_password()

    entered_pass = check_length(entered_pass)

    asterisks_print(entered_pass)


def asterisks_print(entered_pass):
    print("*" * len(entered_pass))


def check_length(entered_pass):
    while len(entered_pass) < 2:
        entered_pass = str(input("Enter Valid Password: "))
    return entered_pass


def get_password():
    return str(input("Entered Password: "))


main()
