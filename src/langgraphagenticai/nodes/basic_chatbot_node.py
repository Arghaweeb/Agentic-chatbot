
from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    BasicChatbotNode class to represent a basic chatbot node in the LangGraph Agentic AI application.
    This class is used to initialize a chatbot node with a specified LLM model.
    """
    def __init__(self, model):
        self.llm = model

    def process(self,state:State)->dict:
        """
        Process the state and return the response from the LLM model."""

        return {"messages":self.llm.invoke(state["messages"])}
