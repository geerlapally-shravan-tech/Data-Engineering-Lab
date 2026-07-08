# Installation Guide

# Week-01

# Installing and Configuring Apache NiFi and Apache Airflow

---

# Objective

The objective of this experiment is to install, configure, and verify Apache NiFi and Apache Airflow on a local machine.

---

# Software Requirements

| Software | Recommended Version |
|-----------|---------------------|
| Operating System | Windows 10/11 (64-bit) or Ubuntu Linux |
| Java JDK | 17 or later |
| Python | 3.10 or later |
| Apache NiFi | Latest Stable Version |
| Apache Airflow | Latest Stable Version |
| Web Browser | Google Chrome / Microsoft Edge |
| Visual Studio Code | Latest Version |

---

# System Requirements

- Minimum 8 GB RAM (16 GB Recommended)
- Dual Core Processor or higher
- At least 10 GB free disk space
- Internet connection for downloading software

---

# Step 1: Install Java JDK

## Download

Download Java JDK from the official Oracle website or OpenJDK distribution.

After installation, verify Java.

Open Command Prompt and execute:

```bash
java -version
```

Expected Output

```text
java version "17.x.x"
```

If the version is displayed, Java is installed successfully.

---

# Step 2: Configure JAVA_HOME

Open

Control Panel

↓

System

↓

Advanced System Settings

↓

Environment Variables

Create

```
JAVA_HOME
```

Set the value to the Java installation directory.

Example

```
C:\Program Files\Java\jdk-17
```

Add the following to the PATH variable.

```
%JAVA_HOME%\bin
```

Verify again.

```bash
java -version
```

---

# Step 3: Install Python

Download Python from the official Python website.

During installation, enable:

✔ Add Python to PATH

Verify installation.

```bash
python --version
```

Expected Output

```text
Python 3.10.x
```

Verify pip.

```bash
pip --version
```

---

# Step 4: Install Apache NiFi

Download Apache NiFi.

Extract the ZIP file.

Example location

```
C:\Apache\NiFi
```

Navigate to

```
bin
```

Run

```text
run-nifi.bat
```

Wait until NiFi starts.

---

# Step 5: Open Apache NiFi

Open your browser.

Visit

```
https://localhost:8443/nifi
```

The Apache NiFi dashboard should appear.

---

# Step 6: Stop Apache NiFi

Navigate to

```
bin
```

Run

```text
stop-nifi.bat
```

---

# Step 7: Create a Python Virtual Environment

Navigate to your working directory.

Create a virtual environment.

```bash
python -m venv airflow-env
```

Activate it.

Windows

```bash
airflow-env\Scripts\activate
```

Linux

```bash
source airflow-env/bin/activate
```

---

# Step 8: Install Apache Airflow

Upgrade pip.

```bash
pip install --upgrade pip
```

Install Apache Airflow.

```bash
pip install apache-airflow
```

Wait until installation completes successfully.

---

# Step 9: Initialize Airflow Database

Execute

```bash
airflow db init
```

This creates the metadata database.

---

# Step 10: Create Administrator User

Execute

```bash
airflow users create ^
--username admin ^
--firstname Admin ^
--lastname User ^
--role Admin ^
--email admin@example.com
```

Enter a password when prompted.

---

# Step 11: Start Airflow Scheduler

Open a terminal.

Execute

```bash
airflow scheduler
```

Keep this terminal running.

---

# Step 12: Start Airflow Web Server

Open another terminal.

Execute

```bash
airflow webserver
```

---

# Step 13: Open Airflow

Visit

```
http://localhost:8080
```

Login using the administrator credentials.

---

# Step 14: Verify Installation

Verify the following.

| Component | Status |
|-----------|--------|
| Java | Installed |
| Python | Installed |
| Apache NiFi | Running |
| Apache Airflow | Running |
| NiFi UI | Accessible |
| Airflow UI | Accessible |

---

# Common Errors

## Error 1

```
java is not recognized
```

Solution

- Verify Java installation.
- Configure JAVA_HOME.
- Restart Command Prompt.

---

## Error 2

```
python is not recognized
```

Solution

- Reinstall Python.
- Enable "Add Python to PATH".

---

## Error 3

```
Port 8443 already in use
```

Solution

- Stop the application using the port.
- Change the NiFi port in the configuration.

---

## Error 4

```
Port 8080 already in use
```

Solution

- Stop the conflicting process.
- Restart Airflow.

---

## Error 5

```
ModuleNotFoundError
```

Solution

Install the missing package.

Example

```bash
pip install pandas
```

---

# Best Practices

- Install Java before Apache NiFi.
- Install Python before Apache Airflow.
- Use a Python virtual environment.
- Verify each installation before proceeding.
- Keep software updated.
- Do not modify configuration files unnecessarily.
- Use the latest stable versions.

---

# Conclusion

In this experiment, Apache NiFi and Apache Airflow were successfully installed and configured. The installation was verified using command-line tools and web interfaces. These tools will be used throughout the remaining Data Engineering Laboratory experiments to build, automate, monitor, and deploy data pipelines.

---

# References

1. Apache NiFi Documentation
2. Apache Airflow Documentation
3. Oracle Java Documentation
4. Python Documentation
