from core.pipeline import parse_resume
import json

def pretty_print(result: dict):
    print("Skills:")
    for skill in result.get("skills", []):
        print(f"  - {skill}")

    print("\nExperience:")
    for line in result.get("experience", []):
        print(f"  {line}")

    print("\nEducation:")
    print(result.get("education", ""))


if __name__ == "__main__":
    result = parse_resume("sample_resume.pdf")
    pretty_print(result)

