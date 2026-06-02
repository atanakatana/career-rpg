from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Character, CareerQuest
from services.gemini_ai import generate_character_blueprint
from services.mbti_engine import calculate_mbti
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Career Blueprint RPG API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class CharacterCreate(BaseModel):
    name: str
    current_job: str
    job_satisfaction: int
    kryptonite: str
    career_vision: str
    mbti_answers: list[int] # Array of 1-5 scores for 20 questions
    hd_type: str
    hd_authority: str
    hd_profile: str

@app.post("/api/character/forge")
def forge_character(char_in: CharacterCreate, db: Session = Depends(get_db)):
    # 1. Calculate MBTI
    mbti_result = calculate_mbti(char_in.mbti_answers)
    
    # 2. Setup Data for AI
    raw_data = char_in.dict()
    raw_data['mbti_result'] = mbti_result
    
    # 3. Consult Gemini Oracle
    ai_blueprint = generate_character_blueprint(raw_data)
    
    # 4. Save Character to DB
    db_char = Character(
        name=char_in.name,
        current_job=char_in.current_job,
        job_satisfaction=char_in.job_satisfaction,
        kryptonite=char_in.kryptonite,
        career_vision=char_in.career_vision,
        mbti_result=mbti_result,
        hd_type=char_in.hd_type,
        hd_authority=char_in.hd_authority,
        hd_profile=char_in.hd_profile,
        character_class=ai_blueprint.get('character_class'),
        archetype_desc=ai_blueprint.get('archetype_desc'),
        stat_wisdom=ai_blueprint['stats'].get('wisdom'),
        stat_leadership=ai_blueprint['stats'].get('leadership'),
        stat_creativity=ai_blueprint['stats'].get('creativity'),
        stat_empathy=ai_blueprint['stats'].get('empathy'),
        stat_execution=ai_blueprint['stats'].get('execution')
    )
    db.add(db_char)
    db.commit()
    db.refresh(db_char)
    
    # 5. Save Quests to DB
    for q in ai_blueprint.get('quests', []):
        db_quest = CareerQuest(
            character_id=db_char.id,
            title=q['title'],
            difficulty=q['difficulty'],
            income_potential=q['income_potential'],
            ai_resistance=q['ai_resistance'],
            why_you=q['why_you'],
            required_skills=q['required_skills']
        )
        db.add(db_quest)
    db.commit()
    
    return {"message": "Character Forged Successfully", "character_id": db_char.id}