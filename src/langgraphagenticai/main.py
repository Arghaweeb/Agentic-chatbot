import streamlit as st

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agentic_ai_app():
    """
    Loads and runs the LangGraph Agentic AI application using Streamlit.
    This function initializes the Streamlit UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while implementing exception handling for robustness.

    """

    ##Load UI
    ui=LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("ERror: Failed to load user input. Please try again.")
        return 
    
    user_message = st.chat_input("Enter your message here...")

    # if user_message:
    #     try:
    #         #Configure the LLM model based on user input
    #         obj_llm_config = GroqLLM(user_controls_input=user_input)
    #         model = obj_llm_config.get_llm_model()

    #         if not model:
    #             st.error("Error: LLM model could not be initialized")
    #             return
            
    #         #initialize the graph based on the selected use case
    #         usecase = user_input.get('selected_usecase')
    #         if not usecase:
    #             st.error("Error: No use case not selected.")
    #             return