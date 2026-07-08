# Program-02

# Reading and Writing CSV Files Using Python

---

## Experiment No.

02

---

## Aim

To read data from and write data to a CSV (Comma-Separated Values) file using Python.

---

## Objective

The objective of this experiment is to understand how Python uses the built-in **csv** module to create, write, and read CSV files. Students will learn how CSV files are used to store tabular data and why they are widely used in Data Engineering for data exchange and processing.

---

## Prerequisites

- Python 3.x installed
- Visual Studio Code or any Python IDE
- Basic knowledge of Python programming
- Basic understanding of rows and columns

---

## Theory

CSV (Comma-Separated Values) is one of the most popular file formats used to store tabular data. Each line in a CSV file represents one record, and each value is separated by a comma.

Python provides the built-in **csv** module that allows developers to read and write CSV files efficiently.

CSV files are widely used because they are:

- Lightweight
- Easy to create
- Human-readable
- Supported by Microsoft Excel, Google Sheets, and database systems
- Commonly used in ETL (Extract, Transform, Load) processes

---

## Software Required

- Python 3.x
- Visual Studio Code
- CSV Module (Built-in)

---

## Algorithm

1. Import the **csv** module.
2. Open a CSV file in write mode.
3. Create a CSV writer object.
4. Write the column headers.
5. Write multiple student records.
6. Close the file automatically.
7. Open the same CSV file in read mode.
8. Create a CSV reader object.
9. Read each row from the CSV file.
10. Display all records.
11. Stop.

---

## Program

The Python source code is available in **csv_file.py**.

---

## Input

No user input is required.

The program automatically creates student records.

---

## Expected Output

```text
CSV file created successfully.

Student Records
-------------------------
['ID', 'Name', 'Department']
['101', 'Rahul', 'CSE']
['102', 'Anitha', 'ECE']
['103', 'Kiran', 'MECH']
```

---

## Output File

The program creates the following file automatically:

**students.csv**

Contents of **students.csv**

```csv
ID,Name,Department
101,Rahul,CSE
102,Anitha,ECE
103,Kiran,MECH
```

---

## Applications

- Student Information Systems
- Employee Management Systems
- Banking Applications
- Sales Reports
- Inventory Management
- Data Migration
- ETL Pipelines
- Machine Learning Datasets

---

## Advantages

- Simple file format
- Human readable
- Easy to exchange data
- Supported by almost every programming language
- Compatible with Microsoft Excel
- Suitable for structured data

---

## Limitations

- Cannot store complex data structures
- No built-in security
- Does not support relationships like databases
- Large CSV files may be slow to process

---

## Result

The program was executed successfully. A CSV file was created, student records were written into the file, and the same records were read and displayed successfully.

---

## Viva Questions

1. What is a CSV file?
2. What does CSV stand for?
3. Which Python module is used for CSV file handling?
4. What is the purpose of `csv.writer()`?
5. What is the purpose of `csv.reader()`?
6. Why is `newline=""` used while writing CSV files?
7. What is the difference between a text file and a CSV file?
8. Why are CSV files widely used in Data Engineering?
9. Can Microsoft Excel open CSV files?
10. Give two real-world applications of CSV files.

---

## References

1. Python Documentation – csv Module
2. Python Standard Library Documentation
3. PostgreSQL Documentation
4. Data Engineering Best Practices
