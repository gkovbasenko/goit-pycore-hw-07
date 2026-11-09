
from hw07.address_book.fields import Name, Phone, Field, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.birthday = None
        self.phones = []

    
    def add_birthday(self, birthday):
        new_birthday = Birthday(birthday)
        self.birthday = new_birthday
        return new_birthday        

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if self.find_phone(phone) is not None:
            raise ValueError(f"Phone {phone} already exists for {self.name}.")
        self.phones.append(new_phone)
        return new_phone

    def remove_phone(self, phone):
        found = self.find_phone(phone)
        if found is None:
            raise ValueError(f"Phone {phone} not found for {self.name}.")
        self.phones.remove(found)
        return found

    def edit_phone(self, old_phone, new_phone):
        replacement = Phone(new_phone)
        found = self.find_phone(old_phone)
        if found is None:
            raise ValueError(f"Phone {old_phone} not found for {self.name}.")
        # replace in place so the phone order is preserved
        self.phones[self.phones.index(found)] = replacement
        return replacement

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)

    def __str__(self):
        birthday_str = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}"

    def __repr__(self):
        birthday_repr = f", birthday={self.birthday.value!r}" if self.birthday else ""
        return f"Record({self.name.value!r}, phones={[p.value for p in self.phones]!r}{birthday_repr})"
