JOB MARKET ANALYSIS AND RECOMMENDATION SYSTEM

The primary objective of this project is to analyze job market trends and build a recommendation system for job seekers based on real-time data. The system will help in identifying high-demand job roles, salary trends, and emerging job categories, and will provide personalized job recommendations.

Prerequisites

Before running the project, we need to ensure that we have the following dependencies installed: Python (version 3.6 or higher) Flask (pip install Flask) Sklearn (pip install scikit-learn) Pandas (pip install pandas) numpy (pip install numpy) regression and classification models (as per the dataset) TF-IDF Vectorizer or CountVectorizer Wordcloud etc.

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

Four models have been trained..Random Forest Classifier, Logistic Regression, Support Vector and Neural Network but Logistic Regression Model has the highest accuracy. So this model only has been used for making Flask Dashboard.

Running the Web App

Navigate to the app/directory and it can be run by running the app.py(python file) by giving the command flask run

This is the link for Twitter Dashboard

Relationship between all the features and target

correlation between all the features which have been created and the Target is as follows: image

Credits/Acknowledgements

All credit goes to Shweta Mam for this project

Contact Information

Nitima Saigal
