import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Create a text input widget
user_input = st.text_input("Enter something:")

# Create a button
if st.button("Submit"):
    # Display the user's input
    st.write("You entered:", user_input)
