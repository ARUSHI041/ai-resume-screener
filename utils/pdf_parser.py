import fitz


def extract_text_from_pdf(pdf_path):
    """
    Extract text from all pages of a PDF file.
    Returns the extracted text as a string.
    """

    text = ""

    try:
        with fitz.open(pdf_path) as document:

            for page in document:
                page_text = page.get_text()

                if page_text:
                    text += page_text + "\n"

    except (fitz.FileDataError, OSError) as error:
        print(f"Error reading PDF: {error}")
        return ""

    except Exception as error:
        print(f"Unexpected PDF parsing error: {error}")
        return ""

    return text.strip()