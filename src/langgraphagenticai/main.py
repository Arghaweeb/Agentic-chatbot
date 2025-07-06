import streamlit as st

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

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

    if user_message:
        try:
            # Configure the LLM model based on user input
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized")
                return
            
            # Initialize the graph based on the selected use case
            usecase = user_input.get('selected_usecase')

            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            ##Graphbuiilder
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Failed to set up the graph for use case '{usecase}'. Please check the configuration. Exception: {e}")
                return


        except Exception as e:
            st.error(f"Error: Grqph setup failed. Please check the configuration. Exception: {e}")
            return



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