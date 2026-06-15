from PIL import Image
from io import BytesIO

from datasets import load_dataset
# from huggingface_hub import snapshot_download


def save_graph(agent):
    img = agent.get_graph().draw_mermaid_png()
    stream = BytesIO(img)
    image = Image.open(stream).convert("RGB")
    stream.close()
    image.save("graph.png")


def import_dataset(dir: str = "./gaia_data"):
    # dir = snapshot_download(
    #     repo_id="gaia-benchmark/GAIA", local_dir=dir, repo_type="dataset"
    # )
    return load_dataset(dir, "2023_level1", split="validation")
