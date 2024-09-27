import streamlit as st
import sys
import os
import mykey
import openai

OPENAI_API_KEY = mykey.OPENAI_API_KEY
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

from openai import OpenAI
client = OpenAI()

OpenAI.api_key = os.getenv('OPENAI_API_KEY') 
st.title("My Message Generator (with Streamlit)")

user_option1 = st.selectbox("Please select relation", ("Mother", "Father", "Sister", "Brother", "Dog", "Cat", "Boss", "Partner"), 
                            index=None, 
                            placeholder="Select relation")
user_option2 = st.selectbox("Please select context", ("Thank you", "Sorry", "Appreciation", "Showing love", "Planning holidays"),
                           index=None,
                           placeholder="Select context")

if user_option1 and user_option2:
    prompt = "Give me a message for my " + user_option1 + " about " + user_option2
    response = client.completions.create(model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=300, temperature=0.9)
    generated_text = response.choices[0].text
    st.write("Here you go: ", generated_text)
else:
    st.write("Please select from the options above")