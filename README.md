# 🚀 AI Resume Analyzer with RAG Chatbot

An AI-powered Resume Analysis Platform built using Django, Groq AI, LangChain, FAISS, and Sentence Transformers.

The system analyzes resumes, calculates ATS scores, identifies missing skills, recommends job roles, generates interview questions, creates PDF reports, and includes a RAG-powered chatbot that can answer questions about any uploaded resume.

---

## 📌 Features

### 🤖 AI Resume Analysis
- Resume Score Calculation
- ATS Score Evaluation
- Resume Level Detection
- Resume Summary Generation

### 💻 Skill Analysis
- Extract Skills from Resume
- Detect Missing Skills
- Suggest Skill Improvements
- Strength & Weakness Analysis

### 🎯 Career Guidance
- Recommended Job Roles
- Personalized Suggestions
- Technical Interview Questions

### 📄 PDF Report Generator
- Download Complete Analysis Report
- Professional PDF Format

### 🔐 User Authentication
- User Registration
- Login & Logout
- Resume History Tracking

### 🧠 RAG Resume Chatbot
- Ask questions about uploaded resumes
- Semantic Search using FAISS
- Resume Embeddings using Sentence Transformers
- Context-Aware Responses using Groq LLM

Examples:

- What projects has the candidate built?
- What skills are mentioned?
- What is the educational background?
- What technologies has the candidate used?
- Summarize the resume

---

##Images:

1.Login Page:

<img width="1918" height="1025" alt="login page" src="https://github.com/user-attachments/assets/a2138ea5-25bf-40ea-b2af-dade767ad50e" />

2.Forgotten Password reset:

<img width="1918" height="1017" alt="forgot password" src="https://github.com/user-attachments/assets/c741a182-7655-4571-b02d-ec215b2891a3" />

3.Dashboard:

<img width="1918" height="1013" alt="dashboard" src="https://github.com/user-attachments/assets/98da34eb-46c6-4648-8e2a-e1c75fa103d3" />

4.Resume score, Detected skills, Missing skills, recommended jobs, interview questions, strengths, weaknesses, suggestions, AI job matcher showing all these after uploading resume:

<img width="1918" height="1020" alt="resume score" src="https://github.com/user-attachments/assets/9f80ebe9-77b3-48af-92e9-e0556f639ef0" />

5.AI chatbot- Resume related questions:

<img width="1918" height="1017" alt="Rag chatbot" src="https://github.com/user-attachments/assets/9e36a911-2441-43d0-9945-80a7f2983c16" />





## 🏗️ Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- Bootstrap

### Database
- SQLite (Development)
- PostgreSQL (Deployment Ready)

### AI & RAG
- Groq API
- LangChain
- FAISS
- Sentence Transformers
- all-MiniLM-L6-v2

### Reports
- ReportLab PDF Generator

### Authentication
- Django Authentication System

---

## 🧠 RAG Architecture

Resume PDF
↓
Text Extraction
↓
Text Chunking
↓
Sentence Embeddings
↓
FAISS Vector Database
↓
Semantic Search
↓
Groq LLM
↓
Answer Generation

---

## 📂 Project Structure

```text
resume_analyzer/
│
├── accounts/
├── analyzer/
│   ├── ai_engine.py
│   ├── rag_engine.py
│   ├── pdf_generator.py
│   ├── views.py
│   └── models.py
│
├── templates/
├── media/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a .env file

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 🚀 Run Project

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## 📈 Future Enhancements

- Multi Resume Comparison
- Resume vs Job Description Matching
- AI Cover Letter Generator
- LinkedIn Profile Analyzer
- Resume Ranking System
- Recruiter Dashboard
- PostgreSQL Production Database
- Docker Deployment

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python Development
- Django Development
- Authentication System
- REST Concepts
- AI Integration
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Prompt Engineering
- PDF Generation
- Full Stack Development

---

## 👨‍💻 Author

Bhavesh Choudhari

Python Developer | Backend Developer

LinkedIn:
[https://linkedin.com/in/bhaveshchoudhari](https://www.linkedin.com/in/bhaveshchoudhari/)

GitHub:
[https://github.com/bhaveshchoudhari](https://github.com/BhaveshChoudhari123?tab=repositories)

---
