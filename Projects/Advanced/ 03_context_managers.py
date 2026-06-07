# ============================================================
# Advanced Lesson 4: File Handling — JSON & CSV
# Instructor: Anaita Ahmadi | GEO Organization
# ============================================================

import json
import csv
import os

# ============================================================
# PART 1: JSON Files
# ============================================================

# --- Write JSON ---
students = [
    {"name": "Fatima", "age": 22, "grade": 90, "courses": ["Python", "AI"]},
    {"name": "Maryam", "age": 24, "grade": 85, "courses": ["Python", "Data Analysis"]},
    {"name": "Zahra",  "age": 21, "grade": 95, "courses": ["Python", "Machine Learning"]},
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)
print("JSON file written successfully.")

# --- Read JSON ---
with open("students.json", "r") as f:
    loaded = json.load(f)

print("\nLoaded students:")
for s in loaded:
    print(f"  {s['name']} | Age: {s['age']} | Grade: {s['grade']}")

# --- Update JSON ---
with open("students.json", "r") as f:
    data = json.load(f)

data.append({"name": "Sara", "age": 23, "grade": 88, "courses": ["Python"]})

with open("students.json", "w") as f:
    json.dump(data, f, indent=4)
print("\nNew student added to JSON.")

# --- JSON String (without file) ---
json_string = '{"city": "Kabul", "country": "Afghanistan"}'
parsed = json.loads(json_string)
print("\nParsed JSON string:", parsed["city"], ",", parsed["country"])

back_to_string = json.dumps(parsed, indent=2)
print("Back to string:\n", back_to_string)

# ============================================================
# PART 2: CSV Files
# ============================================================

# --- Write CSV ---
headers = ["Name", "Age", "Grade", "City"]
rows = [
    ["Fatima", 22, 90, "Kabul"],
    ["Maryam", 24, 85, "Herat"],
    ["Zahra",  21, 95, "Mazar"],
    ["Sara",   23, 88, "Kabul"],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
print("\nCSV file written successfully.")

# --- Read CSV ---
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    print("\nCSV content:")
    for row in reader:
        print(f"  {row['Name']} | Age: {row['Age']} | Grade: {row['Grade']}")

# --- Filter CSV data ---
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    top_students = [row for row in reader if int(row["Grade"]) >= 90]

print("\nTop students (grade >= 90):")
for s in top_students:
    print(f"  {s['Name']} — {s['Grade']}")

# --- Cleanup ---
os.remove("students.json")
os.remove("students.csv")
print("\nTemp files cleaned up.")

# ============================================================
# Practice Exercise:
# 1. Create a JSON file to store a simple contacts book
#    (name, phone, email) — add, read, and search contacts
# 2. Read a CSV of student grades and calculate the average
# 3. Convert a JSON file to a CSV file
# ============================================================
