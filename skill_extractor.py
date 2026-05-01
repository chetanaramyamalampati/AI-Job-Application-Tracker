KNOWN_SKILLS = [
    "python", "sql", "power bi", "tableau", "excel", "aws", "azure", "gcp",
    "machine learning", "rag", "llm", "langchain", "fastapi", "spark",
    "snowflake", "databricks", "pandas", "numpy"
]

def extract_skills(job_description: str) -> list[str]:
    text = job_description.lower()
    return [skill for skill in KNOWN_SKILLS if skill in text]
