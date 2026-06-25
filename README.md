# 🚀 AI Resume Analyzer with RAG Chatbot

An AI-powered Resume Analyzer built using **Django**, **Groq LLM**, **FAISS**, and **PostgreSQL**. The application analyzes resumes, calculates ATS scores, recommends jobs, generates interview questions, provides AI-powered resume improvement suggestions, and includes a Retrieval-Augmented Generation (RAG) chatbot that answers questions based on the uploaded resume.

---

# 🌐 Live Demo

**Website:**
https://YOUR-RAILWAY-URL.up.railway.app

---

# ✨ Features

* 👤 User Registration & Login
* 📄 Upload PDF Resume
* 🤖 AI Resume Analysis
* 📊 ATS Score Calculation
* ⭐ Resume Score
* 🧠 Skill Extraction
* ❌ Missing Skills Detection
* 💼 AI Job Recommendations
* 💪 Resume Strengths & Weaknesses
* 💡 AI Resume Improvement Suggestions
* 🎤 AI Interview Questions
* 🔍 RAG Resume Chatbot
* 📑 Download PDF Resume Report
* 📜 Resume History
* 🗄 PostgreSQL Database
* ☁ Railway Deployment

---

# 🛠 Tech Stack

## Backend

* Python
* Django
* Django REST Framework

## Artificial Intelligence

* Groq LLM
* RAG (Retrieval-Augmented Generation)
* FAISS Vector Database

## Database

* PostgreSQL

## Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

## Deployment

* Railway

---

# 📂 Project Structure

```text
Resume-Analyzer/
│
├── analyzer/
├── accounts/
├── resume_analyzer/
├── templates/
├── static/
├── media/
├── requirements.txt
├── runtime.txt
├── manage.py
├── README.md
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Resume-Analyzer.git
```

Move into the project

```bash
cd Resume-Analyzer
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root and add the following variables.

```env
SECRET_KEY=your_secret_key_here

DATABASE_URL=your_database_url_here

GROQ_API_KEY=your_groq_api_key_here

EMAIL_HOST_USER=your_email@example.com

EMAIL_HOST_PASSWORD=your_gmail_app_password_here

HF_API_TOKEN=your_huggingface_token_here
```

**⚠️ Never upload your real API keys or passwords to GitHub.**

---

# 📸 Screenshots

Add screenshots inside a folder named **screenshots**.

Example:

```
screenshots/
│
├── home.png
├── login.png
├── register.png
├── upload.png
├── analysis.png
├── chatbot.png
├── report.png
```

---

# 🚀 Future Improvements

* Voice AI Interview Assistant
* Resume Comparison
* AI Career Roadmap Generator
* Recruiter Dashboard
* Resume Version History
* Multi-language Resume Analysis

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Bhavesh Choudhari**

Aspiring Full Stack Python & AI Developer

* GitHub: https://github.com/BhaveshChoudhari123
* LinkedIn: *(Add your LinkedIn profile URL here)*
