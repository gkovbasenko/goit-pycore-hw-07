from hw07.address_book.decorators import input_error
from hw07.address_book.book import AddressBook
from hw07.address_book.record import Record

@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Name and phone are required")
    name, phone, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        record.add_phone(phone)
        return "Contact added."
    record.add_phone(phone)
    return "Contact updated."