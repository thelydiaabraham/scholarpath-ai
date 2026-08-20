from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Scholarship(Base):
    __tablename__ = "scholarships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    university = Column(String)
    country = Column(String)
    city = Column(String)
    degree_level = Column(String)
    field_of_study = Column(String)
    funding_type = Column(String)
    benefits = Column(String)
    eligibility = Column(String)
    min_gpa = Column(Float)
    english_requirement = Column(String)
    required_documents = Column(String)
    opening_date = Column(Date)
    deadline = Column(Date)
    duration = Column(String)
    official_url = Column(String)
    source_url = Column(String)
    last_updated = Column(Date)