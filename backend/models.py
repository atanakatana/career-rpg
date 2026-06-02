from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    current_job = Column(String)
    job_satisfaction = Column(Integer)
    kryptonite = Column(Text)
    career_vision = Column(Text)
    
    # Assesssment Results
    mbti_result = Column(String)
    hd_type = Column(String)
    hd_authority = Column(String)
    hd_profile = Column(String)
    
    # AI Generated Stats
    character_class = Column(String)
    archetype_desc = Column(Text)
    stat_wisdom = Column(Integer)
    stat_leadership = Column(Integer)
    stat_creativity = Column(Integer)
    stat_empathy = Column(Integer)
    stat_execution = Column(Integer)

    quests = relationship("CareerQuest", back_populates="character")

class CareerQuest(Base):
    __tablename__ = "career_quests"
    
    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"))
    title = Column(String)
    difficulty = Column(String)
    income_potential = Column(String)
    ai_resistance = Column(String)
    why_you = Column(Text)
    required_skills = Column(String) # Disimpan sebagai comma-separated string untuk demo

    character = relationship("Character", back_populates="quests")