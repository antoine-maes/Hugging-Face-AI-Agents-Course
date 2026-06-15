from langchain.tools import tool
import whisper


@tool
def get_audio_file_transcription(file_path: str) -> str | list:
    """
    Transcribe an audio file (e.g., .mp3, .wav) to text using OpenAI's Whisper model.

    Args:
        file_path: Path to the audio file

    Returns:
        Transcribed text as a string
    """
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]
