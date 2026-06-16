import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_resume_data(text):
    data = {}

    # Email
    email = re.findall(r'\S+@\S+', text)
    data["email"] = email[0] if email else None

    # Phone
    phone = re.findall(r'\b\d{10}\b', text)
    data["phone"] = phone[0] if phone else None

    # NLP processing
    doc = nlp(text)

    # Name (first PERSON entity)
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break
    data["name"] = name

    # Skills (simple rule-based)
    skills_list = [
        "python", "java", "machine learning", "nlp",
        "c++", "sql", "javascript"
    ]

    found_skills = []
    text_lower = text.lower()
    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill)

    data["skills"] = found_skills

    return data
