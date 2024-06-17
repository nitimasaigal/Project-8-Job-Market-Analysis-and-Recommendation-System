import streamlit as st
import pandas as pd

# Function to load the CSV file containing job data
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('jobs.csv')
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Initialize the application
st.title('Job Recommendation Engine')

# Load data once and cache it
data = load_data()

if not data.empty:
    st.write("Loaded job data:")
    st.write(data.head())
else:
    st.write("No job data available. Please check the CSV file.")

# Input for job title
job_title = st.text_input('Enter a job title')

# Button to get recommendations
if st.button('Get Recommendations'):
    try:
        if job_title:
            # Debug: Show the input job title
            st.write(f"Job title entered: {job_title}")
            
            # Simple recommendation logic 
            recommendations = data[data['job_title'].str.contains(job_title, case=False, na=False)]
            
            # Debug: Show the filtered recommendations
            st.write("Filtered recommendations:")
            st.write(recommendations)
            
            if not recommendations.empty:
                st.write(recommendations)
            else:
                st.write("No recommendations found for the given job title.")
        else:
            st.write("Please enter a job title.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")





