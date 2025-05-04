
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()



if __name__ == "__main__":
    # Example usage
    pdf_file = input("Enter the path to the PDF file: ")
    try:
        pdf_text = extract_text_from_pdf(pdf_file)
        print("\nExtracted Text:")
        print("-" * 50)
        print(pdf_text)
    except Exception as e:
        print(f"Error: {str(e)}")

