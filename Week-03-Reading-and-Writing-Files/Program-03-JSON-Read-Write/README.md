# Program-03

# Reading and Writing JSON Files Using Python

---

## Experiment No.

03

---

## Experiment Title

Reading and Writing JSON Files Using Python

---

## Aim

To perform reading and writing operations on JSON files using Python.

---

## Objective

The objective of this experiment is to understand how Python uses the built-in **json** module to create, write, read, and process JSON files. Students will learn how JSON stores data in key-value pairs and why it is widely used in web applications, REST APIs, cloud services, and Data Engineering pipelines.

---

## Prerequisites

- Python 3.x
- Visual Studio Code (VS Code)
- Basic knowledge of Python programming
- Understanding of Python dictionaries

---

## Theory

JSON (**JavaScript Object Notation**) is a lightweight data-interchange format used for storing and exchanging data. It stores information as **key-value pairs**, making it easy for both humans and machines to read and process.

Python provides the built-in **json** module to work with JSON files.

JSON is widely used because it is:

- Human-readable
- Lightweight
- Language-independent
- Easy to exchange over networks
- Compatible with REST APIs

Unlike CSV files, JSON can represent **nested objects**, making it suitable for complex data structures.

---

## Software Required

- Python 3.x
- Visual Studio Code
- JSON Module (Built-in)

---

## Algorithm

1. Import the **json** module.
2. Create a Python dictionary containing employee information.
3. Open a JSON file in write mode.
4. Write the dictionary into the JSON file using `json.dump()`.
5. Close the file.
6. Open the JSON file in read mode.
7. Read the JSON data using `json.load()`.
8. Display the employee details.
9. Close the file.
10. Stop the program.

---

## Program

The Python source code is available in **json_file.py**.

---

## Input

No user input is required.

The program automatically creates employee information.

---

## Expected Output

```text
JSON file created successfully.

Employee Details
--------------------------
ID : 101
Name : Rahul
Department : CSE
Salary : 50000
```

---

## Output File

The program automatically creates the following file:

**employee.json**

Contents of **employee.json**

```json
{
    "ID": 101,
    "Name": "Rahul",
    "Department": "CSE",
    "Salary": 50000
}
```

---

## Applications

- REST API communication
- Cloud Computing
- Web Applications
- Mobile Applications
- Configuration Files
- Data Engineering Pipelines
- Machine Learning Data Exchange
- Microservices

---

## Advantages

- Lightweight
- Human-readable
- Easy to exchange data
- Platform independent
- Supports nested objects
- Supported by almost every programming language

---

## Limitations

- Does not support comments
- Not suitable for complex relational data
- Large JSON files may consume more memory
- Less efficient than binary serialization formats for some use cases

---

## Learning Outcome

After completing this experiment, students will be able to:

- Create JSON files using Python.
- Read JSON files using Python.
- Convert Python dictionaries into JSON format.
- Process structured data stored in JSON files.
- Understand the importance of JSON in Data Engineering.

---

## Result

The program was executed successfully. Employee information was written to a JSON file and read back correctly using Python's **json** module.

---

## Viva Questions

1. What is JSON?
2. What does JSON stand for?
3. Which Python module is used for JSON file handling?
4. What is the purpose of `json.dump()`?
5. What is the purpose of `json.load()`?
6. What is the difference between `json.dump()` and `json.dumps()`?
7. What is the difference between `json.load()` and `json.loads()`?
8. Why is JSON widely used in REST APIs?
9. What is the difference between JSON and CSV?
10. List two real-world applications of JSON.

---

## References

1. Python Documentation – JSON Module
2. JSON Official Documentation
3. PostgreSQL Documentation
4. Data Engineering Best Practices
