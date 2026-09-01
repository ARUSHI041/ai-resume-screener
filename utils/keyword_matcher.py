import re


# Common technical and professional skills
KNOWN_SKILLS = [
    "python",
    "sql",
    "power bi",
    "excel",
    "tableau",
    "google sheets",
    "looker studio",
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "data analysis",
    "data analytics",
    "data visualization",
    "data cleaning",
    "data validation",
    "exploratory data analysis",
    "statistics",
    "business analysis",
    "business intelligence",
    "flask",
    "django",
    "html",
    "css",
    "javascript",
    "java",
    "c++",
    "git",
    "github",
    "mongodb",
    "mysql",
    "postgresql",
    "aws",
    "azure",
    "google cloud",
    "docker",
    "rest api",
    "api",
]


def normalize_text(text):
    """
    Convert text into a consistent lowercase format.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_keywords(text):
    """
    Extract known skills found in the given text.
    """

    normalized_text = normalize_text(text)

    found_skills = set()

    for skill in KNOWN_SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, normalized_text):
            found_skills.add(skill)

    return found_skills


def get_matching_score(resume_text, jd_text):
    """
    Compare resume skills with job description skills
    and calculate a keyword-based matching score.
    """

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    if not jd_keywords:
        return 0, [], []

    matched_keywords = sorted(
        resume_keywords.intersection(jd_keywords)
    )

    unmatched_keywords = sorted(
        jd_keywords - resume_keywords
    )

    match_score = round(
        (len(matched_keywords) / len(jd_keywords)) * 100,
        2
    )

    return (
        match_score,
        matched_keywords,
        unmatched_keywords
    )