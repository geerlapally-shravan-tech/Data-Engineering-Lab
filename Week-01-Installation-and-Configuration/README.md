# Week 01 – Installation and Configuration

## Experiment Title

**Installing and Configuring Apache NiFi and Apache Airflow**

---

## 📖 Introduction

Apache NiFi and Apache Airflow are two of the most widely used tools in Data Engineering for building, managing, and automating data pipelines.

Apache NiFi is designed for data ingestion, routing, transformation, and system integration, while Apache Airflow is used to schedule, orchestrate, and monitor complex workflows. Together, they provide a powerful platform for developing reliable and scalable data engineering solutions.

In this experiment, students will install, configure, and verify both Apache NiFi and Apache Airflow on their local systems.

---

## 🎯 Aim

To install, configure, and verify Apache NiFi and Apache Airflow for building and managing data pipelines.

---

## 🎯 Objectives

After completing this experiment, students will be able to:

- Understand the purpose of Apache NiFi.
- Understand the purpose of Apache Airflow.
- Install Apache NiFi.
- Install Apache Airflow.
- Configure both tools.
- Verify successful installation.
- Launch the web interfaces.
- Understand the basic architecture of both tools.

---

## 🎓 Learning Outcomes

Students will be able to:

- Install Apache NiFi successfully.
- Install Apache Airflow successfully.
- Start and stop both services.
- Access the web interfaces.
- Understand where each tool is used in Data Engineering.

---

## 🛠 Software Required

- Windows 10/11 or Linux
- Java JDK 17 or later
- Python 3.10 or later
- Apache NiFi
- Apache Airflow
- VS Code
- Web Browser (Chrome/Edge)

---

## 📚 Concepts Covered

- Data Engineering
- Data Pipeline
- Workflow Automation
- Apache NiFi
- Apache Airflow
- Java
- Python Virtual Environment
- Scheduler
- DAG (Directed Acyclic Graph)
- FlowFile
- Processors

---

## 🏗 Architecture Overview

```text
             Data Sources
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
 Apache NiFi           Apache Airflow
(Data Ingestion)   (Workflow Scheduling)
        │                     │
        └──────────┬──────────┘
                   ▼
            Data Pipeline
                   │
                   ▼
          Database / Data Lake
```

---

## 📂 Folder Structure

```text
Week-01-Installation-and-Configuration/
│
├── README.md
├── Theory.md
├── Installation-Guide.md
├── Faculty-Notes.md
├── Student-Notes.md
├── Assignments.md
├── Viva.md
│
├── Programs/
│   ├── README.md
│   ├── Program-01-Install-Java.md
│   ├── Program-02-Install-Python.md
│   ├── Program-03-Install-Apache-NiFi.md
│   ├── Program-04-Configure-Apache-NiFi.md
│   ├── Program-05-Install-Apache-Airflow.md
│   ├── Program-06-Configure-Apache-Airflow.md
│   └── Program-07-Verify-Installation.md
│
├── Images/
│   └── README.md
│
├── Outputs/
│   └── README.md
│
└── Resources/
    └── README.md
```

---

## 💻 Experiments Included

| Program | Description |
|----------|-------------|
| Program-01 | Install Java JDK |
| Program-02 | Install Python |
| Program-03 | Install Apache NiFi |
| Program-04 | Configure Apache NiFi |
| Program-05 | Install Apache Airflow |
| Program-06 | Configure Apache Airflow |
| Program-07 | Verify Installation |

---

## 🔄 Installation Workflow

```text
Install Java
       │
       ▼
Install Python
       │
       ▼
Install Apache NiFi
       │
       ▼
Configure Apache NiFi
       │
       ▼
Install Apache Airflow
       │
       ▼
Configure Apache Airflow
       │
       ▼
Verify Installation
       │
       ▼
Launch Web Interfaces
```

---

## 🌍 Real-World Applications

- Enterprise ETL Pipelines
- Banking Data Processing
- Healthcare Data Integration
- Cloud Data Engineering
- IoT Data Collection
- Data Warehouse Automation
- Business Intelligence Workflows

---

## 📌 Expected Outcome

After completing this experiment, students will be able to install, configure, and verify Apache NiFi and Apache Airflow, access their web interfaces, and understand their role in building modern data pipelines.

---

## 📖 References

1. Apache NiFi Documentation
2. Apache Airflow Documentation
3. Oracle Java Documentation
4. Python Documentation

---

## 👨‍🏫 Instructor

**Shravan Chandra Geerlapally**

Assistant Professor

---

## 📄 License

This repository is intended for educational purposes for the Data Engineering Laboratory course.

---

⭐ **If this repository helps your learning, please consider starring the repository.**
