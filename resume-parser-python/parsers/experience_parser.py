def extract_experience(text: str):
    lines = text.splitlines()
    return [line for line in lines if line.strip()]
