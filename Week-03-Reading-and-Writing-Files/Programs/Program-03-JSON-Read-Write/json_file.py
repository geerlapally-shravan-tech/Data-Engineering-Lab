"""
Program-03
Reading and Writing JSON Files Using Python
"""

import json

# ---------------------------------------
# Step 1: Create Employee Dictionary
# ---------------------------------------

employee = {
    "ID": 101,
    "Name": "Rahul",
    "Department": "Computer Science and Engineering",
    "Salary": 50000,
    "City": "Hyderabad"
}

# ---------------------------------------
# Step 2: Write Dictionary to JSON File
# ---------------------------------------

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

print("JSON file created successfully.\n")

# ---------------------------------------
# Step 3: Read JSON File
# ---------------------------------------

with open("employee.json", "r") as file:
    data = json.load(file)

print("Employee Details")
print("-" * 30)

for key, value in data.items():
    print(f"{key:<12}: {value}")
