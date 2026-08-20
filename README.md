# ScholarPath AI

AI-powered scholarship discovery and study-abroad planning platform.

## Overview
ScholarPath AI helps students discover scholarships, understand their competitiveness, 
improve application materials (CV, personal statement), and organize their study-abroad 
journey — all in one platform.

## Tech Stack
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL (hosted on Neon)
- **ORM:** SQLAlchemy + Alembic (migrations)
- **AI:** LLM API (CV review, match scoring, readiness feedback, timeline generation)
- **Deployment:** Render/Railway (planned)
- **Dev environment:** GitHub Codespaces (cloud-based, no local install)

## Project Status
🚧 In active development — Week 1 (Foundation)

## Setup
1. Clone the repo / open in Codespaces
2. Create a virtual environment: `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file with `DATABASE_URL=<your Neon connection string>`
5. Run migrations: `alembic upgrade head`
6. Start the server: `uvicorn app.main:app --reload`

## Roadmap
- Week 1: Auth + user profiles
- Week 2: Scholarship search, save, tracking
- Week 3: AI features (match score, CV review, personal statement coach)
- Week 4: Polish + testing
- Week 5: Deployment
