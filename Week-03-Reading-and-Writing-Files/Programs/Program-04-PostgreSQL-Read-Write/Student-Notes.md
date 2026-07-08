# Student Notes

# Experiment No. 4

# Reading and Writing PostgreSQL Database Using Python

---

# Aim

To connect Python with PostgreSQL, insert records into a database table, and retrieve the stored records.

---

# Learning Outcomes

After completing this experiment, students will be able to:

- Connect Python with PostgreSQL.
- Execute SQL statements using Python.
- Create and use database tables.
- Insert records into a PostgreSQL database.
- Retrieve records using SQL queries.
- Close database resources properly.

---

# PostgreSQL

## Definition

PostgreSQL is an open-source Relational Database Management System (RDBMS) used to store and manage structured data.

Applications

- Banking
- Healthcare
- E-Commerce
- Education
- Data Engineering

---

# psycopg2

## Definition

psycopg2 is a Python library used to connect Python applications with PostgreSQL databases.

Installation

```bash
pip install psycopg2-binary
```

---

# Database Connection

Syntax

```python
connection = psycopg2.connect(
    host="localhost",
    port="5433",
    database="dataengineering1",
    user="postgres",
    password="1234"
)
```

---

# Connection Parameters

| Parameter | Description |
|------------|-------------|
| host | Database Server |
| port | PostgreSQL Port |
| database | Database Name |
| user | Username |
| password | Password |

---

# Cursor Object

A cursor executes SQL statements.

Syntax

```python
cursor = connection.cursor()
```

---

# Frequently Used Cursor Methods

| Method | Purpose |
|----------|----------|
| execute() | Execute SQL Query |
| fetchone() | Read One Record |
| fetchmany() | Read Multiple Records |
| fetchall() | Read All Records |

---

# CRUD Operations

| Operation | SQL Command |
|------------|-------------|
| Create | CREATE |
| Read | SELECT |
| Update | UPDATE |
| Delete | DELETE |

---

# Important SQL Commands

Create Database

```sql
CREATE DATABASE dataengineering1;
```

Create Table

```sql
CREATE TABLE student(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30)
);
```

Insert Records

```sql
INSERT INTO student VALUES
(101,'Rahul','CSE'),
(102,'Anitha','ECE'),
(103,'Kiran','MECH');
```

Display Records

```sql
SELECT * FROM student;
```

---

# Important Python Functions

```python
psycopg2.connect()

cursor()

execute()

fetchall()

commit()

close()
```

---

# Transaction

To save changes permanently:

```python
connection.commit()
```

---

# Closing Resources

```python
cursor.close()

connection.close()
```

Always close the cursor and database connection after completing operations.

---

# Quick Revision

- PostgreSQL is an RDBMS.
- psycopg2 connects Python with PostgreSQL.
- cursor() executes SQL queries.
- commit() saves changes.
- fetchall() retrieves all records.
- close() releases database resources.

---

# Frequently Asked Viva Questions

1. What is PostgreSQL?
2. What is an RDBMS?
3. What is psycopg2?
4. Why is psycopg2 used?
5. What is a cursor?
6. What is commit()?
7. What is fetchall()?
8. What is the purpose of close()?
9. What are CRUD operations?
10. What is the default PostgreSQL port?

---

# University Examination Questions

## Short Questions

1. Define PostgreSQL.
2. What is psycopg2?
3. Explain commit().
4. Explain cursor().
5. What is fetchall()?

---

## Long Questions

1. Explain database connectivity using Python and PostgreSQL.
2. Explain CRUD operations with suitable examples.
3. Explain the role of psycopg2 in Python database programming.

---

# Summary

Python communicates with PostgreSQL using the psycopg2 library. A database connection is established using connection parameters, SQL statements are executed using a cursor, results are retrieved using fetch methods, and resources are released by closing the cursor and connection. These concepts are fundamental for building ETL pipelines and database-driven applications in Data Engineering.
