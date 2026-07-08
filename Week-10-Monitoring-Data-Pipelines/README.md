# Week 10 – Monitoring Data Pipelines

## Experiment Title

**Monitoring Data Pipelines**

---

## 📖 Introduction

Monitoring is a critical component of Data Engineering. It ensures that data pipelines are running correctly, data is processed successfully, and failures are detected and resolved quickly. Apache NiFi provides multiple monitoring mechanisms through its Graphical User Interface (GUI), processor statistics, Data Provenance, Bulletin Board, and REST APIs.

In this experiment, students will learn how to monitor the health and performance of data pipelines using Apache NiFi and Python.

---

## 🎯 Aim

To monitor Apache NiFi data pipelines using the GUI, processors, Python, and REST APIs.

---

## 🎯 Objectives

After completing this experiment, students will be able to:

- Understand the importance of pipeline monitoring.
- Monitor Apache NiFi using the GUI.
- Analyze processor statistics.
- Monitor queues and data flow.
- Track data movement using Data Provenance.
- Use REST APIs to retrieve monitoring information.
- Develop Python scripts for monitoring pipeline status.

---

## 🎓 Learning Outcomes

Students will be able to:

- Monitor data pipelines effectively.
- Detect and troubleshoot pipeline failures.
- Analyze processor performance.
- Use Python and REST APIs for automation.
- Apply monitoring techniques in production environments.

---

## 🛠 Software Required

- Apache NiFi
- Python 3.x
- Requests Library
- VS Code
- Web Browser

---

## 📚 Concepts Covered

- Pipeline Monitoring
- Apache NiFi GUI
- Processor Statistics
- Queue Monitoring
- Data Provenance
- Bulletin Board
- REST API
- Python Requests
- Performance Metrics
- Error Handling

---

## 🏗 Monitoring Architecture

```text
Data Source
      │
      ▼
Apache NiFi
      │
      ├────────► GUI Monitoring
      │
      ├────────► Processor Statistics
      │
      ├────────► Queue Monitoring
      │
      ├────────► Data Provenance
      │
      └────────► REST API
                    │
                    ▼
             Python Monitoring
```

---

## 📂 Folder Structure

```text
Week-10-Monitoring-Data-Pipelines/
│
├── README.md
├── Theory.md
├── Faculty-Notes.md
├── Student-Notes.md
├── Assignments.md
├── Viva.md
│
├── Programs/
│   ├── README.md
│   ├── Program-01-GUI-Monitoring.md
│   ├── Program-02-Processor-Monitoring.md
│   ├── Program-03-Queue-Monitoring.md
│   ├── Program-04-Data-Provenance.md
│   ├── Program-05-REST-API-Monitoring.py
│   ├── Program-06-Python-Monitoring.py
│   └── Program-07-Pipeline-Health-Check.py
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

## 💻 Programs Included

| Program | Description |
|---------|-------------|
| Program-01 | Monitor NiFi using the GUI |
| Program-02 | Analyze Processor Statistics |
| Program-03 | Monitor Queues |
| Program-04 | Track Data Provenance |
| Program-05 | Access NiFi REST API using Python |
| Program-06 | Build a Python Monitoring Script |
| Program-07 | Create a Pipeline Health Check Script |

---

## 🔄 Monitoring Workflow

```text
Data Pipeline
      │
      ▼
Pipeline Execution
      │
      ▼
Monitor Processors
      │
      ▼
Monitor Queues
      │
      ▼
Check Data Provenance
      │
      ▼
REST API Monitoring
      │
      ▼
Python Monitoring Dashboard
```

---

## 🌍 Real-World Applications

- Banking transaction monitoring
- Healthcare data pipeline monitoring
- IoT device monitoring
- Cloud ETL monitoring
- Enterprise data integration
- Production system monitoring
- Security log analysis

---

## 📁 Sample Datasets

- Student Dataset
- Employee Dataset
- Sales Dataset
- Customer Transactions
- Sensor Data
- Server Logs

---

## 📌 Expected Outcome

After completing this experiment, students will be able to monitor Apache NiFi data pipelines using the graphical interface, processor statistics, Data Provenance, Python scripts, and REST APIs to ensure reliable and efficient data processing.

---

## 📖 References

1. Apache NiFi Documentation
2. Apache NiFi REST API Documentation
3. Python Requests Documentation
4. Data Engineering Best Practices

---

## 👨‍🏫 Instructor

**Shravan Chandra Geerlapally**

Assistant Professor

---

## 📄 License

This repository is intended for educational purposes for the Data Engineering Laboratory course.

---

⭐ If this repository helps your learning, please consider starring the repository.
