# ScholarPath AI — Build Log

## Day 1 — Environment Setup
- Created GitHub repo `scholarpath-ai`
- Opened GitHub Codespaces as the dev environment (no local storage used)
- Created virtual environment (`venv`) and activated it
- Installed core dependencies: fastapi, uvicorn, sqlalchemy, psycopg2-binary, 
  python-jose, passlib[bcrypt], alembic, python-dotenv
- Created Neon (neon.tech) PostgreSQL project `scholarpath` (AWS US East 2, Postgres 18)
- Stored database connection string in `.env` (excluded from git via `.gitignore`)
- Verified database connection successfully via `app/database.py`

## Day 2 — Database Models
- Fixed indentation errors in `migrations/env.py` from copy-paste formatting
- Successfully ran first migration: created `users`, `user_profiles`, and 
  `scholarships` tables in Neon (migration id: a62f4274cfeb)
- Created `app/database.py`: SQLAlchemy engine, session, and Base setup
- Created `app/models/user.py`: `User` model (id, name, email, password_hash, created_at)
- Created `app/models/profile.py`: `UserProfile` model (academic info, preferences, 
  experience fields, tied to User via foreign key)
- Created `app/models/scholarship.py`: `Scholarship` model (name, university, country, 
  eligibility, deadlines, documents, etc.)
- Initialized Alembic for migrations (`alembic init migrations`)
