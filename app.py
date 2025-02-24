import streamlit as st

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("RAG Chatbot (Coming Soon!)")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me something...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Placeholder response (Replace with real AI response later)
    bot_response = "I'm still learning! Soon I'll have real answers for you. 🚀"
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)