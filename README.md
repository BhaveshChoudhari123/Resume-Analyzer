# 🚀 AI Resume Analyzer with RAG Chatbot

An AI-powered Resume Analyzer built using **Django**, **Groq LLM**, **FAISS**, and **PostgreSQL**. The application analyzes resumes, calculates ATS scores, recommends jobs, generates interview questions, provides AI-powered resume improvement suggestions, and includes a Retrieval-Augmented Generation (RAG) chatbot that answers questions based on the uploaded resume.

---

# 🌐 Live Demo

**Website:**
https://web-production-1c408.up.railway.app/accounts/login/

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

## Deployment

* Railway

---

```

---

# 🚀 Installation

Clone the repository

```bash
git clone (https://github.com/BhaveshChoudhari123/Resume-Analyzer)
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

---

# 📸 Screenshots

Add screenshots inside a folder named **screenshots**.

Example:

```
screenshots/
│
├── home.png
<img width="1918" height="1023" alt="home page" src="https://github.com/user-attachments/assets/cfedd218-0511-4870-9d1a-804f98625e01" />

├── login.png
<img width="1918" height="1020" alt="login" src="https://github.com/user-attachments/assets/f072a523-eb94-46f7-ae62-6c5ba9116382" />

├── register.png
<img width="1917" height="1012" alt="image" src="https://github.com/user-attachments/assets/45907ac8-1e9f-451c-84d7-a30d79b9e720" />

├── analysis.png
<img width="1918" height="1020" alt="analysis" src="https://github.com/user-attachments/assets/705c18c5-ecd1-4d09-9f36-61a50458e5f9" />

├── chatbot.png
<img width="1918" height="922" alt="chatbot" src="https://github.com/user-attachments/assets/f6948c67-d1e8-4862-90f5-484323ffb9bd" />

├── improvement.png
<img width="1918" height="1008" alt="improvement" src="https://github.com/user-attachments/assets/962b1acf-e75c-4d57-8eae-bea4060c92f1" />

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
* LinkedIn: https://www.linkedin.com/in/bhaveshchoudhari/
