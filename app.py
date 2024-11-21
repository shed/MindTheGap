import streamlit as st
import pandas as pd

# Set up the app title
st.title("Load and Display Local CSV File")

# Attempt to load the CSV file
try:
    # Load the local file
    df = pd.read_csv("df_boolean.csv")
    
    # Display success message and data
    st.success("Successfully loaded csv`!")
    st.write("Here is the data:")
    st.dataframe(df)
    
    # Show summary statistics
    st.write("Summary Statistics: ")
    st.write(df.describe())
except FileNotFoundError:
    st.error("File csv not found in the current directory. Please ensure the file exists.")

