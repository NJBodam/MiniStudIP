
# Student Management System
A Python implementation of a simple student registry system using Object-Oriented Programming (OOP). It defines classes for managing individual students and a dedicated class for handling a sorted list of all registered students.

## Features* **OOP Design:
** Utilizes three classes: `Student`, `Student2BA` (inherits from `Student`), and `StudentList`.
* **Unique Student Numbers:** Automatically assigns a unique sequential number to each new student using a class variable.
* **Data Structure:** The `StudentList` maintains students in a sequence, sorted by student number.
* **Efficient Searching:** Implements **binary search** (`search()`) for fast retrieval of students by their unique number.
* **Sequential Search:** Implements **sequential search** (`searchName()`) for finding students by name.
* **Specialized Students:** The `Student2BA` class handles students with both a major and a minor subject, overriding the `__str__` method for correct output.
* **File Import:** Can load student data from a tab-separated text file using `importStudents()`.
* **Registration Management:** Functions for registering new students (`register()`) and deregistering existing students (`deRegister()`).

## Project Structure
The code defines three main classes:

###1. `Student`The base class for all students.

* **Attributes:** `firstname`, `lastname`, `major`, `num` (student number), `term`.
* **Methods:** `getName()`, `getNo()`, `inc_term()`, `setMajor()`, etc.

###2. `Student2BA`Extends `Student` for students pursuing two subjects (a major and a minor).

* **Inherits:** All attributes and methods from `Student`.
* **Adds:** `minor` attribute.
* **Overrides:** `__init__`, `__str__`, and modifies `setMajor`/`setMinor` to prevent major and minor from being the same.

###3. `StudentList`Manages the collection of `Student` objects.

* **Attribute:** `studList` (a list of student objects, sorted by number).
* **Key Methods:** `register()`, `findStudentNo()` (uses binary search), `findStudentName()` (uses sequential search), `deRegister()`, and `importStudents()`.

## Key Algorithms
###Binary Search for Student NumberThe `search(self, key)` method within `StudentList` uses binary search to quickly find a student based on their unique, sequential student number (`key`).

This is highly efficient because the `studList` is guaranteed to be sorted by the student number.

###Sequential Search for NameThe `searchName(self, name)` method uses a sequential (linear) search. Since the list is only guaranteed to be sorted by number, not by name, this simple iteration is necessary to match the first and last name string.

## Example Usage
The main execution block demonstrates how to use the classes:

1. Initializes an empty `StudentList` object (`uniOL`).
2. Imports student data from a file (`UniOlStudents.txt`).
3. Retrieves a student by index (`getStudent(13)`).
4. Deregisters that student by their student number (`deRegister()`).
5. Searches for a student by their number (`findStudentNo(13)`).

```python
# Create the student list container
uniOL = StudentList()

# Load students from a file
uniOL.importStudents("UniOlStudents.txt")

# Find and print a student by number (efficient binary search)
stud_num13 = uniOL.findStudentNo(13)
print(stud_num13)

# Remove a student by their number
uniOL.deRegister(stud_num13.getNo())

```
