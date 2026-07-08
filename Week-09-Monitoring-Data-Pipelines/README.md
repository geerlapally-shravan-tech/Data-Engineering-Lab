# Week 09 – Monitoring Data Pipelines

## Experiment Title

**Monitoring Data Pipelines**

---

## 📖 Introduction

Data pipelines are responsible for moving, transforming, and processing data between different systems. In production environments, it is essential to continuously monitor these pipelines to ensure that data is flowing correctly, tasks are completed successfully, and failures are detected immediately.

Apache NiFi provides several monitoring capabilities, including the graphical user interface (GUI), processor statistics, queue monitoring, Data Provenance, Bulletin Board, and REST APIs. Monitoring helps Data Engineers identify bottlenecks, troubleshoot failures, optimize performance, and maintain reliable data pipelines.

---

## 🎯 Objectives

After completing this experiment, students will be able to:

- Understand the importance of monitoring data pipelines.
- Monitor Apache NiFi using the graphical user interface (GUI).
- Analyze processor statistics and queue status.
- Track data movement using Data Provenance.
- Monitor NiFi using REST APIs.
- Develop simple Python scripts for monitoring pipelines.
- Identify and troubleshoot common pipeline failures.

---

## 🎓 Learning Outcomes

After successful completion of this experiment, students will be able to:

- Monitor data pipelines in real time.
- Analyze processor performance.
- Detect and troubleshoot errors.
- Use REST APIs for monitoring.
- Develop Python-based monitoring utilities.
- Understand production pipeline monitoring techniques.

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
- Bulletin Board
- Data Provenance
- REST API
- Python Monitoring
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
     ┌─────────────┼──────────────┐
     │             │              │
     ▼             ▼              ▼
 Processor     Queue Status   Bulletin Board
 Statistics
     │
     ▼
 Data Provenance
     │
     ▼
 REST API
     │
     ▼
 Python Monitoring Script
```

---

## 📂 Folder Structure

```text
Week-09-Monitoring-Data-Pipelines/
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
│   ├── Program-01-NiFi-GUI-Monitoring.md
│   ├── Program-02-Processor-Statistics.md
│   ├── Program-03-Queue-Monitoring.md
│   ├── Program-04-Data-Provenance.md
│   ├── Program-05-REST-API-Monitoring.py
│   └── Program-06-Python-Monitoring.py
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
|----------|-------------|
| Program-01 | Monitor Apache NiFi using the GUI |
| Program-02 | Analyze Processor Statistics |
| Program-03 | Monitor Queues |
| Program-04 | Monitor Data Provenance |
| Program-05 | Access NiFi REST API using Python |
| Program-06 | Develop a Python Monitoring Script |

---

## 🔄 Monitoring Workflow

```text
Data Pipeline
      │
      ▼
Apache NiFi
      │
      ▼
Pipeline Execution
      │
      ▼
Processor Statistics
      │
      ▼
Queue Monitoring
      │
      ▼
Data Provenance
      │
      ▼
REST API
      │
      ▼
Python Monitoring Dashboard
```

---

## 🌍 Real-World Applications

- Banking transaction monitoring
- Healthcare data pipeline monitoring
- IoT sensor monitoring
- Cloud ETL monitoring
- Production system monitoring
- Enterprise data pipeline management
- Security log monitoring

---

## 📁 Sample Dataset

Students may use:

- Student Records
- Employee Records
- Sales Dataset
- Customer Transactions
- Sensor Data
- Server Logs

---

## 📌 Expected Outcome

After completing this experiment, students will be able to monitor Apache NiFi pipelines using the graphical interface, processor statistics, Data Provenance, REST APIs, and Python scripts to ensure reliable, efficient, and fault-tolerant data processing.

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

This repository is intended for educational purposes to support the Data Engineering Laboratory course.

---

⭐ **If this repository helps your learning, please consider starring the repository.**
