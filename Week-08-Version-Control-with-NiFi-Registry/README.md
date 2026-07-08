# Week 08 – Version Control with Apache NiFi Registry

## Experiment Title

**Version Control with Apache NiFi Registry**

---

## 📖 Introduction

Apache NiFi Registry is a companion application for Apache NiFi that provides version control for data flows. It enables developers and data engineers to save, manage, compare, and restore different versions of NiFi flows. This makes collaboration easier and ensures that changes can be tracked over time.

Version control is an essential practice in Data Engineering because it helps teams maintain consistency, recover previous versions, and safely deploy data pipelines.

---

## 🎯 Objectives

After completing this experiment, students will be able to:

- Understand the purpose of Apache NiFi Registry.
- Install and configure NiFi Registry.
- Connect Apache NiFi with NiFi Registry.
- Create and save versioned flows.
- Update and manage different versions of a flow.
- Restore previous versions of a data flow.
- Understand collaborative development using version control.

---

## 🎓 Learning Outcomes

Students will be able to:

- Configure NiFi Registry.
- Publish a process group to the Registry.
- Manage multiple versions of a data pipeline.
- Compare flow versions.
- Restore previous versions when required.

---

## 🛠 Software Required

- Apache NiFi
- Apache NiFi Registry
- Java JDK 17 or later
- Web Browser
- VS Code (Optional)

---

## 📚 Concepts Covered

- Apache NiFi Registry
- Version Control
- Buckets
- Flows
- Process Groups
- Flow Snapshot
- Commit
- Restore
- Synchronization
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
NiFi Registry
     │
     ▼
Version History
     │
     ▼
Restore / Compare / Update
```

---

## 📂 Folder Structure

```text
Week-08-Version-Control-with-NiFi-Registry/
│
├── README.md
├── Theory.md
├── Faculty-Notes.md
├── Student-Notes.md
├── Installation-Guide.md
├── Assignments.md
├── Viva.md
│
├── Programs/
│   ├── README.md
│   ├── Program-01-Install-NiFi-Registry.md
│   ├── Program-02-Connect-NiFi-Registry.md
│   ├── Program-03-Create-Bucket.md
│   ├── Program-04-Version-a-Process-Group.md
│   ├── Program-05-Update-Flow-Version.md
│   └── Program-06-Restore-Previous-Version.md
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
| Program-01 | Install Apache NiFi Registry |
| Program-02 | Connect Apache NiFi to NiFi Registry |
| Program-03 | Create a Bucket |
| Program-04 | Version a Process Group |
| Program-05 | Update a Flow Version |
| Program-06 | Restore a Previous Version |

---

## 🔄 Workflow

```text
Create Flow
      │
      ▼
Publish Process Group
      │
      ▼
Save to NiFi Registry
      │
      ▼
Create New Version
      │
      ▼
Compare Versions
      │
      ▼
Restore Previous Version
```

---

## 🌍 Real-World Applications

- Enterprise Data Pipeline Management
- Team Collaboration
- Production Change Management
- Backup and Recovery
- Data Pipeline Auditing
- CI/CD for Data Engineering

---

## 📌 Expected Outcome

After completing this experiment, students will be able to configure Apache NiFi Registry, publish version-controlled process groups, manage multiple versions of a data flow, and restore previous versions when required.

---

## 📖 References

1. Apache NiFi Documentation
2. Apache NiFi Registry Documentation
3. Apache Software Foundation Documentation

---

## 👨‍🏫 Instructor

**Shravan Chandra Geerlapally**

Assistant Professor

---

⭐ If this repository helps your learning, please consider starring the repository.
