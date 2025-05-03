import os
from dotenv import load_dotenv
from openai import OpenAI


class LlamaTranslator:
    def __init__(self, api_key=None, base_url="https://api.sambanova.ai/v1",):
        load_dotenv()  # Load environment variables from .env
        self.client = OpenAI(
            api_key=api_key or os.environ.get("SAMBA_NOVA_KEY"),
            base_url=base_url
        )

    def translate(self, text):
        response = self.client.chat.completions.create(
            model="Llama-4-Maverick-17B-128E-Instruct",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a translator who translates any input I give you into English, "
                        "no matter the input. If the input is in English, the output should equal the input. "
                        "The output should only include the raw translation."
                    )
                },
                {"role": "user", "content": text}
            ],
        )
        return response.choices[0].message.content


# Example usage
if __name__ == "__main__":
    translator = LlamaTranslator()
    result = translator.translate("Kya aapake paas kamare upalabdh hain?")
    print(result)
