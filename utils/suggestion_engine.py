def get_missing_keywords(unmatched_keywords, jd_text):
    """
    Generate resume improvement suggestions
    based on skills missing from the resume.
    """

    suggestions = []

    jd_text_lower = jd_text.lower()

    for keyword in unmatched_keywords:

        if keyword.lower() in jd_text_lower:
            suggestions.append(
                f"Consider adding: {keyword}"
            )

    if not suggestions:
        suggestions.append(
            "Your resume covers the identified job requirements."
        )

    return suggestions