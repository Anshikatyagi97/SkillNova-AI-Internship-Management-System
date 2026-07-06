# SkillNova — AI-Powered Internship Management & Mentor Intelligence System

> ⚠️ **This is a STARTER TEMPLATE, not a finished project.**
> The project runs out of the box and returns dummy/placeholder data.
> All AI logic is intentionally left as `TODO` sections for interns to implement.

## 1. Project Overview

This backend module assists mentors, team leads, administrators, and interns
by automating internship monitoring, analysing student progress, generating
AI-based insights, and improving overall internship management for the
**SkillNova Internship Platform**.

The system is a collection of **AI-powered backend services** (FastAPI) that
will later be integrated into the main SkillNova web application, which is
built and owned separately by the Web Development team. Interns on this
project build **backend APIs only** — a minimal Streamlit app is included
purely for local testing, not as the production frontend.

### Modules
| # | Module | Status |
|---|--------|--------|
| 1 | AI Internship Progress Tracker | 🟡 Skeleton only — logic is TODO |
| 2 | AI Mentor Dashboard | 🟡 Skeleton only — logic is TODO |
| 3 | AI Attendance & Performance Analyzer | 🟡 Skeleton only — logic is TODO |
| 4 | AI Task Recommendation System | 🟡 Skeleton only — logic is TODO |
| 5 | AI GitHub & Code Review Assistant | 🟡 Skeleton only — logic is TODO |
| 6 | AI Certificate Eligibility Analyzer | 🟡 Skeleton only — logic is TODO |
| 7 | AI Internship Analytics Dashboard | 🟡 Skeleton only — logic is TODO |

## 2. Folder Structure

```
AI_Internship_Management_System/
│
├── backend/                      # FastAPI backend
│   ├── api/
│   │   ├── routes/               # One router file per module
│   │   └── schemas/              # Shared Pydantic response models
│   ├── config/                   # Environment-driven settings
│   ├── database/                 # SQLAlchemy engine/session + init script
│   ├── models/                   # SQLAlchemy ORM models
│   ├── services/                 # Bridges routes <-> ai_modules (dummy data for now)
│   ├── utils/                    # Logger, response helpers
│   └── main.py                   # FastAPI app entry point
│
├── ai_modules/                    # AI logic lives here — mostly TODOs
│   ├── progress_tracker/
│   ├── mentor_dashboard/
│   ├── attendance_analyzer/
│   ├── task_recommender/
│   ├── github_analyzer/
│   ├── certificate_analyzer/
│   └── analytics_dashboard/
│   (each folder: service.py, utils.py, README.md)
│
├── datasets/                      # Sample fake CSV data + generator script
│   ├── interns.csv
│   ├── tasks.csv
│   ├── attendance.csv
│   ├── submissions.csv
│   ├── mentor_feedback.csv
│   ├── github_activity.csv
│   ├── certificates.csv
│   └── generate_datasets.py
│
├── frontend/                      # Minimal Streamlit app (for testing only)
│   ├── streamlit_app.py
│   ├── pages/
│   └── utils/
│
├── reports/                       # Put your project report here
├── screenshots/                   # Put your submission screenshots here
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md                      # You are here
```

## 3. Technologies Used

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI, Pydantic |
| Database | SQLAlchemy ORM + SQLite (swap to PostgreSQL if needed) |
| AI / ML | Scikit-learn, pandas, numpy |
| LLM / RAG | LangChain, Gemini API / Groq, ChromaDB / FAISS |
| Frontend (testing only) | Streamlit |
| Tooling | Git, GitHub, Docker (optional) |

## 4. Installation Guide

### Prerequisites
- Python 3.10+
- pip

### Steps
```bash
# 1. Clone the repository
git clone <your-repo-url>
cd AI_Internship_Management_System

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# then edit .env with your own values (API keys, DB URL, etc.)

# 5. (Optional) Regenerate sample datasets
python datasets/generate_datasets.py

# 6. Initialize the database (creates tables + seeds interns.csv)
python -m backend.database.init_db
```

## 5. Running the Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

- API base URL: `http://127.0.0.1:8000`
- Interactive Swagger docs: `http://127.0.0.1:8000/docs`
- Health check: `GET /health`

### Available Endpoints (all currently return dummy data)

| Method | Endpoint | Module |
|---|---|---|
| GET | `/api/progress/{intern_id}` | Progress Tracker |
| GET | `/api/progress/inactive/list` | Progress Tracker |
| GET | `/api/mentor-dashboard` | Mentor Dashboard |
| GET | `/api/attendance/{intern_id}` | Attendance Analyzer |
| GET | `/api/task-recommendations/{intern_id}` | Task Recommender |
| POST | `/api/github-analysis` | GitHub Analyzer |
| GET | `/api/certificate/{intern_id}` | Certificate Analyzer |
| GET | `/api/analytics` | Analytics Dashboard |

## 6. Running the Frontend (for testing)

In a **second terminal**, with the backend already running:

```bash
cd frontend
streamlit run streamlit_app.py
```

This opens a minimal multi-page app you can use to manually exercise each
API while you build out the real logic. It is **not** the production
SkillNova frontend.

## 7. What You Need To Implement (TODO Features)

Every AI module under `ai_modules/` contains a `service.py` with empty
function stubs and detailed TODO comments. At a high level, you'll need to:

- **Progress Tracker** — completion %, slow-progress prediction, inactivity
  detection, AI-generated progress summaries, next-task suggestions.
- **Mentor Dashboard** — real aggregate stats, top/weak performer ranking,
  AI-generated alerts and mentor recommendations.
- **Attendance Analyzer** — attendance %, consecutive absence detection,
  attendance-drop prediction, consistency scoring, heatmap data.
- **Task Recommender** — weak-skill detection, personalized task/course
  recommendations (optionally RAG-based using ChromaDB/FAISS).
- **GitHub Analyzer** — GitHub API integration, README/code quality
  scoring, actionable Git-practice suggestions.
- **Certificate Analyzer** — weighted eligibility decision logic and
  natural-language explanations.
- **Analytics Dashboard** — platform-wide aggregates, domain distribution,
  mentor workload, health score, AI-generated weekly/batch reports.

Each `ai_modules/<module>/README.md` includes a suggested implementation
approach (start rule-based, then layer AI/LLM on top).

## 8. Suggested Implementation Order

1. Get comfortable with the dummy data flow: Route → Service → AI module stub.
2. Implement rule-based / statistical logic first (pandas, SQL queries).
3. Layer in Scikit-learn models where prediction is genuinely needed
   (e.g. slow-progress prediction, attendance-drop prediction).
4. Layer in LLM calls (Gemini/Groq via LangChain) for natural-language
   summaries, alerts, and explanations.
5. Add a RAG pipeline (ChromaDB/FAISS) only for the Task Recommender's
   learning-resource suggestions, if time allows.

## 9. Future Work

- Authentication / authorization (JWT) before integration with SkillNova.
- Migrate from SQLite to PostgreSQL for production.
- Add background/scheduled jobs (e.g. nightly analytics snapshot generation).
- Add automated tests (pytest) for each service and AI module.
- Containerize with Docker for consistent deployment.
- Replace the testing Streamlit frontend’s placeholder data once every
  endpoint returns real values.

## 10. Deliverables Checklist

- [ ] Complete source code
- [ ] README.md (this file, plus any module-level notes you add)
- [ ] requirements.txt (kept up to date as you add dependencies)
- [ ] Project Report (in `reports/`)
- [ ] Screenshots (in `screenshots/`)
- [ ] GitHub Repository
- [ ] Demo Video (3–5 minutes)

## 11. Scope Boundary (Important)

The focus of this project is **AI-powered backend services and APIs only**.
Frontend implementation and platform integration into the live SkillNova
product will be handled separately by the Web Development team. Design
your modules so they can be integrated cleanly through REST APIs.
