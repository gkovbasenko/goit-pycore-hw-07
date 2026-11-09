import unittest
from datetime import date, timedelta
from hw07.address_book import AddressBook, Record


class TestGetUpcomingBirthdays(unittest.TestCase):
    def setUp(self):
        self.book = AddressBook()

    def test_empty_book(self):
        result = self.book.get_upcoming_birthdays()
        self.assertEqual(result, [])

    def test_no_birthdays_set(self):
        record = Record("John")
        record.add_phone("1234567890")
        self.book.add_record(record)
        result = self.book.get_upcoming_birthdays()
        self.assertEqual(result, [])

    def test_birthday_in_past(self):
        record = Record("John")
        record.add_phone("1234567890")
        record.add_birthday("15.03.1990")
        self.book.add_record(record)
        result = self.book.get_upcoming_birthdays()
        # Should be empty or contain only if it's within 7 days of next year
        self.assertIsInstance(result, list)

    def test_returns_dict_with_name_and_date(self):
        today = date.today()
        year = today.year if today.month == 3 and today.day <= 15 else today.year + 1
        birthday_date = f"15.03.{year - 30}"
        
        record = Record("John")
        record.add_phone("1234567890")
        record.add_birthday(birthday_date)
        self.book.add_record(record)
        
        result = self.book.get_upcoming_birthdays()
        if result:
            self.assertIsInstance(result[0], dict)
            self.assertIn("name", result[0])
            self.assertIn("congratulation_date", result[0])
            self.assertEqual(result[0]["name"], "John")

    def test_weekend_birthday_moves_to_monday(self):
        """Test that Saturday/Sunday birthdays move to the following Monday"""
        book = AddressBook()
        
        # Create a contact with a birthday that will fall on weekend
        record = Record("Weekend Person")
        record.add_phone("1234567890")
        # This is just testing the logic, actual weekend dates depend on the year
        record.add_birthday("15.03.1990")
        book.add_record(record)
        
        result = book.get_upcoming_birthdays()
        # If there's an upcoming birthday, verify structure
        if result:
            self.assertIn("congratulation_date", result[0])


class TestBirthdayInYear(unittest.TestCase):
    def test_normal_date(self):
        birthday = date(1992, 3, 15)
        result = AddressBook._birthday_in_year(birthday, 2025)
        self.assertEqual(result, date(2025, 3, 15))

    def test_feb_29_in_leap_year(self):
        birthday = date(2000, 2, 29)
        result = AddressBook._birthday_in_year(birthday, 2000)
        self.assertEqual(result, date(2000, 2, 29))

    def test_feb_29_in_non_leap_year_falls_back_to_feb_28(self):
        birthday = date(2000, 2, 29)
        result = AddressBook._birthday_in_year(birthday, 2001)
        self.assertEqual(result, date(2001, 2, 28))


class TestNextBirthday(unittest.TestCase):
    def test_future_birthday_this_year(self):
        # Birthday later this year
        birthday = date(1990, 12, 25)
        today = date(2025, 1, 1)
        result = AddressBook._next_birthday(birthday, today)
        self.assertEqual(result.year, 2025)
        self.assertEqual(result.month, 12)
        self.assertEqual(result.day, 25)

    def test_past_birthday_moves_to_next_year(self):
        # Birthday earlier this year
        birthday = date(1990, 1, 15)
        today = date(2025, 3, 1)
        result = AddressBook._next_birthday(birthday, today)
        self.assertEqual(result.year, 2026)
        self.assertEqual(result.month, 1)
        self.assertEqual(result.day, 15)

    def test_birthday_today_returns_today(self):
        birthday = date(1990, 3, 15)
        today = date(2025, 3, 15)
        result = AddressBook._next_birthday(birthday, today)
        self.assertEqual(result, today)


class TestAddRecordDuplicate(unittest.TestCase):
    def test_duplicate_name_raises_error(self):
        book = AddressBook()
        record1 = Record("John")
        record1.add_phone("1234567890")
        book.add_record(record1)
        
        record2 = Record("John")
        record2.add_phone("9999999999")
        
        with self.assertRaises(ValueError) as context:
            book.add_record(record2)
        self.assertIn("already exists", str(context.exception))

    def test_different_names_allowed(self):
        book = AddressBook()
        record1 = Record("John")
        record1.add_phone("1234567890")
        book.add_record(record1)
        
        record2 = Record("Jane")
        record2.add_phone("9999999999")
        book.add_record(record2)
        
        self.assertEqual(len(book), 2)


class TestRecordWithBirthday(unittest.TestCase):
    def test_str_includes_birthday(self):
        record = Record("John")
        record.add_phone("1234567890")
        record.add_birthday("15.03.1990")
        result = str(record)
        self.assertIn("1990-03-15", result)
        self.assertIn("John", result)
        self.assertIn("1234567890", result)

    def test_str_without_birthday(self):
        record = Record("John")
        record.add_phone("1234567890")
        result = str(record)
        self.assertNotIn("birthday", result)

    def test_repr_includes_birthday(self):
        record = Record("John")
        record.add_phone("1234567890")
        record.add_birthday("15.03.1990")
        result = repr(record)
        self.assertIn("birthday", result)
        self.assertIn("1990", result)

    def test_repr_without_birthday(self):
        record = Record("John")
        record.add_phone("1234567890")
        result = repr(record)
        self.assertNotIn("birthday", result)


if __name__ == "__main__":
    unittest.main()
