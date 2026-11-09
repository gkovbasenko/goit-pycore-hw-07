from hw07.address_book.decorators import input_error
from hw07.address_book.book import AddressBook


@input_error
def show_birthday(args, book: AddressBook):
    if not args:
        raise ValueError("Name is required")
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    if record.birthday is None:
        return f"{name} has no birthday set."
    return f"{name}'s birthday: {record.birthday.value}"
