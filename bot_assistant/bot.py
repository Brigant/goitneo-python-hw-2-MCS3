"""
Module providing a function of bot assistan.
This bot can store the contact in RAM using command "add [name] [phone]". 
There is a possibilyty to change existen user using command "change [name] [phone]". 
You can show a number of specified user by the command "phone [name]" and you can see all 
contacs using command "all".
"""


def input_error(func):
    """The function handle the user inputs error"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Caught the ValueError exception: {e}"
        except KeyError as e:
            return f"Caught the KeyError exception: {e}"

    return inner


def is_validate_phone(phone) -> bool:
    """Phone validation function"""
    try:
        int(phone)
    except ValueError:
        return False

    return True


def parse_input(user_input):
    """The function parse user input and return command and arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


@input_error
def add_contact(args, contacts):
    """
    The function add new contact to the contacts list.
    Use 'add <name> <phone>' command.
    """

    if len(args) != 2:
        raise ValueError("Give me name and phone please")
    name, phone = args
    if not is_validate_phone(phone):
        raise ValueError("Invalid phone format")
    contacts[name] = phone

    return "Contact added."


@input_error
def change_contact(args, contacts):
    """
    The function change existen contact.
    Use 'change <name> <phormat>'.
    """

    if len(args) != 2:
        raise ValueError("Give me name and phone please")
    name, phone = args
    if not is_validate_phone(phone):
        raise ValueError("Invalid phone format")
    if name not in contacts:
        raise KeyError("Specified name not found")
    contacts[name] = phone

    return "Contact updated."


@input_error
def show_phone(args, contacts: dict):
    """
    The function show phone number of the contact.
    Use phone command.
    """

    if len(args) == 1:
        name = args[0]
    else:
        raise ValueError("Give me name please")

    if name not in contacts:
        raise KeyError("Specified name not found")

    return contacts[name]


@input_error
def show_all(contacts):
    """
    The function show all contacts.
    Use 'all' command.
    """

    if len(contacts) < 1:
        return "Your contact list is empty"

    result = [f"{name} {phone}\n" for name, phone in contacts.items()]
    str_result = ''.join(result)

    return str_result


def main():
    """The main function"""
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if len(user_input)>0:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            if command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(add_contact(args, contacts))

            elif command == "change":
                print(change_contact(args, contacts))

            elif command == "phone":
                print(show_phone(args, contacts))

            elif command == "all":
                print(show_all(contacts))

            else:
                print("Invalid command.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
