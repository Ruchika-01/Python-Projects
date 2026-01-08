import re
from typing import Dict

SECTION_HEADERS = [
    "education",
    "experience",
    "skills",
    "projects",
    "certifications"
]

def split_into_sections(text: str) -> Dict[str, str]:
    sections = {}
    current_section = "header"
    sections[current_section] = []

    for line in text.splitlines():
        clean = line.strip().lower()
        if clean in SECTION_HEADERS:
            current_section = clean
            sections[current_section] = []
        else:
            sections[current_section].append(line)

    return {k: "\n".join(v).strip() for k, v in sections.items()}
