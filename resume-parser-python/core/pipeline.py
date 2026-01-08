from loaders.pdf_loader import load_pdf
from loaders.docx_loader import load_docx
from parsers.section_parser import split_into_sections
from parsers.skills_parser import extract_skills
from parsers.experience_parser import extract_experience

def parse_resume(path: str):
    if path.endswith(".pdf"):
        raw_text = load_pdf(path)
    elif path.endswith(".docx"):
        raw_text = load_docx(path)
    else:
        raise ValueError("Unsupported file format")

    sections = split_into_sections(raw_text)

    return {
        "skills": extract_skills(sections.get("skills", "")),
        "experience": extract_experience(sections.get("experience", "")),
        "education": sections.get("education", "")
    }
