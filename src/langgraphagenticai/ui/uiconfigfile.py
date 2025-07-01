from configparser import ConfigParser

class Config:
    def __init__(self, config_file='src/langgraphagenticai/ui/uiconfigfile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        """Get the LLM options from the config file."""
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(', ')
    
    def get_page_title(self):
        """Get the page title from the config file."""
        return self.config["DEFAULT"].get("PAGE_TITLE", "LangGraph: Build Stateful Agentic AI LangGraph")
    
    def get_usecase_options(self):
        """Get the use case options from the config file."""
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(', ')
    
    def get_groq_model_options(self):
        """Get the Groq model options from the config file."""
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(', ')
    
    def get_openai_model_options(self):
        """Get the OpenAI model options from the config file."""
        return self.config["DEFAULT"].get("OpenAI_MODEL_OPTIONS").split(', ')