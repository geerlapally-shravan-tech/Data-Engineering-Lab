# Week 09 – Version Control with the NiFi Registry

## Experiment Title

**Version Control with the NiFi Registry**

---

## 📖 Introduction

Apache NiFi Registry is a companion application for Apache NiFi that provides version control for data flows. It allows Data Engineers to store, manage, compare, and restore different versions of process groups. This enables collaborative development, change tracking, rollback, and deployment of reliable data pipelines.

Version control is an essential practice in modern Data Engineering because it improves collaboration, simplifies maintenance, and ensures consistency across development, testing, and production environments.

---

## 🎯 Aim

To understand and implement version control for Apache NiFi data flows using Apache NiFi Registry.

---

## 🎯 Objectives

After completing this experiment, students will be able to:

- Install and configure Apache NiFi Registry.
- Connect Apache NiFi with NiFi Registry.
- Create Registry Buckets.
- Version Process Groups.
- Update and manage different versions.
- Restore previous versions of a data flow.
- Understand Git persistence in NiFi Registry.

---

## 🎓 Learning Outcomes

Students will be able to:

- Configure NiFi Registry.
- Publish process groups.
- Maintain version history.
- Compare flow versions.
- Restore previous versions.
- Understand collaborative pipeline development.

---

## 🛠 Software Required

- Apache NiFi
- Apache NiFi Registry
- Java JDK 17+
- Git
- Web Browser
- VS Code

---

## 📚 Concepts Covered

- Apache NiFi Registry
- Version Control
- Buckets
- Process Groups
- Flow Snapshots
- Version History
- Flow Comparison
- Restore Version
- Git Persistence
- Collaboration

---

## 🏗 NiFi Registry Architecture

```text
Developer
      │
      ▼
Apache NiFi
      │
      ▼
Publish Process Group
      │
      ▼
Apache NiFi Registry
      │
      ▼
Version History
      │
      ├── Compare Versions
      ├── Restore Version
      └── Git Persistence
```

---

## 📂 Folder Structure

```text
Week-09-Version-Control-with-NiFi-Registry/
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
│   ├── Program-01-Install-NiFi-Registry.md
│   ├── Program-02-Configure-NiFi-Registry.md
│   ├── Program-03-Create-Bucket.md
│   ├── Program-04-Version-a-Process-Group.md
│   ├── Program-05-Compare-Flow-Versions.md
│   ├── Program-06-Restore-Flow-Version.md
│   └── Program-07-Git-Persistence.md
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
| Program-01 | Install Apache NiFi Registry |
| Program-02 | Configure NiFi Registry |
| Program-03 | Create a Registry Bucket |
| Program-04 | Version a Process Group |
| Program-05 | Compare Flow Versions |
| Program-06 | Restore a Previous Version |
| Program-07 | Configure Git Persistence |

---

## 🔄 Workflow

```text
Create Data Flow
        │
        ▼
Publish Process Group
        │
        ▼
Apache NiFi Registry
        │
        ▼
Create Version
        │
        ▼
Modify Flow
        │
        ▼
Commit New Version
        │
        ▼
Compare Versions
        │
        ▼
Restore Previous Version
```

---

## 🌍 Real-World Applications

- Enterprise ETL Development
- Data Pipeline Versioning
- Team Collaboration
- Backup and Recovery
- Production Change Management
- CI/CD for Data Engineering

---

## 📁 Sample Exercise

Students will:

- Install Apache NiFi Registry.
- Connect NiFi with the Registry.
- Create a Bucket.
- Publish a Process Group.
- Create multiple versions.
- Restore an earlier version.
- Configure Git persistence.

---

## 📌 Expected Outcome

After completing this experiment, students will be able to configure Apache NiFi Registry, version data pipelines, compare different versions, restore previous versions, and understand how version control improves the reliability and maintainability of Data Engineering workflows.

---

## 📖 References

1. Apache NiFi Documentation
2. Apache NiFi Registry Documentation
3. Apache Software Foundation Documentation
4. Git Documentation

---

## 👨‍🏫 Instructor

**Shravan Chandra Geerlapally**

Assistant Professor

---

## 📄 License

This repository is intended for educational purposes for the Data Engineering Laboratory course.

---

⭐ If this repository helps your learning, please consider starring the repository.
