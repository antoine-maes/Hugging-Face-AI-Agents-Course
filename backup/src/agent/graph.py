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
)


class Answer(BaseModel):
    answer: str
    confidence: float


agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=SystemMessage(content=format_system_prompt(tools)),
    response_format=Answer,
)


# def assistant(state: AgentState):
#     """Assistant node that processes messages and file_path"""
#     messages = state["messages"]
#     file_path = state.get("file_path")

#     # Add file context to system prompt if available
#     final_system_prompt = system_prompt
#     if file_path:
#         final_system_prompt += f"\n\n📄 File to analyze: {file_path}"

#     # Build message list with system prompt
#     formatted_messages = [SystemMessage(content=final_system_prompt), *messages]

#     response = model.invoke(formatted_messages)

#     print(response.content)

#     return {
#         "messages": [response],
#     }


# # Create the graph
# builder = StateGraph(AgentState)

# # Add nodes
# builder.add_node("assistant", assistant)
# builder.add_node("tools", ToolNode(tools))

# # Add edges
# builder.add_edge(START, "assistant")
# builder.add_conditional_edges(
#     "assistant",
#     tools_condition,
#     {"tools": "tools", "__end__": "__end__"},
# )
# builder.add_edge("tools", "assistant")

# # Compile the agent
# # LangGraph API handles persistence automatically
# agent = builder.compile()
