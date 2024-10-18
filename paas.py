import streamlit as st
import pandas as pd

# Title of the app
st.title("Simple File Upload App")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file is uploaded, read and display it
if uploaded_file is not None:
    # Read the file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the DataFrame
    st.write("Uploaded Data:")
    st.dataframe(df)

    # Optionally, show summary statistics
    if st.checkbox("Show Summary Statistics"):
        st.write(df.describe())
