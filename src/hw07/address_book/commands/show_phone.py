from hw07.address_book.decorators import input_error
from hw07.address_book.book import AddressBook

@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book[name]
    return "; ".join(p.value for p in record.phones)
