# Student Management System (Console) with optional JSON persistence
# Run: python student_mgmt.py

import json
import os
from typing import List, Dict, Optional

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

# Global in-memory store
students: List[Dict[str, str]] = []


# ---------- Persistence ----------
def load_data() -> List[Dict[str, str]]:
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                return data
        except Exception:
            # If file is corrupted or unreadable, start fresh
            pass
    return []


def save_data() -> None:
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(students, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving data: {e}")


# ---------- Helpers ----------
def pause() -> None:
    input("\nPress Enter to continue...")


def find_by_roll(roll: str) -> Optional[Dict[str, str]]:
    for s in students:
        if s.get("roll_no") == roll:
            return s
    return None


def non_empty(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("This field is required. Please try again.")


# ---------- CRUD ----------
def add_student() -> None:
    print("\n=== Add Student ===")
    roll = non_empty("Roll no: ")
    if find_by_roll(roll):
        print("❌ Roll number already exists. Not added.")
        return
    name = non_empty("Name: ")
    grade = non_empty("Grade: ")
    age = input("Age (optional): ").strip()
    students.append({"roll_no": roll, "name": name, "grade": grade, "age": age})
    print("✅ Student added.")


def view_students() -> None:
    print("\n=== View Students ===")
    if not students:
        print("No records.")
        return
    # Header
    print(f"{'Roll':<8}{'Name':<20}{'Grade':<8}{'Age':<6}")
    print("-" * 42)
    # Rows
    for s in students:
        print(f"{s.get('roll_no',''):<8}{s.get('name',''):<20}{s.get('grade',''):<8}{s.get('age',''):<6}")


def search_student() -> None:
    print("\n=== Search Student ===")
    mode = input("Search by (1) Roll No or (2) Name: ").strip()
    if mode == "1":
        roll = input("Enter roll no: ").strip()
        s = find_by_roll(roll)
        if s:
            print("Found:")
            print(s)
        else:
            print("Not found.")
    elif mode == "2":
        name = input("Enter (partial) name: ").strip().lower()
        results = [s for s in students if name in s.get('name','').lower()]
        if results:
            for s in results:
                print(s)
        else:
            print("No matches.")
    else:
        print("Invalid choice.")


def update_student() -> None:
    print("\n=== Update Student ===")
    roll = input("Roll to update: ").strip()
    s = find_by_roll(roll)
    if not s:
        print("Not found.")
        return
    new_name = input(f"Name [{s.get('name','')}]: ").strip()
    if new_name:
        s['name'] = new_name
    new_grade = input(f"Grade [{s.get('grade','')}]: ").strip()
    if new_grade:
        s['grade'] = new_grade
    new_age = input(f"Age [{s.get('age','')}]: ").strip()
    if new_age:
        s['age'] = new_age
    print("✅ Updated.")


def delete_student() -> None:
    print("\n=== Delete Student ===")
    roll = input("Roll to delete: ").strip()
    s = find_by_roll(roll)
    if not s:
        print("Not found.")
        return
    confirm = input(f"Are you sure you want to delete {s.get('name')} (Roll {s.get('roll_no')})? (y/N): ").strip().lower()
    if confirm == "y":
        students.remove(s)
        print("✅ Deleted.")
    else:
        print("Cancelled.")


# ---------- Main Menu ----------
def main() -> None:
    global students
    students = load_data()
    while True:
        print("\nStudent Management System")
        print("1) Add  2) View  3) Search  4) Update  5) Delete  6) Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_student()
            pause()
        elif choice == "2":
            view_students()
            pause()
        elif choice == "3":
            search_student()
            pause()
        elif choice == "4":
            update_student()
            pause()
        elif choice == "5":
            delete_student()
            pause()
        elif choice == "6":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()