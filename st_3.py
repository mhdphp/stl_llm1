import streamlit as st
import pandas as pd

# expander
with st.expander("Click to expand"):
    st.write("Hidden content revealed!")


# file uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(uploaded_file.name)
    # For CSV files:
    # df = pd.read_csv(uploaded_file)
    # st.dataframe(df)


# Progress and status bar
import time

# Progress bar
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i + 1)

# Spinner
with st.spinner("Loading..."):
    time.sleep(2)
st.success("Done!")

# Status messages
st.error("This is an error")
st.warning("This is a warning")
st.info("This is info")
st.success("This is a success")

# cashing
@st.cache_data
def expensive_computation():
    time.sleep(2)  # Simulate slow computation
    return 42

result = expensive_computation()
st.write(f"The answer is {result}")

# advanced features
# Session State (for maintaining state)
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Count: {st.session_state.counter}")

# Theme customization
st.write("Check out the theme options in the hamburger menu (☰)")

# Custom components (using HTML/JS)
st.html("<h3 style='color: red;'>Custom HTML</h3>")