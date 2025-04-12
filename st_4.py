from streamlit import st


# inputs
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

age = st.number_input("Your age:", min_value=0, max_value=120, value=25)
st.write(f"You are {age} years old.")

temperature = st.slider("Select temperature (°C):", -10, 40, 20)
st.write(f"Selected: {temperature}°C")

color = st.selectbox("Pick a color:", ["Red", "Green", "Blue"])
st.write(f"You chose: {color}")

agree = st.checkbox("I agree to the terms")
if agree:
    st.success("Thank you for agreeing!")

if st.button("Click me!"):
    st.balloons()  # Show celebration balloons
    st.write("Button clicked! 🎉")

# using inputs in calculations
weight = st.number_input("Weight (kg):", min_value=30.0, max_value=200.0)
height = st.number_input("Height (m):", min_value=1.0, max_value=2.5, value=1.75)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")


# file uploader
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write("Data preview:")
    st.dataframe(df.head())


# Session State (Preserve Data Between Reruns)
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")

# Forms (st.form) for Batch Input
with st.form("user_details"):
    name = st.text_input("Name")
    age = st.number_input("Age")
    submit = st.form_submit_button("Submit")

if submit:
    st.write(f"Submitted: {name}, {age} years old")

# Real-Time Updates (Using Callbacks)
def update_slider():
    st.session_state.slider_value = st.session_state.new_value

st.slider("Select a value:", 0, 100, key="slider_value")
st.number_input("Or type a value:", 0, 100, key="new_value", on_change=update_slider)
