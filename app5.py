from flask import Flask, request, jsonify
from recommendation_engine import JobRecommender

app = Flask(__name__)
recommender = JobRecommender('jobs.csv')

@app.route('/')
def home():
    return "Job Recommendation API is running"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    job_title = data.get('job_title')
    if not job_title:
        return jsonify({'error': 'Job title is required'}), 400
    recommendations = recommender.recommend_jobs(job_title)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)

