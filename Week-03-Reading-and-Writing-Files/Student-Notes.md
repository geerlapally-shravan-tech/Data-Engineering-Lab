# Student Notes

# Experiment No. 3

# Reading and Writing Files

---

# Aim

To perform file handling operations using Python by reading and writing text files, CSV files, JSON files, and PostgreSQL databases.

---

# Learning Outcomes

After completing this experiment, students will be able to:

- Read and write text files.
- Perform CSV file operations.
- Perform JSON file operations.
- Connect Python with PostgreSQL.
- Store and retrieve records from a database.

---

# File Handling

## Definition

File handling is the process of creating, opening, reading, writing, updating, and closing files using a programming language.

Python provides built-in functions for file handling.

---

# Types of Files

## 1. Text File (.txt)

- Stores plain text
- Human readable
- Used for logs, reports, notes

Example

```
Name : Rahul
Age : 20
```

---

## 2. CSV File (.csv)

CSV stands for **Comma-Separated Values**.

Stores tabular data.

Example

```
ID,Name,Department
101,Rahul,CSE
102,Anitha,ECE
```

Applications

- Student records
- Sales reports
- Employee data

---

## 3. JSON File (.json)

JSON stands for **JavaScript Object Notation**.

Stores data in key-value format.

Example

```json
{
   "id":101,
   "name":"Rahul"
}
```

Applications

- REST APIs
- Web applications
- Configuration files

---

## 4. PostgreSQL Database

PostgreSQL is an open-source relational database.

Stores data in tables.

Applications

- Banking
- Hospital
- Inventory
- Education

---

# File Modes

| Mode | Purpose |
|------|---------|
| r | Read |
| w | Write |
| a | Append |
| x | Create New File |
| rb | Read Binary |
| wb | Write Binary |

---

# Important Functions

## File Handling

```python
open()

read()

readline()

readlines()

write()

close()
```

---

## CSV Module

```python
csv.reader()

csv.writer()

csv.DictReader()

csv.DictWriter()
```

---

## JSON Module

```python
json.load()

json.dump()

json.loads()

json.dumps()
```

---

## PostgreSQL

```python
connect()

cursor()

execute()

commit()

fetchall()

close()
```

---

# Important Python Modules

| Module | Purpose |
|---------|----------|
| csv | CSV File Handling |
| json | JSON File Handling |
| psycopg2 | PostgreSQL Connectivity |

---

# Advantages

## Text Files

- Simple
- Easy to read
- Lightweight

---

## CSV Files

- Tabular format
- Excel compatible
- Easy to process

---

## JSON Files

- Lightweight
- Human readable
- API compatible

---

## PostgreSQL

- Secure
- Reliable
- Fast
- ACID compliant

---

# Quick Revision

- File handling stores data permanently.
- Text files store plain text.
- CSV stores tabular data.
- JSON stores key-value pairs.
- PostgreSQL stores relational data.
- Python uses the csv module.
- Python uses the json module.
- psycopg2 connects Python with PostgreSQL.

---

# Frequently Asked Viva Questions

1. What is file handling?
2. What is a text file?
3. What is a CSV file?
4. What is JSON?
5. What is PostgreSQL?
6. What is the purpose of `open()`?
7. Explain file modes in Python.
8. What is the difference between CSV and JSON?
9. Why is `psycopg2` used?
10. What are the applications of file handling?

---

# University Examination Questions

## Short Questions

1. Define file handling.
2. What is CSV?
3. What is JSON?
4. Define PostgreSQL.
5. Explain file modes.

---

## Long Questions

1. Explain file handling in Python.
2. Explain reading and writing CSV files.
3. Explain JSON file handling.
4. Explain PostgreSQL database connectivity using Python.

---

# Summary

Python provides powerful support for file handling through built-in functions and libraries such as **csv** and **json**, while **psycopg2** enables communication with PostgreSQL databases. These concepts form the foundation of data ingestion and storage in Data Engineering.
