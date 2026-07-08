# Theory

# Experiment No. 3

# Reading and Writing Files

---

# 1. Introduction

Data is one of the most valuable resources in modern organizations. Every application stores and retrieves data from different sources such as text files, CSV files, JSON files, and databases. Before data can be analyzed or processed, it must first be read from its source and, after processing, written back to a file or database.

Python provides powerful built-in libraries that make file handling simple and efficient. These libraries enable Data Engineers to work with structured and semi-structured data, automate ETL (Extract, Transform, Load) processes, and build reliable data pipelines.

In this experiment, students will learn how to read and write data using different file formats and PostgreSQL databases.

---

# 2. Learning Objectives

After completing this experiment, students will be able to:

- Understand file handling in Python.
- Read and write text files.
- Read and write CSV files.
- Read and write JSON files.
- Connect Python with PostgreSQL.
- Store and retrieve records from a database.

---

# 3. What is File Handling?

File handling is the process of creating, opening, reading, writing, updating, and closing files using a programming language.

Python provides built-in functions for file handling that allow programmers to store data permanently instead of keeping it only in memory.

---

# 4. Types of Files

Python commonly works with the following types of files:

## Text Files (.txt)

Text files store plain text data.

Example:

```
Name : Rahul
Age : 21
Department : CSE
```

Applications

- Notes
- Log files
- Configuration files
- Reports

---

## CSV Files (.csv)

CSV stands for **Comma-Separated Values**.

It stores tabular data in rows and columns.

Example

```
ID,Name,Department
101,Rahul,CSE
102,Anitha,ECE
```

Applications

- Student records
- Employee data
- Sales reports
- Financial data

---

## JSON Files (.json)

JSON stands for **JavaScript Object Notation**.

It stores data as key-value pairs.

Example

```json
{
    "id":101,
    "name":"Rahul",
    "department":"CSE"
}
```

Applications

- REST APIs
- Web applications
- Data exchange
- Configuration files

---

## PostgreSQL Database

PostgreSQL is an open-source relational database management system (RDBMS).

Unlike files, databases store data in tables and support SQL queries.

Applications

- Banking
- Hospital Management
- Inventory Systems
- Enterprise Applications

---

# 5. File Modes in Python

| Mode | Description |
|------|-------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create New File |
| rb | Read Binary |
| wb | Write Binary |

---

# 6. File Handling Functions

Python provides several functions for working with files.

### open()

Opens a file.

### read()

Reads the complete file.

### readline()

Reads one line.

### readlines()

Reads all lines.

### write()

Writes data into a file.

### close()

Closes the file.

---

# 7. CSV Module

Python provides the **csv** module.

Important functions

- csv.reader()
- csv.writer()
- csv.DictReader()
- csv.DictWriter()

Advantages

- Easy tabular data handling
- Compatible with Excel
- Simple syntax

---

# 8. JSON Module

Python provides the **json** module.

Important functions

- json.load()
- json.loads()
- json.dump()
- json.dumps()

Advantages

- Lightweight
- Human-readable
- Widely used in APIs

---

# 9. PostgreSQL Connectivity

Python communicates with PostgreSQL using the **psycopg2** library.

Steps

1. Connect to database.
2. Create cursor.
3. Execute SQL query.
4. Commit changes.
5. Retrieve data.
6. Close connection.

---

# 10. Advantages of File Handling

- Permanent storage
- Easy data sharing
- Supports automation
- Reduces manual work
- Enables ETL processing

---

# 11. Real-World Applications

### Banking

Store daily transaction records.

### Healthcare

Maintain patient information.

### E-Commerce

Store customer orders.

### Education

Manage student records.

### Data Engineering

Build ETL pipelines using CSV, JSON, and databases.

---

# 12. Best Practices

- Always close files after use.
- Use the correct file mode.
- Handle exceptions.
- Validate input data.
- Store sensitive information securely.
- Use CSV for tabular data.
- Use JSON for API communication.
- Use databases for large datasets.

---

# 13. Summary

Python provides powerful support for file handling using built-in libraries such as **csv** and **json**, along with external libraries like **psycopg2** for database connectivity. These capabilities form the foundation of modern Data Engineering pipelines by enabling reliable data ingestion, transformation, storage, and retrieval.

---

# 14. Key Terms

- File Handling
- Text File
- CSV
- JSON
- PostgreSQL
- psycopg2
- CRUD
- ETL
- Database
- Record
- Table

---

# 15. Review Questions

1. What is file handling?
2. Explain different file modes in Python.
3. What is a CSV file?
4. What is JSON?
5. What is PostgreSQL?
6. Explain the csv module.
7. Explain the json module.
8. What is psycopg2?
9. Explain the steps to connect Python with PostgreSQL.
10. List the applications of file handling in Data Engineering.
