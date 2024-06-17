from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model and vectorizers
model = joblib.load('budget_predictor_model.pkl')
tfidf_job_title = joblib.load('tfidf_job_title.pkl')
tfidf_company = joblib.load('tfidf_company.pkl')
tfidf_location = joblib.load('tfidf_location.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        form_data = request.form
        data = {
            'job_title': str(form_data['job_title']),
            'company': str(form_data['company']),
            'location': str(form_data['location']),
            'link': str(form_data['link'])  # Include link for the output
        }

        # Transform text data
        job_title_tfidf = tfidf_job_title.transform([data['job_title']])
        company_tfidf = tfidf_company.transform([data['company']])
        location_tfidf = tfidf_location.transform([data['location']])

        # Create a DataFrame for the input data
        input_df = pd.concat([
            pd.DataFrame(job_title_tfidf.toarray(), index=[0]),
            pd.DataFrame(company_tfidf.toarray(), index=[0]),
            pd.DataFrame(location_tfidf.toarray(), index=[0])
        ], axis=1)
        input_df.columns = input_df.columns.astype(str)  # Convert column names to strings

        # Predict
        prediction = model.predict(input_df)[0]

        return render_template('results.html', prediction=prediction, link=data['link'])
    except Exception as e:
        return f"An error occurred: {e}", 400

if __name__ == '__main__':
    app.run(debug=True)
