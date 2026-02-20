from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Literal,Annotated
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

load_dotenv()

from langgraph.graph.message import add_messages 
class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage],add_messages]


model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


def chat_node(state: ChatState):
    
    messages = state['messages']

    response = model.invoke(messages)

    return {'messages' :[response]}


conn = sqlite3.connect(database='chatbot.db',check_same_thread = False)
checkpointer = SqliteSaver()
graph = StateGraph(ChatState)

graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

Chatbot = graph.compile(checkpointer = checkpointer)

all_threads = set()

def retrieve_all_thread():
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)

