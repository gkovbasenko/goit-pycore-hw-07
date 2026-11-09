from collections import UserDict
from datetime import datetime, date, timedelta
import calendar

class AddressBook(UserDict):

    @staticmethod
    def _birthday_in_year(birthday, year):
        """Feb 29 birthdays fall back to Feb 28 in non-leap years."""
        if birthday.month == 2 and birthday.day == 29 and not calendar.isleap(year):
            return birthday.replace(year=year, day=28)
        return birthday.replace(year=year)

    
    @staticmethod
    def _next_birthday(birthday, today):
        occurrence = AddressBook._birthday_in_year(birthday, today.year)
        if occurrence < today:
            # Re-derive from birthday: bumping occurrence would carry a Feb 28 fallback
            # into a leap year, or crash on a Feb 29 occurrence.
            occurrence = AddressBook._birthday_in_year(birthday, today.year + 1)
        return occurrence


    def get_upcoming_birthdays(self):
        """Return list of dicts with contact info for birthdays in the next 7 days."""
        users_to_congratulate = []
        today = date.today()
        
        for record in self.data.values():
            if not hasattr(record, 'birthday') or record.birthday is None:
                continue
            
            birthday = record.birthday.value
            next_birthday = self._next_birthday(birthday, today)
            
            number_of_days_until_birthday = (next_birthday - today).days
            if number_of_days_until_birthday <= 7:
                congratulation_date = next_birthday
                if congratulation_date.weekday() >= 5:
                    congratulation_date += timedelta(days=7 - congratulation_date.weekday())
                
                users_to_congratulate.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })
        
        return users_to_congratulate


    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError(f"Contact '{record.name.value}' already exists.")
        self.data[record.name.value] = record
        return record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        return self.data.pop(name, None)

    def __str__(self):
        if not self.data:
            return "Address book is empty."
        return "\n".join(str(record) for record in self.data.values())

    
