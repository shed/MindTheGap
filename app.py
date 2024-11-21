import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the app title
st.title("Load and Display Local CSV File")

# Attempt to load the CSV file
try:
    # Load the local file
    df = pd.read_csv("df_boolean.csv")
    
    # Display success message and data
    st.success("Successfully loaded csv !")
    st.write("Here is the data:")
    st.dataframe(df)
    
    # Show summary statistics
    

    # Assuming 'df' is your DataFrame
    years_in_university_counts = df.groupby('years_in_university').size()

    fig = px.bar(
        x=years_in_university_counts.index,
        y=years_in_university_counts.values,
        labels={'x': 'Years in University', 'y': 'Number of Participants'},
        title='Number of Participants by Years in University',
        color_discrete_sequence=['#1b69af']  # Set a single color
    )
    fig.update_xaxes(type='category')  # Treat x-axis as categorical

    # Map numerical values to labels for x-axis
    x_axis_labels = {
        0: 'Less than a Year',
        1: '1 Year',
        2: '2 Years',
        3: '3 Years',
        4: '4+ Years'
    }
    fig.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(x_axis_labels.keys()),
            ticktext=list(x_axis_labels.values())
        )
    )

    fig.show()

    
    
    
    
except FileNotFoundError:
    st.error("File csv not found in the current directory. Please ensure the file exists.")

