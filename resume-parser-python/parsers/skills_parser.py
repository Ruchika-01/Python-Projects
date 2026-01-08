import re

COMMON_SKILLS = [
    "python", "django", "flask", "sql",
    "git", "docker", "rest", "linux"
]

def extract_skills(text: str):
    found = set()
    text = text.lower()
    for skill in COMMON_SKILLS:
        if re.search(rf"\b{skill}\b", text):
            found.add(skill)
    return sorted(found)
