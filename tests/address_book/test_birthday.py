import unittest
from datetime import date
from hw07.address_book import Birthday


class TestBirthday(unittest.TestCase):
    def test_accepts_valid_date_format(self):
        birthday = Birthday("15.03.1990")
        self.assertEqual(birthday.value, date(1990, 3, 15))

    def test_stores_as_date_object(self):
        birthday = Birthday("01.01.2000")
        self.assertIsInstance(birthday.value, date)

    def test_invalid_format_raises_error(self):
        with self.assertRaises(ValueError) as context:
            Birthday("1990-03-15")
        self.assertIn("DD.MM.YYYY", str(context.exception))

    def test_invalid_date_raises_error(self):
        with self.assertRaises(ValueError):
            Birthday("32.13.2000")  # Invalid month and day

    def test_empty_string_raises_error(self):
        with self.assertRaises(ValueError):
            Birthday("")

    def test_non_string_raises_error(self):
        with self.assertRaises((ValueError, TypeError)):
            Birthday(None)

    def test_feb_29_in_leap_year(self):
        birthday = Birthday("29.02.2000")
        self.assertEqual(birthday.value, date(2000, 2, 29))

    def test_invalid_feb_29_in_non_leap_year(self):
        with self.assertRaises(ValueError):
            Birthday("29.02.2001")

    def test_error_message_format(self):
        with self.assertRaises(ValueError) as context:
            Birthday("invalid")
        self.assertEqual(str(context.exception), "Invalid date format. Use DD.MM.YYYY")


class TestBirthdayEquality(unittest.TestCase):
    def test_equal_birthdays(self):
        b1 = Birthday("15.03.1990")
        b2 = Birthday("15.03.1990")
        self.assertEqual(b1, b2)

    def test_different_birthdays(self):
        b1 = Birthday("15.03.1990")
        b2 = Birthday("16.03.1990")
        self.assertNotEqual(b1, b2)

    def test_is_hashable(self):
        b1 = Birthday("15.03.1990")
        b2 = Birthday("15.03.1990")
        self.assertEqual(len({b1, b2}), 1)


if __name__ == "__main__":
    unittest.main()
