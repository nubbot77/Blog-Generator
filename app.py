import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from constants import path


##function top get responce from llama model

def response(input_text,no_words,blog_style):
    
    ## load LLama model

    llm = CTransformers(model=path, model_type='llama',config={'max_new_tokens':500,'temperature':0.7})

    ## Prompt

    template = """write a blog for {blog_style} job profile for a topic {input_text} within the {no_words} words."""

    prompt = PromptTemplate(input_variables=["blog_style","nput_text","no_words"],template=template)

    ##create responce from llama

    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))

    print(response)
    return response




st.set_page_config(page_title="Generate Blogs",
                   page_icon="🤖",
                   layout="centered",
                   initial_sidebar_state="collapsed"
)

st.header("Generate the Blogs 🤖")

input_text = st.text_input("Enter the Blog title")

##creating two more column for additional two fields

col1,col2 = st.columns([5,5])


with col1:
    no_words = st.text_input("No of words")


with col2:
    blog_style = st.selectbox('Writting the blog for',('Researchers','Data Scientists','Common People'),index=0)


submit = st.button("Generate")
 
## Final Response

if submit:
    st.write(response(input_text,no_words,blog_style))


