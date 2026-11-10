from hw07.address_book.decorators import input_error
from hw07.address_book.book import AddressBook

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book[name]
    record.add_birthday(birthday)
    return "Birthday added."

