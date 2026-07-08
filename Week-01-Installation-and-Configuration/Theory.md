# Theory

# Experiment No. 1

# Installing and Configuring Apache NiFi and Apache Airflow

---

# 1. Introduction

Data has become one of the most valuable assets in today's digital world. Every organization generates enormous amounts of data from websites, mobile applications, sensors, banking systems, hospitals, social media platforms, and enterprise applications. Before this data can be analyzed, it must be collected, stored, processed, and transferred efficiently.

Data Engineering is the discipline that focuses on designing and building systems capable of collecting, transforming, storing, and processing data at scale. Data Engineers build automated workflows known as **data pipelines** that move data from one system to another while maintaining its quality, security, and reliability.

Two of the most widely used tools in modern Data Engineering are **Apache NiFi** and **Apache Airflow**. Apache NiFi is used for real-time data movement and integration, whereas Apache Airflow is used for workflow orchestration and scheduling.

---

# 2. Learning Objectives

After completing this experiment, students will be able to:

- Understand the role of Data Engineering.
- Explain the importance of data pipelines.
- Understand Apache NiFi architecture.
- Understand Apache Airflow architecture.
- Install Apache NiFi.
- Install Apache Airflow.
- Verify successful installation.
- Access the web interfaces of both tools.

---

# 3. What is Data Engineering?

Data Engineering is the process of designing, building, and maintaining systems that collect, store, transform, and process large volumes of data for analysis and decision-making.

A Data Engineer develops reliable and scalable pipelines that move data from multiple sources to storage systems and analytical platforms.

### Responsibilities of a Data Engineer

- Collect data from multiple sources
- Build ETL/ELT pipelines
- Clean and transform data
- Store data securely
- Ensure data quality
- Monitor data pipelines
- Optimize data processing

---

# 4. What is a Data Pipeline?

A Data Pipeline is an automated sequence of steps that transfers data from a source system to a destination system.

Typical stages include:

- Data Collection
- Data Validation
- Data Transformation
- Data Loading
- Data Storage
- Data Analysis

### Data Pipeline Workflow

```text
Data Source
      │
      ▼
Data Collection
      │
      ▼
Data Cleaning
      │
      ▼
Data Transformation
      │
      ▼
Database / Data Warehouse
      │
      ▼
Analytics & Reporting
```

---

# 5. Apache NiFi

Apache NiFi is an open-source data integration platform developed by the Apache Software Foundation.

It provides an easy-to-use graphical interface for designing and managing data flows between systems.

NiFi is primarily used for:

- Data ingestion
- Data routing
- Data transformation
- Data synchronization
- Data migration

---

# 6. Features of Apache NiFi

- Web-based graphical interface
- Drag-and-drop development
- Real-time data processing
- Flow-based programming
- Data provenance
- Guaranteed data delivery
- Prioritized queues
- Secure communication
- Scalability
- Fault tolerance

---

# 7. Apache NiFi Architecture

Major components include:

## FlowFile

A FlowFile represents a piece of data moving through the NiFi pipeline.

## Processor

Processors perform operations such as reading, writing, filtering, routing, and transforming data.

Examples:

- GetFile
- PutFile
- ExecuteSQL
- ReplaceText
- ConvertRecord

## Connection

Connections transfer FlowFiles between processors.

## Process Group

A collection of related processors grouped together.

## Controller Services

Reusable services such as database connections and file system access.

---

### Apache NiFi Architecture

```text
Data Source
      │
      ▼
GetFile Processor
      │
      ▼
Transform Processor
      │
      ▼
Route Processor
      │
      ▼
PutDatabase Processor
      │
      ▼
Database
```

---

# 8. Advantages of Apache NiFi

- Easy to learn
- No coding required for basic workflows
- High throughput
- Excellent monitoring
- Secure data transfer
- Supports hundreds of processors

---

# 9. Applications of Apache NiFi

- Banking
- Healthcare
- IoT
- Cloud Computing
- Government Services
- Cybersecurity
- Big Data
- Log Collection

---

# 10. Apache Airflow

Apache Airflow is an open-source workflow orchestration platform used to schedule, execute, and monitor complex workflows.

Airflow workflows are defined using Python programs called **DAGs (Directed Acyclic Graphs)**.

---

# 11. Features of Apache Airflow

- Workflow scheduling
- DAG-based execution
- Retry mechanism
- Logging
- Monitoring
- Scalability
- Extensible architecture
- Web-based interface

---

# 12. Apache Airflow Architecture

The main components are:

## Web Server

Provides the graphical user interface.

## Scheduler

Schedules tasks according to defined intervals.

## Executor

Executes workflow tasks.

## Workers

Run the scheduled tasks.

## Metadata Database

Stores workflow information, task status, and logs.

---

### Apache Airflow Architecture

```text
User
   │
   ▼
Web Server
   │
   ▼
Scheduler
   │
   ▼
Executor
   │
   ▼
Workers
   │
   ▼
Database
```

---

# 13. Advantages of Apache Airflow

- Python-based workflows
- Highly scalable
- Flexible scheduling
- Easy monitoring
- Automatic retries
- Open source

---

# 14. Applications of Apache Airflow

- ETL Pipelines
- Machine Learning Workflows
- Cloud Automation
- Business Reporting
- Data Warehousing
- Workflow Scheduling

---

# 15. Apache NiFi vs Apache Airflow

| Feature | Apache NiFi | Apache Airflow |
|----------|-------------|----------------|
| Primary Purpose | Data movement | Workflow scheduling |
| Programming | GUI-based | Python-based |
| Processing | Real-time and batch | Mostly batch workflows |
| Interface | Drag-and-drop | DAG code |
| Main Unit | FlowFile | Task |
| Scheduling | Basic scheduling | Advanced scheduling |
| Monitoring | Excellent | Excellent |
| Typical Use | Data ingestion | Workflow orchestration |

---

# 16. Real-World Example

Consider an online shopping platform.

1. Customers place orders through a website.
2. Apache NiFi collects order data from multiple sources.
3. The data is validated and transformed.
4. Apache Airflow schedules daily ETL jobs.
5. The processed data is stored in PostgreSQL.
6. Business dashboards display sales reports using Kibana.

---

# 17. Best Practices

- Use the latest stable versions.
- Install Java before Apache NiFi.
- Use a Python virtual environment for Apache Airflow.
- Keep configuration files backed up.
- Verify installations after every step.
- Monitor system resources during execution.

---

# 18. Summary

Apache NiFi and Apache Airflow are two essential tools in the Data Engineering ecosystem. Apache NiFi specializes in data ingestion, routing, and transformation through a graphical interface, while Apache Airflow focuses on workflow scheduling and orchestration using Python-based DAGs. Together, these tools help organizations build reliable, scalable, and automated data pipelines for processing large volumes of data.

---

# 19. Key Terms

- Data Engineering
- Data Pipeline
- ETL
- Workflow
- Apache NiFi
- Apache Airflow
- FlowFile
- Processor
- DAG
- Scheduler
- Executor
- Metadata Database

---

# 20. Review Questions

1. What is Data Engineering?
2. What is a Data Pipeline?
3. Explain the architecture of Apache NiFi.
4. Explain the architecture of Apache Airflow.
5. Differentiate Apache NiFi and Apache Airflow.
6. What is a FlowFile?
7. What is a DAG?
8. List the advantages of Apache NiFi.
9. List the advantages of Apache Airflow.
10. Explain a real-world application of Apache NiFi and Apache Airflow.
