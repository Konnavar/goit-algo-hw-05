import re
from typing import Callable

def input_error(func):
    def wrapper(*args, **kwargs): # Функція-обгортка приймає будь-яку кількість позиційних аргументів і іменованих аргументів
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "No contact found with this name."
            elif isinstance(e, ValueError):
                return "Invalid input. Please provide a valid input."
            elif isinstance(e, IndexError):
                return "Invalid number of arguments. Please provide the correct number of arguments."
            else:
                return "An error occurred while processing your request."
    return wrapper

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    args = [arg.strip() for arg in args]
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        raise IndexError

@input_error
def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Phone number updated for {name}."
        else:
            raise KeyError(name)
    else:
        raise IndexError

@input_error
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return f"The phone number for {name} is {contacts[name]}."
        else:
            raise KeyError(name)
    else:
        raise IndexError

@input_error
def show_all_contacts(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
