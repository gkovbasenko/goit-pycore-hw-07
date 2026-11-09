from hw07.address_book.decorators import input_error
from hw07.address_book.book import AddressBook
from hw07.address_book.record import Record

@input_error
def show_phone(args, book: AddressBook):
    if not args:
        raise ValueError("Name is required")
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return "; ".join(p.value for p in record.phones)
