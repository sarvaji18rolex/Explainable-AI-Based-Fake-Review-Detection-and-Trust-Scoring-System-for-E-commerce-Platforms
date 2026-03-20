from flask import Flask, render_template, request
import pickle 

app = Flask(__name__)

# Import your functions from main.py
from main import predict_with_score, calculate_trust_score

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    
    label, confidence = predict_with_score(review)
    
    return render_template('index.html', 
                           prediction=label, 
                           confidence=confidence)

@app.route('/trust', methods=['POST'])
def trust():
    reviews = request.form['reviews'].split("\n")
    
    result = calculate_trust_score(reviews)
    
    return render_template('index.html', trust=result)

if __name__ == "__main__":
    app.run(debug=True)
