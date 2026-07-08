# Theory

# Experiment No. 4

# Reading and Writing PostgreSQL Database Using Python

---

# 1. Introduction

In Data Engineering, databases are used to store, manage, and retrieve large volumes of structured data. Python can communicate with relational databases using database connectors, enabling developers to automate data storage and retrieval.

PostgreSQL is one of the most popular open-source Relational Database Management Systems (RDBMS). It is widely used in enterprise applications, cloud platforms, data warehouses, and ETL (Extract, Transform, Load) pipelines because of its reliability, scalability, and SQL compliance.

Python communicates with PostgreSQL using the **psycopg2** library, which provides functions for establishing database connections, executing SQL statements, and retrieving query results.

---

# 2. Learning Objectives

After completing this experiment, students will be able to:

- Understand the basics of PostgreSQL.
- Connect Python with PostgreSQL.
- Execute SQL queries from Python.
- Create database tables.
- Insert records into a table.
- Retrieve records from a table.
- Close database resources correctly.

---

# 3. What is PostgreSQL?

PostgreSQL is an open-source Object Relational Database Management System (ORDBMS) used for storing and managing structured data. It supports SQL standards, transactions, indexing, views, stored procedures, triggers, and advanced data types.

PostgreSQL is widely used in:

- Banking applications
- Healthcare systems
- E-Commerce platforms
- Government databases
- Data Engineering pipelines
- Cloud-based applications

---

# 4. What is psycopg2?

**psycopg2** is a PostgreSQL database adapter for Python.

It allows Python programs to:

- Connect to PostgreSQL databases
- Execute SQL queries
- Insert records
- Update records
- Delete records
- Retrieve records

Installation command:

```bash
pip install psycopg2-binary
```

---

# 5. Database Connectivity Steps

Python communicates with PostgreSQL through the following steps:

1. Import the psycopg2 module.
2. Establish a database connection.
3. Create a cursor object.
4. Execute SQL queries.
5. Commit changes (for INSERT, UPDATE, DELETE).
6. Retrieve records (for SELECT).
7. Close the cursor.
8. Close the database connection.

---

# 6. Connection Parameters

A database connection requires the following parameters:

| Parameter | Description |
|-----------|-------------|
| host | Database server address (localhost) |
| port | PostgreSQL server port (5432 or 5433) |
| database | Database name |
| user | PostgreSQL username |
| password | PostgreSQL password |

Example:

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

# 7. Cursor Object

A cursor is an object used to execute SQL statements and retrieve query results.

Common cursor methods:

- execute()
- fetchone()
- fetchmany()
- fetchall()

Example:

```python
cursor = connection.cursor()
```

---

# 8. SQL Operations

The four basic database operations are known as CRUD operations.

| Operation | SQL Statement |
|-----------|---------------|
| Create | CREATE |
| Read | SELECT |
| Update | UPDATE |
| Delete | DELETE |

---

# 9. Transaction Management

Whenever data is modified, the changes should be saved permanently using:

```python
connection.commit()
```

If changes are not committed, they may be lost after the connection is closed.

---

# 10. Closing Database Resources

After completing database operations, both the cursor and the connection should be closed.

```python
cursor.close()
connection.close()
```

Closing resources prevents memory leaks and releases database connections.

---

# 11. Applications

PostgreSQL is widely used in:

- Student Information Systems
- Banking Applications
- Hospital Management Systems
- Inventory Management
- Payroll Systems
- Data Warehousing
- Business Intelligence
- Data Engineering Pipelines

---

# 12. Advantages

- Open source
- Highly secure
- ACID compliant
- Supports large databases
- High performance
- Platform independent
- Supports concurrent users

---

# 13. Best Practices

- Always close database connections.
- Use parameterized queries to prevent SQL injection.
- Commit transactions after modifying data.
- Handle exceptions using try-except blocks.
- Store passwords securely instead of hardcoding them.
- Use meaningful table and column names.

---

# 14. Summary

Python uses the **psycopg2** library to communicate with PostgreSQL databases. A typical workflow involves connecting to the database, executing SQL statements using a cursor, retrieving results, committing transactions, and closing the connection. This approach is widely used in Data Engineering to build ETL pipelines, automate database operations, and process large datasets efficiently.

---

# 15. Key Terms

- PostgreSQL
- RDBMS
- ORDBMS
- SQL
- psycopg2
- Cursor
- Connection
- Transaction
- Commit
- CRUD
- ETL
- Database

---

# 16. Review Questions

1. What is PostgreSQL?
2. What is an RDBMS?
3. What is psycopg2?
4. Explain the steps involved in database connectivity.
5. What is a cursor?
6. What is the purpose of commit()?
7. What is the purpose of fetchall()?
8. Explain CRUD operations.
9. Why should database connections be closed?
10. List the applications of PostgreSQL in Data Engineering.
