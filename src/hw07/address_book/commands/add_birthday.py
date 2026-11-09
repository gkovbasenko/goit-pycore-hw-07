from hw07.address_book.decorators import input_error
from hw07.address_book.book import AddressBook

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Name and birthday are required")
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_birthday(birthday)
    return "Birthday added."

