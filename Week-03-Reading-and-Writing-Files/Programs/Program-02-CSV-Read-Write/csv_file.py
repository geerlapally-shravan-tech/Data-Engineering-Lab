"""
Program-02
Reading and Writing CSV Files using Python
"""

import csv

# -----------------------------
# Step 1: Write data to CSV file
# -----------------------------

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow(["ID", "Name", "Department"])

    # Student Records
    writer.writerow([101, "Rahul", "CSE"])
    writer.writerow([102, "Anitha", "ECE"])
    writer.writerow([103, "Kiran", "MECH"])
    writer.writerow([104, "Ravi", "EEE"])

print("CSV file created successfully.\n")

# -----------------------------
# Step 2: Read data from CSV
# -----------------------------

print("Student Records")
print("-" * 40)

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
