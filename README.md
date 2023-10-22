# goitneo-python-hw-2-MCS3

## subtask 1

All user input errors should be handled using the ```input_error``` decorator. This decorator is responsible for returning messages like ```"Enter user name"```, ```"Give me name and phone please"``` etc. to the user. The ```input_error``` decorator should handle exceptions that occur in the handler functions (```KeyError```, ```ValueError```, ```IndexError```) and return the appropriate response to the user.

## subtask 2

Develop a system for managing the address book.

### **ENTITIES**

* **Field**: Base class for record fields.
* **Name**: A class for storing the name of a contact. Mandatory field.
* **Phone**: A class for storing a phone number. Has format validation (10 digits).
* **Record**: A class for storing information about a contact, including name and phone list.
* **AddressBook**: A class for storing and managing records.

### **FUNCTIONALITY**

1 ```Address Book```:

* Adding records.
* Search records by name.
* &&Deleting records by name.

2 ```Records```:

* Adding phones.
* Deleting phones.
* Editing phones.
* Phone search.

### **Evaluation criteria**

**AddressBook class**:

* Implemented the ``add_record`` method, which adds a record to ``self.data``.
* Implemented the ``find method``, which finds a record by name.
* Implemented the ``delete`` method, which deletes a record by name.

**Record class**:

* Storage of the ``Name`` object in a separate attribute has been implemented.
* Storage of the list of ``Phone`` objects in a separate attribute has been implemented.
* Implemented methods for adding - ``add_phone``, for deleting - ``remove_phone``, for editing - ``edit_phone``, finding Phone objects - ``find_phone``.
**Phone class**:
* Phone number validation has been implemented (must be 10 digits).

## TO CHECK

### for sub_task 1

``` bash
python ./bot_assistant/bot.py
```

### for sub_task 2

``` bash
python ./bot_assistant/book.py
```
