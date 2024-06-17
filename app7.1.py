import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
import matplotlib.pyplot as plt

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

if df.empty:
    st.error("No data available.")
else:
    # Filter for remote jobs
    remote_jobs = df[df['title'].str.contains('remote', case=False, na=False)]

    # Extract year and month from 'published_date'
    remote_jobs['year_month'] = remote_jobs['published_date'].dt.to_period('M')

    # Group by 'year_month' to get the count of remote job postings each month
    monthly_remote_job_counts = remote_jobs.groupby('year_month').size().reset_index(name='job_count')
    monthly_remote_job_counts['year_month'] = monthly_remote_job_counts['year_month'].astype(str)

    if monthly_remote_job_counts.empty:
        st.error("No remote job postings found in the data.")
    else:
        st.title('Remote Work Trends Dashboard')

        # Create a line plot to show remote job postings over time
        fig = px.line(monthly_remote_job_counts, x='year_month', y='job_count', 
                      title='Remote Job Postings Over Time', 
                      labels={'year_month': 'Month', 'job_count': 'Number of Remote Job Postings'})
        fig.update_traces(line=dict(color='royalblue', width=4))
        fig.update_layout(width=800, height=600)

        # Display the plot
        st.plotly_chart(fig)

        # Prepare data for Prophet
        monthly_remote_job_counts['ds'] = pd.to_datetime(monthly_remote_job_counts['year_month'])
        monthly_remote_job_counts['y'] = monthly_remote_job_counts['job_count']
        prophet_df = monthly_remote_job_counts[['ds', 'y']]

        # Initialize and fit Prophet model
        model = Prophet()
        model.fit(prophet_df)

        # Create future dataframe and make predictions
        future = model.make_future_dataframe(periods=12, freq='M')  # Forecast for the next 12 months
        forecast = model.predict(future)

        # Plot the forecast
        fig_forecast = model.plot(forecast)
        
        # Render forecast plot in Streamlit
        st.write("### Forecast Plot")
        st.pyplot(fig_forecast)

        # Summary and insights
        st.header('Summary and Insights')
        st.write("""
        - The number of remote job postings has shown [increase] over the past months.
        - According to the forecast, the trend is expected to [continue] in the coming year.
        - Key factors influencing this trend include factors such as industry changes, economic conditions, etc.
        """)

        # Refresh button
        if st.button('Refresh Data'):
            st.experimental_rerun()
