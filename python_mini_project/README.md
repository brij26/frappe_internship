# Student Marks Tracker (CLI)

A simple command-line application built in Python to manage student records. The application allows users to add, remove, update, search, and view student marks while persisting the data in a JSON file.

## Features

- Add a new student with marks.
- Remove an existing student.
- Update a student's marks.
- Search for a student by name.
- View all students and their marks.
- Calculate the average marks of all students.
- Save student data to a JSON file.
- Automatically load existing student data when the application starts.

## Concepts Demonstrated

This project was built to practice core Python concepts, including:

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Properties (`@property` and `@property.setter`)
- Custom Decorators
- Exception Handling
- File Handling
- JSON Serialization and Deserialization
- Type Hints
- Command Line Interface (CLI)

## Project Structure

```text
python_mini_project/
│
├── admin.py          # Business logic for managing student records
├── logger.py         # Custom logging decorator
├── main.py           # Command-line interface
├── data.json         # Stores student data
└── README.md
```

## Requirements

- Python 3.10 or later (Python 3.8+ should also work)

No external libraries are required. The project uses only Python's standard library.

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd python_mini_project
```

3. Run the application.

```bash
python main.py
```

## Menu Options

```text
===== Student Marks Tracker =====

1. Add Student
2. Remove Student
3. Update Marks
4. Search Student
5. View Students
6. Average Marks
7. Save Data
8. Exit
```

## Example

```text
===== Student Marks Tracker =====

1. Add Student
2. Remove Student
3. Update Marks
4. Search Student
5. View Students
6. Average Marks
7. Save Data
8. Exit

Enter choice: 1

Name of the student: Brij
Marks: 95

Student added successfully.
```

## Data Storage

Student information is stored in `data.json` using the following format:

```json
{
  "Brij": 95,
  "Rahul": 88,
  "Amit": 91
}
```

## Error Handling

The application handles common errors such as:

- Invalid menu selections.
- Negative marks.
- Student not found.
- Empty student records.
- Invalid JSON file or missing data file.

## Learning Outcomes

Through this project, I practiced:

- Designing classes using object-oriented programming.
- Separating business logic from the user interface.
- Creating reusable decorators.
- Using properties for controlled access to class attributes.
- Reading from and writing to JSON files.
- Implementing exception handling for robust applications.
- Building an interactive command-line application.

## Future Improvements

- Store additional student details such as ID and grade.
- Display highest and lowest marks.
- Sort students by marks or name.
- Delete all student records.
- Export reports to CSV.
- Add unit tests using `pytest`.
- Replace the CLI with a graphical user interface or web application.

## Author

**Brij Patel**

Python Mini Project – Student Marks Tracker
