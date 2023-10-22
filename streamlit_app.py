# Code refactored from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage


chat_model =  ChatOllama(model="mistral:latest")

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
    print(f"this is the prompt: {prompt}")
    #Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    #Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # format the prompt into a human message so it can be read by ollama 
        ollama_prompt = [
            HumanMessage(content=prompt)
        ]
        message = chat_model(ollama_prompt)
        full_response = message.content
        # st. write the data type of message 
        # st.write(type(message))

        st.markdown(full_response)
    # Add assistant response to chat history 
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# TODO add memory to the chatbot so it can remember the previous line!

