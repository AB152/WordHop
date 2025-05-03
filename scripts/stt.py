# transcriber.py

import os
from dotenv import load_dotenv
from io import BytesIO
import requests
from elevenlabs.client import ElevenLabs

class ElevenLabsTranscriber:
    def __init__(self, api_key=None):
        load_dotenv()
        self.client = ElevenLabs(
            api_key=api_key or os.getenv("ELEVENLABS_API_KEY")
        )

    def transcribe_from_url(self, audio_url, language_code="eng"):
        response = requests.get(audio_url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch audio from URL: {audio_url}")
        audio_data = BytesIO(response.content)

        transcription = self.client.speech_to_text.convert(
            file=audio_data,
            model_id="scribe_v1",
            tag_audio_events=True,
            language_code=language_code,
            diarize=True,
        )

        return transcription.text


# Example usage
if __name__ == "__main__":
    transcriber = ElevenLabsTranscriber()
    url = "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
    result = transcriber.transcribe_from_url(url)
    print(result)
