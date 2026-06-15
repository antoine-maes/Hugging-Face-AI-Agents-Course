from langchain_community.tools import (
    DuckDuckGoSearchRun,
    WikipediaQueryRun,
    YouTubeSearchTool,
)
import wikipedia
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

from .audio import get_audio_file_transcription
from .tabular import read_grid_file, get_cell_info
from .text import extract_text_from_pdf, extract_text_from_docx
from .math import add, subtract, multiply, divide, round_number


# Web search tool
search_tool = DuckDuckGoSearchRun()


# Wrapped Wikipedia tool with error handling
class RobustWikipediaQueryRun(WikipediaQueryRun):
    def _run(self, query: str) -> str:
        """Run with error handling for JSON decode errors"""
        try:
            return super()._run(query)
        except Exception as e:
            # If Wikipedia fails, use DuckDuckGo instead
            return (
                f"Wikipedia temporarily unavailable. Try searching '{query}' directly."
            )


wikipedia_tool = RobustWikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        wiki_client=wikipedia, top_k_results=1, doc_content_chars_max=500
    )
)

# YouTube search tool
youtube_tool = YouTubeSearchTool()


tools = [
    search_tool,
    wikipedia_tool,
    youtube_tool,
    read_grid_file,
    get_cell_info,
    extract_text_from_pdf,
    extract_text_from_docx,
    get_audio_file_transcription,
    add,
    subtract,
    multiply,
    divide,
    round_number,
]

__all__ = [
    "tools",
    "search_tool",
    "wikipedia_tool",
    "youtube_tool",
    "read_grid_file",
    "get_cell_info",
    "extract_text_from_pdf",
    "extract_text_from_docx",
    "get_audio_file_transcription",
    "add",
    "subtract",
    "multiply",
    "divide",
    "round_number",
]
