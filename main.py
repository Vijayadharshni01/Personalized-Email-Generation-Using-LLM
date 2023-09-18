import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI 
import os

os.environ["OPEN_API_KEY"] = "API-KEY"

llm = OpenAI(temperature=0.9, openai_api_key="API-KEY")
text = "hello what is your name"
print(llm(text))

template =""" 
Write a proper email with the given informations below/
- tone for the email should be {tone}
- language in which the email should be written {language}
- the content for the email which should be modified using the above paramters and thw content is given in closed brackets ({email})
"""

prompt = PromptTemplate(input_variables=["tone","language","email"],template=template)

#def load_llm():
    #llm = OpenAI(temperature=0, openai_api_key="API-KEY")
    #return llm

#llm = load_llm()

web = st.set_page_config(page_title="Axolotl",page_icon="🐢")
st.header("I am Creating a Chatbot")
col1,col2 = st.columns(2)

with col1:
    st.write("I watched many youtube tutorials and doing this webpage using streamlit.")

with col2:
    st.image(image="puppy.jpg",width=500)

st.markdown("## Convert your content into Email")
col11,col22 = st.columns(2)

with col11:
    option1 = st.selectbox("Select the tone",("formal tone","informal tone"))
with col22:
    option2 = st.selectbox("Select the language",("english","english only"))

def userinput():
    input_text = st.text_area(placeholder="Write the content",label="",key="user_text")
    return input_text

user_text = userinput()

st.markdown("#### OK Converting that into an email :)")

if user_text:
    prompt_a = prompt.format(tone = option1, language = option2, email = user_text)
    #st.write(prompt_a)
    st.write(llm(prompt_a))

