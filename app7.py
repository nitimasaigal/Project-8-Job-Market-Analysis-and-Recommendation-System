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

    # Ensure 'published_date' is in datetime format and remove timezone information if present
    try:
        df['published_date'] = pd.to_datetime(df['published_date']).dt.tz_localize(None)
        st.write("Published date converted successfully")
    except Exception as e:
        st.error(f"Error converting published_date: {e}")
        return pd.DataFrame()

    return df

# Load data
df = load_data()

# Filter for remote jobs
remote_jobs = df[df['title'].str.contains('remote', case=False, na=False)]

# Extract year and month from 'published_date'
remote_jobs['year_month'] = remote_jobs['published_date'].dt.to_period('M')

# Group by 'year_month' to get the count of remote job postings each month
monthly_remote_job_counts = remote_jobs.groupby('year_month').size().reset_index(name='job_count')
monthly_remote_job_counts['year_month'] = monthly_remote_job_counts['year_month'].astype(str)

# Check if data is not empty
if monthly_remote_job_counts.empty:
    st.error("No data to display")
else:
    st.write("Processed data:", monthly_remote_job_counts.head())

    # Create Streamlit app
    st.title('Remote Work Trends Dashboard')

    # Create a line plot to show remote job postings over time with customizations
    fig = px.line(monthly_remote_job_counts, x='year_month', y='job_count', 
                  title='Remote Job Postings Over Time', 
                  labels={'year_month': 'Month', 'job_count': 'Number of Remote Job Postings'})
    fig.update_traces(line=dict(color='royalblue', width=4))
    fig.update_layout(width=800, height=600)

    # Show the plot
    st.plotly_chart(fig)


    # Refresh button
    if st.button('Refresh Data'):
        st.experimental_rerun()
