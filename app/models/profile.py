from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.database import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    degree = Column(String)
    university = Column(String)
    cgpa = Column(Float)
    graduation_year = Column(Integer)
    preferred_countries = Column(String)
    preferred_courses = Column(String)
    work_experience = Column(String)
    leadership = Column(String)
    volunteering = Column(String)
    research_experience = Column(String)
    publications = Column(String)
    ielts_status = Column(String)
    budget = Column(String)