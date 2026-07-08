"""
Experiment No. 4
Reading and Writing PostgreSQL Database Using Python
"""

import psycopg2

try:
    # ----------------------------------------
    # Step 1: Connect to PostgreSQL Database
    # ----------------------------------------

    connection = psycopg2.connect(
        host="localhost",
        port="5433",              # Change to 5432 if required
        database="dataengineering1",
        user="postgres",
        password="1234"
    )

    print("=" * 50)
    print("Connected Successfully to PostgreSQL")
    print("=" * 50)

    cursor = connection.cursor()

    # ----------------------------------------
    # Step 2: Create Table
    # ----------------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student(
        id INT PRIMARY KEY,
        name VARCHAR(50),
        department VARCHAR(30)
    );
    """)

    connection.commit()

    print("Student table verified.")

    # ----------------------------------------
    # Step 3: Insert Records
    # ----------------------------------------

    cursor.execute("""
    INSERT INTO student(id,name,department)
    VALUES
    (101,'Rahul','CSE'),
    (102,'Anitha','ECE'),
    (103,'Kiran','MECH')
    ON CONFLICT (id) DO NOTHING;
    """)

    connection.commit()

    print("Sample records inserted.")

    # ----------------------------------------
    # Step 4: Read Records
    # ----------------------------------------

    cursor.execute("SELECT * FROM student ORDER BY id;")

    rows = cursor.fetchall()

    print("\nStudent Records")
    print("-" * 50)

    print("{:<10} {:<20} {:<15}".format("ID", "NAME", "DEPARTMENT"))
    print("-" * 50)

    for row in rows:
        print("{:<10} {:<20} {:<15}".format(row[0], row[1], row[2]))

    print("-" * 50)

    # ----------------------------------------
    # Step 5: Close Connection
    # ----------------------------------------

    cursor.close()
    connection.close()

    print("\nDatabase connection closed successfully.")

except Exception as error:
    print("\nDatabase Error")
    print(error)