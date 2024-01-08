import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Function to clear the assistant ID
def clear_assistant_id():
    st.session_state.assistant_id = ""
    st.session_state.assistant_name = ""


def assistant_input_component():
    st.session_state.assistant_id = st.text_input(
        label="Enter your assistant_id",
    )

    if st.session_state.assistant_id and not st.session_state.assistant_id == "":
        get_assistant_name()


def get_assistant_name():
    assistant = client.beta.assistants.retrieve(st.session_state.assistant_id)
    st.session_state.assistant_name = assistant.name
