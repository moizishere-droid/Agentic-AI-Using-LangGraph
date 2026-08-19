from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
from typing import Annotated,TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


load_dotenv()
model = ChatOpenAI()

class ChatbotState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]
    
def chat_node(state:ChatbotState):
    messages = state['messages']
    response = model.invoke(messages)
    return {"messages":[response]}

checkpointer = InMemorySaver()

graph = StateGraph(ChatbotState)

graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=checkpointer)