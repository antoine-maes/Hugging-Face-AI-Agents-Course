from azure.identity import DefaultAzureCredential
from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage
from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel

from src.agent.prompt import format_system_prompt
from src.agent.tools import tools

import os

from dotenv import load_dotenv

load_dotenv()

# model = ChatOllama(model="qwen2:7b", base_url="http://localhost:11434", verbose=True)

model = AzureAIOpenAIApiChatModel(
    endpoint=os.environ["OPENAI_BASE_URL"],
    credential=DefaultAzureCredential(),
    model="DeepSeek-V4-Flash",
    max_completion_tokens=16000,
    temperature=0.0,
    top_p=1.0,
    model_kwargs={"top_k": 1},
    verbosity="medium"
)


# class Answer(BaseModel):
#     answer: str
#     confidence: float


agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=SystemMessage(content=format_system_prompt(tools)),
)