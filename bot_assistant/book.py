"""
Address book
"""

from collections import UserDict


class Field:
    """Class representing a field"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class representing a Name field of the record"""


class Phone(Field):
    """Class representing a Phone field of the record"""

    def __init__(self, value):
        if self.is_valid(value):
            super().__init__(value)
        else:
            raise ValueError("Wrong format of phone number")

    def __eq__(self, another):
        return self.value == another.value

    @staticmethod
    def is_valid(value: str):
        """Validation Phone method"""
        return len(value) == 10 and value.isdigit()


class Record:
    """Class representing a record of address book"""

    def __init__(self, new_name):
        self.name = Name(new_name)
        self.phones: list(Phone) = []

    def find_phone(self,  phone: str):
        """Return phone list and return it."""
        found_phones = [p.value for p in filter(lambda p: phone == p.value, self.phones)]
        if len(found_phones) > 0:
            return found_phones[0]
        return None

    def add_phone(self, str_phone):
        """Add phone to phone list"""
        new_phone = Phone(str_phone)
        if new_phone in self.phones:
            raise ValueError(f"the number: '{str_phone}' is already exist")
        self.phones.append(new_phone)

    def remove_phone(self, str_phone):
        """Remove phone from phone list"""
        phone = Phone(str_phone)
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        """Edit phone in the phone list."""
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Class representing an address book"""

    def add_record(self, new_record: Record):
        """AddressBook method that allows to add record"""
        self.data[new_record.name.value] = new_record

    def find(self, search_name: str):
        """Finds the record by name"""
        return self.data.get(search_name)

    def delete(self, search_name: str):
        """Removes the record by name from the book """
        if search_name in self.data:
            del self.data[search_name]


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    # Спроба добавити існуючий номер до запису
    try:
        john_record.add_phone("5555555555")
    except ValueError as e:
        print(f"Get exception: {e}")

    # Пошук не існуючого номера
    print(john_record.add_phone("5555555552"))
