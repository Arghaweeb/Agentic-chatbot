import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        """Initialize the Streamlit UI loader."""
        self.config = Config()
        self.user_controls={}
    
    def load_streamlit_ui(self):
        st.set_page_config(
            page_title= "🤖 " + self.config.get_page_title(),
            layout="wide"
        )
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:
            #Get options from the config file
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            
            #LLM selection
            self.user_controls['selected_llm'] = st.selectbox(
                "Select LLM",
                options=llm_options
            )

            if self.user_controls['selected_llm'] == "Groq":
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                #Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API Key to use the Groq model. Don't have one? Sign up at https://groq.com/ to get your API key.")

            ## Usecases selection
            self.user_controls['selected_usecase'] = st.selectbox(
                "Select Use Case",
                usecase_options,
            )
            if self.user_controls['selected_usecase'] == "Chatbot With Web":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"]=st.text_input("Tavily API Key", type="password")

                 #Validate API Key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your Tavily API Key to proceed. Don't have one? Sign up at https://www.tavily.com/ to get your API key.")



        return self.user_controls