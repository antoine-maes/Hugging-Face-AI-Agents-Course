from langchain.tools import tool
import whisper

_model = None


def _get_model():
    """Lazily load and cache the Whisper model so it's only loaded once."""
    global _model
    if _model is None:
        _model = whisper.load_model("base")
    return _model


@tool
def get_audio_file_transcription(file_path: str) -> str | list:
    """
    Transcribe an audio file (e.g., .mp3, .wav) to text using OpenAI's Whisper model.

    Args:
        file_path: Path to the audio file

    Returns:
        Transcribed text as a string
    """
    result = _get_model().transcribe(file_path)
    return result["text"]

