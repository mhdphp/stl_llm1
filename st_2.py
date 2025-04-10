import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:", layout="wide")
st.title("My Streamlit App")

st.write("This is a simple Streamlit app with various components.")


st.sidebar.title("Sidebar")
option = st.sidebar.selectbox("Choose:", ["A", "B", "C"])
st.write(f"Main content with {option} from sidebar")


st.subheader("columns")
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Column 1 content")

with col2:
    st.header("Column 2")
    st.write("Column 2 content")


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header("Column 1")
    st.write("Column 1 content")

with col2:
    st.header("Column 2")
    st.write("Column 2 content")    

with col3:
    st.header("Column 3")
    st.write("Column 3 content")    

with col4:
    st.header("Column 4")
    st.write("Column 4 content")