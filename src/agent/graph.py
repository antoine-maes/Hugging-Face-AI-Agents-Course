import os
from azure.identity import DefaultAzureCredential
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage
from langchain.agents import create_agent
from pydantic import BaseModel
from dotenv import load_dotenv

from src.agent.prompt import format_system_prompt
from src.agent.tools import tools

load_dotenv()

# model = ChatOllama(model="qwen2:7b", base_url="http://localhost:11434", verbose=True)

model = ChatOpenAI(
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"], # type: ignore
    model="DeepSeek-V4-Flash",
    max_completion_tokens=16000,
    temperature=0.0,
    top_p=1.0,
)


agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=SystemMessage(content=format_system_prompt(tools)),
)