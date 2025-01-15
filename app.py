import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun
import os


load_dotenv()


try:
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="gemma2-9b-it"
    )
except Exception as e:
    st.error("Error initializing the LLM. Please check your API key.")
    st.stop()


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a ShubhGPT. How can I assist you today?"}
    ]

st.title("ShubhGPT")
st.write("Ask me anything! I'll Answer")

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])


user_input = st.chat_input(placeholder="What is machine learning?")

if user_input:
    
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    conversation_history = "\n".join(
        f"{msg['role'].capitalize()}: {msg['content']}"
        for msg in st.session_state["messages"]
    )

    with st.spinner("Thinking..."):
        try:
            response = llm.invoke(input=conversation_history)  
            response_content = response.content 
            st.session_state["messages"].append({"role": "assistant", "content": response_content})
            st.chat_message("assistant").write(response_content)
        except Exception as e:
            st.error(f"An error occurred: {e}")

