import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class JobRecommender:
    def __init__(self, dataset_path):
        self.jobs = pd.read_csv("jobs.csv")
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.jobs['description'])
    
    def recommend_jobs(self, job_title, top_n=5):
        query_vec = self.tfidf.transform([job_title])
        similarity_scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = similarity_scores.argsort()[-top_n:][::-1]
        return self.jobs.iloc[top_indices].to_dict(orient='records')

# Example usage
# recommender = JobRecommender('jobs.csv')
# recommendations = recommender.recommend_jobs('Software Engineer')
# print(recommendations)
