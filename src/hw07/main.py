from hw07.address_book.data import parse_input
from hw07.address_book.commands.add_contact import add_contact
from hw07.address_book.commands.change_contact import change_contact
from hw07.address_book.commands.show_all import show_all
from hw07.address_book.commands.show_phone import show_phone
from hw07.address_book.commands.add_birthday import add_birthday
from hw07.address_book.commands.show_birthday import show_birthday
from hw07.address_book.commands.show_birthdays import show_birthdays

from hw07.address_book.book import AddressBook

COMMANDS = [
    ("hello", "get a greeting from the bot"),
    ("add <name> [phone]", "add a new contact or add phone to existing"),
    ("change <name> <old_phone> <new_phone>", "change phone number for a contact"),
    ("phone <name>", "show phone numbers for a contact"),
    ("all", "show all contacts in address book"),
    ("add-birthday <name> <DD.MM.YYYY>", "add a birthday for a contact"),
    ("show-birthday <name>", "show birthday for a contact"),
    ("birthdays", "show upcoming birthdays in the next 7 days"),
    ("close | exit", "quit the program"),
]


def print_commands():
    width = max(len(usage) for usage, _ in COMMANDS)
    print("\nAvailable commands:")
    for usage, description in COMMANDS:
        print(f"  {usage.ljust(width)}  - {description}")
    print()


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    print_commands()
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if not command:
            print("Please enter a command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(show_birthdays(book))

        else:
            print("Invalid command.")
