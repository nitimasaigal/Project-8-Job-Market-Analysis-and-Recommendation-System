JOB MARKET ANALYSIS AND RECOMMENDATION SYSTEM

The primary objective of this project is to analyze job market trends and build a recommendation system for job seekers based on real-time data. The system will help in identifying high-demand job roles, salary trends, and emerging job categories, and will provide personalized job recommendations.

Prerequisites

Before running the project, we need to ensure that we have the following dependencies installed: Python (version 3.6 or higher) Flask (pip install Flask) Sklearn (pip install scikit-learn) Pandas (pip install pandas) numpy (pip install numpy) regression and classification models (as per the dataset) TF-IDF Vectorizer.

Project Structure

The project is structured as follows:

|--app/

| |--static/

| |--templates/

| | |--index.html

| | |--results.html

| |--app.py

| |--dockerfile

| |--requirements.txt

| |--budget_predictor_model.pkl

| |--tfidf_company.pkl

| |--tfidf_description.pkl

| |--tfidf_job_title.pkl

| |--tfidf_link.pkl

| |--tfidf_location.pkl

|--flask dashboard to predict job recommendation system.pdf

|--dashboards for job market analysis and recommendation system.pdf

|--job market analysis and recommendation system.pdf

|--jobs.csv

|--emerging_categories_report.csv

|--Project Solution Task 1.ipynb

|--Project Solution Task 2.ipynb

|--model prediction for flask.ipynb

|--README.md

Training the Model

Random Forest Regressor Model has been used through Pipeline for making Flask Dashboard. And also TfidfVectorizer to change the text.

Running the Web App

Navigate to the app/directory and it can be run by running the app.py(python file) by giving the command flask run and streamlit run

Running the Dockerfile

docker build --no-cache -t nitimasaigal/project8-job_recommendation_system:latest .

docker run -d -p 3000:3000 nitimasaigal/project8-job_recommendation_system:latest


Link for Dockerfile:

Running on all addresses (0.0.0.0)

Running on http://127.0.0.1:3000

Running on http://172.17.0.8:3000


This is the link for Dashboard

Task 5:
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8502
  Network URL: http://192.168.1.2:8502

Local URL: http://localhost:8512
  Network URL: http://192.168.1.2:8512



Task 6:
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8503
  Network URL: http://192.168.1.2:8503

Task 7:
Local URL: http://localhost:8504
Network URL: http://192.168.1.2:8504

Task 7.1:
Local URL: http://localhost:8505
Network URL: http://192.168.1.2:8505


Relationship between all the features and target

correlation between all the features which have been created and the Target is as follows: ![correlation_plot](https://github.com/nitimasaigal/Project-8-Job-Market-Analysis-and-Recommendation-System/assets/146649752/ca168741-7ff8-4110-ad0d-818691455cc9)

Predicting Future job market trends with Potential Future scenarios: ![image](https://github.com/nitimasaigal/Project-8-Job-Market-Analysis-and-Recommendation-System/assets/146649752/b6547675-ff82-4e9d-ad4b-d6c2707002be)



Credits/Acknowledgements

All credit goes to Shweta Mam for this project

Contact Information

Nitima Saigal
