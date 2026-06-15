from langchain.tools import tool


@tool
def analyze_image(
    image_path: str, prompt: str = "Describe this image in detail:"
) -> str | None:
    """Analyze an image using LLaVA vision model"""
    import ollama

    with open(image_path, "rb") as f:
        image_data = f.read()

    response = ollama.generate(
        model="llava:7b",
        prompt=prompt,
        images=[image_data],
        stream=False,
    )
    return response.response
