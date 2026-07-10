# Contact Management System

A simple command-line contact management system built in Python. It lets you add, search, delete, and display contacts, with data stored persistently in a CSV file.

## Features

- **Add Contact** — Store a contact's name, number, and email (email is optional).
- **Delete Contact** — View all contacts and remove one by selecting its number.
- **Search Contact** — Search by name, number, or email.
- **Display Contacts** — View all saved contacts in a clean, formatted table.

## Requirements

- Python 3
- `tabulate` library

Install the dependency with:

```bash
pip install tabulate
```

## Setup

Before running the program for the first time, create a `contacts.csv` file in the same directory with the following header row:

```
NAME,NUMBER,EMAIL
```

This ensures new contacts are appended correctly and existing features (search/display) work as expected.

## Usage

Run the program with:

```bash
python contacts.py
```

You'll be shown a menu of options:

- `Add` — Add a new contact
- `Delete` — Delete an existing contact
- `Search` — Search for a contact by name, number, or email
- `Display` — Display all contacts in a table
- `Quit` — Exit the program

## File Structure

```
├── contacts.py       # Main program
├── contacts.csv       # Contact data storage (created by user)
└── README.md
```

## Author
Ritabanta Ghosh
