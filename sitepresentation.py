import streamlit as st
from PIL import Image
import pandas as pd

#set up the logo
logo = Image.open("logo.png")
st.sidebar.image(logo, width=100)

#Inserting the title
st.title("Amsterdam's best business")

#Sidebar
st.sidebar.header("Presentation")
st.sidebar.text("What is the best business in Amsterdam?")
st.sidebar.markdown("""We are going to present a series of graphs to you now, extracted from [Yelp]("https://www.yelp.it/search?find_desc=&find_loc=Amsterdam%2C+Noord-Holland&ns=1") to help you choose the best business to invest in""")

#Main page/header
st.header("How can you invest effectively")

#Main_text
st.markdown
