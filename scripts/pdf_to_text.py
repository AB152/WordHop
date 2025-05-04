from pypdf import PdfReader

def pdf_to_text(path: str):
    pdf_path = path
    reader = PdfReader(pdf_path)

    all_text = ''
    for page in reader.pages:
        all_text += page.extract_text() + '\n'

    return all_text