from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"{type(self).__name__}({self.value!r})"

    def __eq__(self, other):
        if isinstance(other, Field):
            return type(self) is type(other) and self.value == other.value
        return NotImplemented

    def __hash__(self):
        return hash((type(self), self.value))


class Name(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name is required and must be a non-empty string.")
        super().__init__(value.strip())


class Phone(Field):
    LENGTH = 10

    def __init__(self, value):
        if not isinstance(value, str) or len(value) != self.LENGTH or not value.isdigit():
            raise ValueError(f"Phone must be exactly {self.LENGTH} digits, got {value!r}.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            date_obj = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date_obj)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")