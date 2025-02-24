import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Get API key from environment
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("🚨 Error: GROQ_API_KEY is missing! Ensure it's set in your .env file.")
    st.stop()

# Initialize Llama 3 model
llm = ChatGroq(model_name="llama3-8b-8192", api_key=api_key)

# Set Streamlit config to force using port 8501
st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("RAG Chatbot - Powered by Llama 3")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me something...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Query Llama 3
    bot_response = llm.invoke(user_input)

    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)