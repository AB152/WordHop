import os
from llama_api_client import LlamaAPIClient
from pdf_to_text import pdf_to_text

client = LlamaAPIClient(
    api_key=os.environ.get("LLAMA_API_KEY"),  # This is the default and can be omitted
)

pdf_text = pdf_to_text("data/pdfs/book.pdf")

user_query = "Given this novel, generate 10 DALLE Prompts for images and tell me the best places in the novel to insert these images. " + pdf_text
model_name = "Llama-4-Maverick-17B-128E-Instruct-FP8"

create_chat_completion_response = client.chat.completions.create(
    messages=[
        {
            "content": user_query,
            "role": "user",
        }
    ],
    model=model_name,
)
print(create_chat_completion_response.completion_message)