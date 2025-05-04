from dotenv import load_dotenv
from llama_api_client import LlamaAPIClient
import os
import PyPDF2
import sys

file_name = sys.argv[1]

load_dotenv()
client = LlamaAPIClient()


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    text = ""
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
                
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")


system_prompt = "Read the text which follows the newline after the user's prompt. List the generated moods as text."
base_user_prompt = "Can you generate a list of moods on the content in each chapter?\n"

completion = client.chat.completions.create(
    model="Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=[
        # {
        #     "role": "system",
        #     "content": system_prompt
        # },
        {
            "role": "user",
            "content": base_user_prompt + "\n" + extract_text_from_pdf(file_name)
        },
    ],
    # response_format={
    #     "type": "json_schema",
    #     "json_schema": {
    #         "schema": {
    #             "type": "object",
    #             "required": ["moods"],
    #                 "properties": {
    #                 "moods": {
    #                     "type": "array",
    #                     "items": {
    #                         "type": "string",
    #                     },
    #                 }
    #             },
    #         }
    #     }
    # }
)

print(completion.completion_message)

