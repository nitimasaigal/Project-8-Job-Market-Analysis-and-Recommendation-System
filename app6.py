import pandas as pd
import plotly.express as px
import streamlit as st

# Function to load and process data
def load_data():
    try:
        df = pd.read_csv(r"C:\Users\Niti\NEXT HIKES\PROJECT 8\all_upwork_jobs_next.csv")
        st.write("Data loaded successfully")
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

    
    try:
        df['published_date'] = pd.to_datetime(df['published_date']).dt.tz_localize(None)
        st.write("Published date converted successfully")
    except Exception as e:
        st.error(f"Error converting published_date: {e}")
        return pd.DataFrame()

    # Extract month and year from 'published_date'
    try:
        df['year_month'] = df['published_date'].dt.to_period('M')
        st.write("Year and month extracted successfully")
    except Exception as e:
        st.error(f"Error extracting year_month: {e}")
        return pd.DataFrame()

    # Group by 'year_month' to get the count of job postings each month
    try:
        monthly_job_counts = df.groupby('year_month').size().reset_index(name='job_count')
        monthly_job_counts['year_month'] = monthly_job_counts['year_month'].astype(str)
        st.write("Monthly job counts calculated successfully")
    except Exception as e:
        st.error(f"Error calculating monthly job counts: {e}")
        return pd.DataFrame()

    return monthly_job_counts

# Load data
monthly_job_counts = load_data()

# Check if data is not empty
if monthly_job_counts.empty:
    st.error("No data to display")
else:
    st.write("Processed data:", monthly_job_counts.head())

    # Create Streamlit app
    st.title('Job Market Dynamics Dashboard')

    # Create a line plot to show job postings over time with customizations
    fig = px.line(monthly_job_counts, x='year_month', y='job_count', 
                  title='Job Postings Over Time', 
                  labels={'year_month': 'Month', 'job_count': 'Number of Job Postings'})
    fig.update_traces(line=dict(color='royalblue', width=4))
    fig.update_layout(width=800, height=600)

    # Show the plot
    st.plotly_chart(fig)

    # Refresh button
    if st.button('Refresh Data'):
        st.experimental_rerun()
