# Memory-Based Chatbot using LangChain and Ollama

This project is a commandline conversational AI chatbot built using LangChain with a locally hosted large language model (LLM) via Ollama. 
It integrates a conversation summary memory module to maintain context across user interactions, 
making responses more coherent and context aware.


# Features

* Conversational chatbot loop with terminal interface
* Context-aware responses using LangChain’s `ConversationSummaryMemory`
* Local LLM deployment using Ollama with `llama3`
* Modular design using LangChain’s `RunnableLambda` and `PromptTemplate`
* Fully offline and API-free operation


# Tech Stack

* Python 3.12+
* LangChain (Core, Memory)
* Ollama
* llama3 model


# Setup

1. Set Up a Virtual Environment :
python3 -m venv venv
source venv/bin/activate

2. Installed Python Dependencies :
pip install langchain langchain-core langchain-ollama

3. Installed and Started Ollama :
brew install ollama
ollama serve
ollama pull llama3

   * Note: Ensure `ollama serve` is running before executing the chatbot.

4. Run the Chatbot :
python "python code/chatbot_memory.py"


# File Structure

├── python code/
│   └── Chatbot_memory.py      # Main chatbot implementation
├── venv/                      # Python virtual environment
└── README.md
    └── requirements.txt       # Project explained (here)


#Project Goals

This project aims to demonstrate how to integrate memory with local LLMs using LangChain. 
It focuses on building a fully local and extensible chatbot that can remember previous messages 
and respond in a contextually relevant way, without relying on cloud APIs.


# Future Enhancements

* Web UI with Streamlit or Flask
* Integration with speech recognition
* Vector store-based long-term memory
* Logging and analytics
