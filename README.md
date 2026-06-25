# 🚀 CareerAI - Intelligent Career Recommendation Platform

An AI-powered career platform that analyzes resumes and recommends personalized job opportunities using OpenAI LLMs, Groq, and JSearch API scraping.

---

## 🛠️ Setup & Installation

### 1. Install Dependencies
Ensure you have Python installed, then run the following command to install all the dependencies:
```bash
pip install -r Requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory by copying the template file:
```bash
cp .env.example .env
```

Open the newly created `.env` file and configure the required environment variables:
```env
# Required for AI Resume Analysis and Job Recommendation Generation
OPENAI_API_KEY=your_openai_api_key_here

# Optional fallback for Llama-3.3-70b analysis model
GROQ_API_KEY=your_groq_api_key_here

# Required for JSearch real-time job scraping
RAPIDAPI_KEY=your_rapidapi_key_here
```

### 3. Run the Application
Run the Streamlit application using the command below:
```bash
streamlit run app.py
```

---

## 🔑 Environment Variables Required

The application relies on the following environment variables:

| Variable Name | Description | Required | Format |
|---|---|---|---|
| `OPENAI_API_KEY` | Key for GPT-4o-mini used for resume analysis and job matching. | **Yes** | `sk-proj-...` |
| `GROQ_API_KEY` | Key for fallback analysis using Llama 70B model. | No | `gsk_...` |
| `RAPIDAPI_KEY` | Key for fetching real-time job listings via the JSearch API. | No (Recommended) | `656f457a78m...` |

---

## 📦 Project Structure

```
Intelligent-Career-Recommendation-Platform/
├── app.py                  # Main Streamlit entry point
├── Requirements.txt        # Python dependencies
├── users.json              # Auto-generated user database
├── .env                    # Local environment variables (git-ignored)
├── .env.example            # Environment variables template
└── pages/
    ├── Auth.py             # Login & Registration
    ├── Dashboard.py        # Home dashboard overview
    ├── Resume.py           # Resume upload & parsing
    ├── Insights.py         # AI Resume Analysis
    ├── Jobs.py             # Job recommendation engine
    └── Settings.py         # API keys & connection status
```

---

## 🧩 Key Features

- **Resume Upload & Parsing**: Support for PDF resume parsing and text extraction.
- **AI-Powered Insights**: Actionable recommendations, strengths/gaps identification, ATS compatibility score.
- **Job Recommendations**: Tailored job matching using real-time job listing aggregators.
- **Secure Authentication**: Local profile database with hashed passwords.
