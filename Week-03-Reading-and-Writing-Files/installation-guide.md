# Installation Guide

# Experiment No. 4

# PostgreSQL Database Connectivity Using Python

---

# 1. Objective

This guide explains how to install and configure PostgreSQL, pgAdmin4, Python, Visual Studio Code, and the psycopg2 library required for connecting Python with PostgreSQL.

---

# 2. Software Requirements

| Software | Version |
|----------|----------|
| Python | 3.10 or later |
| PostgreSQL | 18.x (Recommended) |
| pgAdmin4 | Latest Version |
| Visual Studio Code | Latest Version |
| psycopg2-binary | Latest Version |

---

# 3. Install Python

1. Download Python from the official website.
2. Run the installer.
3. Select **Add Python to PATH**.
4. Click **Install Now**.

Verify installation:

```bash
python --version
```

Expected Output

```text
Python 3.10.x
```

---

# 4. Install PostgreSQL

1. Download PostgreSQL.
2. Run the installer.
3. Select the installation directory.
4. Install pgAdmin4 when prompted.
5. Set the password for the **postgres** user.
6. Complete the installation.

---

# 5. Verify PostgreSQL Installation

Open Command Prompt.

Run:

```bash
"C:\Program Files\PostgreSQL\18\bin\psql.exe" --version
```

Expected Output

```text
psql (PostgreSQL) 18.x
```

---

# 6. Open pgAdmin4

Launch pgAdmin4.

Connect to the PostgreSQL server.

Example Connection

| Property | Value |
|----------|--------|
| Host | localhost |
| Port | 5433 |
| Username | postgres |
| Password | Your PostgreSQL Password |

> **Note:** In our lab setup, PostgreSQL 18 is configured on **port 5433**. If your installation uses the default port **5432**, update the connection settings accordingly.

---

# 7. Install psycopg2

Open Command Prompt.

Run

```bash
pip install psycopg2-binary
```

Verify

```bash
pip show psycopg2-binary
```

---

# 8. Create the Database

Open pgAdmin4.

Select

```
Databases
    ↓
Create
    ↓
Database
```

Database Name

```
dataengineering1
```

Click **Save**.

---

# 9. Create the Student Table

Open

```
Tools
    ↓
Query Tool
```

Execute

```sql
CREATE TABLE student(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30)
);
```

---

# 10. Insert Sample Records

```sql
INSERT INTO student VALUES
(101,'Rahul','CSE'),
(102,'Anitha','ECE'),
(103,'Kiran','MECH');
```

---

# 11. Verify Records

Execute

```sql
SELECT * FROM student;
```

Expected Output

```text
 id  |  name   | department
-----+---------+------------
101  | Rahul   | CSE
102  | Anitha  | ECE
103  | Kiran   | MECH
```

---

# 12. Configure Python

Create a Python file.

Example connection:

```python
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port="5433",
    database="dataengineering1",
    user="postgres",
    password="YOUR_PASSWORD"
)
```

Replace **YOUR_PASSWORD** with your PostgreSQL password.

---

# 13. Common Errors and Solutions

## Error

```
ModuleNotFoundError: No module named 'psycopg2'
```

Solution

```bash
pip install psycopg2-binary
```

---

## Error

```
password authentication failed
```

Solution

- Verify the PostgreSQL username.
- Verify the password.
- Ensure the correct port is used (5433 in this setup).

---

## Error

```
relation "student" does not exist
```

Solution

Create the table using:

```sql
CREATE TABLE student(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30)
);
```

---

## Error

```
IndentationError
```

Solution

- Use four spaces for indentation.
- Do not mix tabs and spaces.

---

## Error

```
'psql' is not recognized
```

Solution

Either:

- Add `C:\Program Files\PostgreSQL\18\bin` to the Windows PATH, or
- Run `psql.exe` using its full path.

---

# 14. Best Practices

- Use PostgreSQL 18 consistently.
- Close database connections after use.
- Commit transactions after INSERT, UPDATE, or DELETE operations.
- Store passwords securely in production applications.
- Use meaningful database and table names.

---

# 15. Summary

After completing this installation, students will be able to:

- Install PostgreSQL.
- Configure pgAdmin4.
- Install the psycopg2 library.
- Create a PostgreSQL database.
- Create database tables.
- Connect Python with PostgreSQL.
- Execute SQL queries using Python.
