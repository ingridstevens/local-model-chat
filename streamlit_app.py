# Code refactored from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

from langchain.llms import Ollama

llm =  Ollama(model="mistral:latest")


import streamlit as st

# Set the page title
st.title("Mistral Bot")

# Create a sidebar that says OpenAI Chatbot
with st.sidebar:
    st.write("## 🤖💬 OpenAI Chatbot")
    
# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display Chat Messages from History 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# check if there is a prompt and it is not none
if prompt := st.chat_input("How can I help?"):
    #Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    #Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})



    response = llm(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history 
    st.session_state.messages.append({"role": "assistant", "content": response})


