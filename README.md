# Local Model Chat
============================

This is a simple chat application built using the Langchain library in Python. It allows users to interact with an AI chatbot through a user interface. The chatbot responds to prompts from the user and can generate new responses based on the user's input.

## Prerequisites

---------------------------------------------------------

Before running this code, you will need to install the following libraries:

-   `langchain` 
-   `streamlit` 

```
pip install langchain streamlit
```

## Setup

-----------------------------------------

To set up the chat application, save the code below in a file named `local_model_chat.py`. 

Install dependencies via `requirements.txt`:

``` 
pip install -r requirements.txt

```

Then, run the following command to start the application:

```
streamlit run local_model_chat.py
```

The chat application will open in your default web browser. You can interact with the AI chatbot by typing messages in the text box on the left side of the screen.

## How it works

-------------------------------------------------------

The chat application uses the Langchain library to create an AI chatbot that can understand and respond to user input. The chatbot is able to generate new responses based on the user's input using a machine learning model. The `local_model_chat.py` file imports the necessary libraries and sets up the user interface for the chat application. It also initializes memory for the chat session using the Langchain library, which allows the chatbot to remember previous messages exchanged between the user and itself. When a user types a message in the text box on the left side of the screen, the message is sent to the chatbot through the user interface. The chatbot then processes the message using its machine learning model and generates a response. The generated response is displayed in the text box on the right side of the screen, along with any previously exchanged messages. The user can continue the conversation by typing more messages in the left-hand text box.

## Machine Learning Model

---------------------------------------------------------------------------

The chatbot uses an LLM model to generate responses based on the user's input. The `local_model_chat.py` file includes a picker for choosing an LLM model, with two options available: "Mistral" and "llama2". If the user selects "llama2", the chatbot uses the Ollama model with a specific model name and version. Otherwise, it uses the Mistral model with its default settings. The LLM model is integrated into the chatbot through the Langchain library, which provides a simple interface for interacting with the model and generating responses based on user input.