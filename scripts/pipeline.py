from translate import LlamaTranslator
from stt import ElevenLabsTranscriber
from record import record_audio


def translate_user_audio():
    record_audio(duration=5)  # Records 5 seconds to input.mp3

    transcriber = ElevenLabsTranscriber()
    with open("input.mp3", "rb") as f:
        transcription = transcriber.client.speech_to_text.convert(
            file=f,
            model_id="scribe_v1",
            tag_audio_events=True,
            diarize=True
        ).text

    print(f"Transcription: {transcription}")

    translator = LlamaTranslator()
    translation = translator.translate(transcription)
    print(f"Translation: {translation}")
    return translation


if __name__ == "__main__":
    translate_user_audio()
