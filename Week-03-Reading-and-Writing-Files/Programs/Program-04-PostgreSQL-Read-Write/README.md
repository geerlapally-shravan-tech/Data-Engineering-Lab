# Program-04

# Reading and Writing PostgreSQL Database Using Python

---

## Experiment No.

04

---

## Aim

To connect Python with PostgreSQL, create a table, insert records, and retrieve data.

---

## Objective

To understand database connectivity between Python and PostgreSQL using the `psycopg2` library.

---

## Prerequisites

- Python 3.x
- PostgreSQL installed and running
- pgAdmin4
- psycopg2 library installed

Install psycopg2 using:

```bash
pip install psycopg2-binary
```

---

## Theory

PostgreSQL is an open-source relational database management system (RDBMS). Python connects to PostgreSQL using the **psycopg2** library.

The basic steps are:

1. Connect to the database.
2. Create a cursor.
3. Execute SQL statements.
4. Commit changes.
5. Retrieve records.
6. Close the connection.

---

## Software Required

- Python 3.x
- PostgreSQL
- pgAdmin4
- psycopg2

---

## Algorithm

1. Import psycopg2.
2. Connect to PostgreSQL.
3. Create a table.
4. Insert records.
5. Commit the transaction.
6. Retrieve records.
7. Display records.
8. Close the connection.

---

## Program

The Python program is available in **postgresql_read_write.py**.

---

## Expected Output

```text
Connected Successfully

Student Records

101 Rahul CSE
102 Anitha ECE
103 Kiran MECH
```

---

## Applications

- Student Information Systems
- Banking Systems
- Healthcare Management
- Inventory Systems
- ETL Pipelines

---

## Advantages

- Reliable
- Secure
- ACID compliant
- Scalable

---

## Result

The program connected successfully to PostgreSQL, inserted records into the table, and displayed the stored records.

---

## Viva Questions

1. What is PostgreSQL?
2. What is psycopg2?
3. What is a cursor?
4. What is commit()?
5. What is fetchall()?
6. Why do we close the database connection?

---

## References

1. PostgreSQL Documentation
2. psycopg2 Documentation
3. Python Documentation
