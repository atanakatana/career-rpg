import google.generativeai as genai
import os
import json

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_character_blueprint(character_data: dict) -> dict:
    prompt = f"""
    You are an AI Career Architect in a gamified RPG universe. Analyze the following user data and generate a Character Career Blueprint.
    
    User Data:
    - Name: {character_data['name']}
    - Current Job: {character_data['current_job']} (Satisfaction: {character_data['job_satisfaction']}/10)
    - Kryptonite (Energy Drainers): {character_data['kryptonite']}
    - Vision: {character_data['career_vision']}
    - MBTI: {character_data['mbti_result']}
    - Human Design: Type: {character_data['hd_type']}, Authority: {character_data['hd_authority']}, Profile: {character_data['hd_profile']}
    
    Translate their psychological profile into productivity and career terms.
    Return ONLY a valid JSON object with the following schema, no markdown blocks:
    {{
      "character_class": "e.g., The System Architect, The Catalyst Leader",
      "archetype_desc": "A brief, empowering description of their core identity.",
      "stats": {{
        "wisdom": int (1-100),
        "leadership": int (1-100),
        "creativity": int (1-100),
        "empathy": int (1-100),
        "execution": int (1-100)
      }},
      "quests": [
        {{
          "title": "Job Title",
          "difficulty": "Easy/Medium/Hard/Epic",
          "income_potential": "High/Medium/Low",
          "ai_resistance": "High/Medium/Low",
          "why_you": "Why this fits their MBTI & Human Design.",
          "required_skills": "Skill 1, Skill 2, Skill 3"
        }}
      ] # Provide exactly 3 quests
    }}
    """
    
    response = model.generate_content(prompt)
    try:
        # Strip markdown if Gemini accidentally includes it
        clean_json = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_json)
    except Exception as e:
        print("JSON Parsing Error:", e)
        return {} # Handle fallback in production