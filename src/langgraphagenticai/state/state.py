from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    State class to manage the state of the LangGraph Agentic AI application.
    This class is used to store and retrieve messages in the graph.
    """
    messages: Annotated[List, add_messages]