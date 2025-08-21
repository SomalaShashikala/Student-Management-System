# Student Management System (Console, Python)

Simple console app for managing student records (CRUD) with optional JSON persistence.

## Requirements
- Python 3.8+

## Run
```bash
python student_mgmt.py
```

## Features
- Add, View, Search (by roll or name), Update, Delete
- Data saved to `data.json` on exit

## Project Structure
```
student-management/
├─ student_mgmt.py        # main program
├─ data.json              # created/updated automatically on exit
└─ README.md
```

## Tips
- Use clear, unique roll numbers to avoid duplicates.
- Press Enter on update prompts to keep old values.
- If `data.json` is deleted, the app starts with an empty list.