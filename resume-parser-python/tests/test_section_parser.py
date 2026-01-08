import pytest
from parsers.section_parser import split_into_sections


def test_basic_section_split():
    text = """
    Skills
    Python
    Django

    Experience
    Software Engineer
    """

    sections = split_into_sections(text)

    assert "skills" in sections
    assert "experience" in sections
    assert "python" in sections["skills"].lower()
    assert "software engineer" in sections["experience"].lower()


def test_text_without_sections_goes_to_header():
    text = """
    John Doe
    john@example.com
    +91-XXXXXXXXXX
    """

    sections = split_into_sections(text)

    assert "header" in sections
    assert "john doe" in sections["header"].lower()


def test_case_insensitive_section_headers():
    text = """
    SKILLS
    Python

    EXPERIENCE
    Backend Developer
    """

    sections = split_into_sections(text)

    assert "skills" in sections
    assert "experience" in sections


def test_unknown_section_is_not_created():
    text = """
    Interests
    Reading books
    """

    sections = split_into_sections(text)

    # "interests" is not in SECTION_HEADERS
    assert "interests" not in sections
    assert "header" in sections
