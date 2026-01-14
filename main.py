import string
import secrets

def print_menu():
    """
     Prompts the user for input and returns the first character.
     """
    menu_user_input = input("""
    a. Generate Secure Password
    b. Calculate and Format a Percentage
    c. How many days from today until July 4, 2025?
    d. Use the Law of Cosines to calculate the leg of a triangle.
    e. Calculate the volume of a Right Circular Cylinder
    f. Exit program
    """).upper()

    print(f"you have entered:  {menu_user_input}")

    return menu_user_input


def validate_user_input(choice):
    """
    This uses the return value of print_menu function
    and validates the input to the selection choices available
    """
    valid_selection = False
    match choice:
        case "A":
            print("User has input a or A")
            valid_selection = True
        case "B":
            print("User has input b or B")
            valid_selection = True
        case "C":
            print("User has input c or C")
            valid_selection = True
        case "D":
            print("User has input d or D")
            valid_selection = True
        case "E":
            print("User has input e or E")
            valid_selection = True
        case "F":
            print("User has input f or F")
            valid_selection = True
        case _:
            print("Invalid option")
    return valid_selection


def get_yes_no(prompt):
    """
    Prompts the user for a yes/no response and returns True or False.
    """

    while True:
        choice = input(prompt).upper()

        match choice:
            case "Y":
                return True
            case "N":
                return False
            case _:
                print("Invalid selection. Please enter Y or N.")


def generate_secure_password():
    """
    Prompts the user for password length, validates input
    Prompts user to select password to include:
    uppercase,
    lowercase,
    numbers,
    special characters
    :return:
    """
    print("User has selected generate a secure password")
    include_num = False
    include_upper = False
    include_lower = False
    include_spec_char = False

    while True:
        length_input = input("Please enter a number for the length of the password")

        try:
            length = int(length_input)

            if length < 8:
                print("Password length must be at least 8 characters long.")
                continue

            if length > 20:
                print("Password length must be a maximum of 20 characters long")

            print(f"Password length set to: {length}")
            break

        except ValueError:
            print("Invalid input. Please enter integer value only")
    # 2) Get flags (reprompt until at least one is True)
    while True:
        include_num = get_yes_no("Include numbers? (Y/N): ")
        include_upper = get_yes_no("Include uppercase letters? (Y/N): ")
        include_lower = get_yes_no("Include lowercase letters? (Y/N): ")
        include_spec_char = get_yes_no("Include special characters? (Y/N): ")

        if include_num or include_upper or include_lower or include_spec_char:
            break

    # 3) Print selections (ternary operators for flag conditions)
    print(f"Include numbers: {'Yes' if include_num else 'No'}")
    print(f"Include uppercase letters: {'Yes' if include_upper else 'No'}")
    print(f"Include lowercase letters: {'Yes' if include_lower else 'No'}")
    print(f"Include special characters: {'Yes' if include_spec_char else 'No'}")

    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))

    print(f"{password}")


def calculate_formate_percentage():

    while True:
        try:
            a,b,c = map(int, input("Enter three numbers separated by white space \n").split())
            break
        except ValueError:
            print("Invalid input. Please enter exactly three integers.")

    percent = (a / b) * 100
    print(f"result: {percent:.2f}")


def main():
    """
    Main entry point
    Keeps prompting until the user enters a valid menu selection.
    """

    while True:
        user_input = print_menu()

        if not validate_user_input(user_input):
            continue

        match user_input:
            case "A":
                generate_secure_password()
            case "B":
                calculate_formate_percentage()
            case "C":
                print("Placeholder for option C")
            case "D":
                print("Placeholder for option D")
            case "E":
                print("Placeholder for option E")
            case "F":
                print("Exiting program...")
                return


if __name__ == "__main__":
    main()
