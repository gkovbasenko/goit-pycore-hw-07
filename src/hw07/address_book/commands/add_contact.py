from hw07.address_book.decorators import input_error
from hw07.address_book.book import AddressBook
from hw07.address_book.record import Record

@input_error
def add_contact(args, book: AddressBook):
    name, *rest = args
    phone = rest[0] if rest else None
    
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message