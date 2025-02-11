import os
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_together import ChatTogether

# Set Together AI API Key
os.environ["TOGETHER_API_KEY"] = "ff4b9f7386b2863ee05da857e4c23d08c6d867d819ff40f7319f2c5489962911"  # Replace with your actual API key

# Initialize the LLM
llm = ChatTogether(model="mistralai/Mistral-7B-Instruct-v0.1", api_key=os.environ["TOGETHER_API_KEY"])

# Streamlit UI
st.title("🤖 Deutscher KI-Chatbot mit Together AI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Schreibe deine Nachricht...")  # Prompt in German
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    
    # System message to enforce German responses
    system_message = SystemMessage(content="Du bist ein hilfreicher KI-Chatbot und antwortest nur auf Deutsch.")
    
    # Get AI response
    response = llm.invoke([system_message, HumanMessage(content=user_input)])
    ai_response = response.content if response else "Fehler beim Generieren der Antwort."
    
    st.session_state["messages"].append({"role": "ai", "content": ai_response})
    st.chat_message("ai").write(ai_response)
