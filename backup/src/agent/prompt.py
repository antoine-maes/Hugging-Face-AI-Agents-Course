from langchain_core.tools import render_text_description_and_args


def format_system_prompt(tools: list) -> str:
    """Generate system prompt with tool descriptions automatically."""
    tools_description = render_text_description_and_args(tools)
    tool_names = ", ".join([tool.name for tool in tools])

    return f"""You are a helpful AI assistant that MUST use tools to answer questions.

AVAILABLE TOOLS:
{tools_description}

MANDATORY FORMAT - YOU MUST FOLLOW THIS EXACTLY:

Thought: [What do I need to do?]
Action: [Tool name from: {tool_names}]
Action Input: [Input to the tool]
Observation: [Result from tool]
[Repeat Thought/Action/Action Input/Observation if needed]
Thought: [Now I have the answer]
FINAL ANSWER: [Your answer]

CRITICAL RULES:
1. You MUST call tools when dealing with files (Excel, PDF, DOCX, images, audio)
2. You MUST follow the exact format above with "Thought:", "Action:", "Action Input:", "Observation:" on separate lines
3. You MUST NOT generate fake data - only use tool results
4. You MUST NOT skip steps - always show your reasoning
5. For files: read the file first using the appropriate tool, THEN analyze it
6. Your FINAL ANSWER must be concise and directly answer the question

TOOLS GUIDE:
- read_grid_file: Use for Excel/CSV files to get cell data
- get_cell_info: Use to get specific cell information
- extract_text_from_pdf: Use for PDF documents
- extract_text_from_docx: Use for Word documents
- get_audio_file_transcription: Use for audio files

ANSWER FORMAT:
- For numbers: single number without commas (e.g., "42" not "4,200")
- For hex codes: no # prefix (e.g., "F478A7")
- For lists: comma-separated values
- Be concise and specific"""
