from hw07.address_book.book import AddressBook


def show_birthdays(book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next 7 days."
    result = []
    for contact in upcoming:
        result.append(f"{contact['name']}: {contact['congratulation_date']}")
    return "\n".join(result)
