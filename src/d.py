from agent.tools import tools

from langchain_core.tools import (
    render_text_description,
    render_text_description_and_args,
)

# Simple
tools_description = render_text_description(tools)
print(tools_description)

# Avec les arguments
tools_with_args = render_text_description_and_args(tools)
print(tools_with_args)
