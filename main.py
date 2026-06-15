import os
import uuid

from langchain_core.runnables import RunnableConfig
from src.agent.graph import agent
from src.utils import save_graph, import_dataset

save_graph(agent)

data_dir = "./gaia_data"
dataset = import_dataset(data_dir)

# get 1 random line in the dataset
dataset = dataset.shuffle(seed=42).select(range(1))


for i, example in enumerate(dataset):  # type: ignore
    example: dict = example
    question = example["Question"]
    answer = example["Final answer"]
    file = example["file_path"] if example["file_path"] else None
    if file:
        file = os.path.join(data_dir, file)

    message_invoke = (
        f"Question: {question}\n {f'File Path: {file}' if file else 'No file provided'}"
    )

    # Use a thread_id to track execution in LangGraph Studio
    thread_id = f"example_{i}_{uuid.uuid4().hex[:8]}"
    config: RunnableConfig = {"configurable": {"thread_id": thread_id}}

    print("============================================")
    print(f"Question: {question}")
    print("File Path:", file if file else "No file provided")
    print("Answer:")
    response = agent.invoke(
        {"messages": [{"role": "user", "content": message_invoke}]}, config
    )
    # print(
    #     "Structured Response:", response["structured_response"]
    # )  # Answer(answer=..., confidence=...)

    message = response["messages"][-1].content
    print(f" Response: {message}")

    print(f"Expected Answer: {answer[:50]}")
    print(f"Thread ID (visible in Studio): {thread_id}")
    if answer == message:
        print("✅ Correct answer!\n")
    else:
        print("❌ Incorrect answer.\n")
