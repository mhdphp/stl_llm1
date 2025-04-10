import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

#components.html("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """)

st.title("My First Streamlit App")
st.write("Hello, world!")

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is plain text")
st.markdown("**This** is markdown")

#components.html("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """)

# Button
st.subheader("Button")
if st.button("Click me!"):
    st.write("Button clicked!")

# Checkbox
st.subheader("Checkbox")
if st.checkbox("Check me!"):
    st.write("Checkbox checked!")


# Radio button
st.subheader("Radio button")
option = st.radio("Choose one:", ("Option 1", "Option 2"))
st.write(f"You selected: {option}")

# Selectbox
st.subheader("Selectbox")
option = st.selectbox("Select one:", ["A", "B", "C"])
st.write(f"You selected: {option}")

# Slider
st.subheader("Slider")
age = st.slider("Your age", 0, 100, 25)
st.write(f"I'm {age} years old")

# Text input
st.subheader("Text input")
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")

#components.html("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """)

# Display dataframes
st.subheader("Dataframes")
st.text("define dataframe")
df = pd.DataFrame({
    "Column 1": [1, 2, 3],
    "Column 2": ["A", "B", "C"],
    "Column 3": [True, False, True]
})
st.text("Display dataframe")
st.dataframe(df, width=700, height=300)
st.text("Display table")
st.table(df)

# Display charts
st.subheader("Charts")
st.line_chart(df["Column 1"])
st.bar_chart(df["Column 1"])
st.area_chart(df["Column 1"])

