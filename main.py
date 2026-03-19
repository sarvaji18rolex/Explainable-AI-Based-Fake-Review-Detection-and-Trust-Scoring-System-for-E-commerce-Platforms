import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# =========================
# LOAD DATASET
# =========================
data = pd.read_csv("Preprocessed Fake Reviews Detection Dataset.csv")

# Clean dataset
data = data.drop(columns=["Unnamed: 0"])
data = data.rename(columns={"text_": "review"})
data = data.dropna()

print(data.head())
print(data['label'].value_counts())

# =========================
# TEXT PREPROCESSING
# =========================
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

data['clean_review'] = data['review'].apply(clean_text)
data['review_length'] = data['clean_review'].apply(len)

print(data[['review', 'clean_review']].head())

# =========================
# TF-IDF VECTORIZATION
# =========================
vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(data['clean_review']).toarray()
y = data['label']

print(X.shape)

# =========================
# TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# MODEL TRAINING
# =========================
model = LogisticRegression()
model.fit(X_train, y_train)

# =========================
# MODEL EVALUATION
# =========================
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# =========================
# PREDICTION FUNCTION
# =========================
def predict_with_score(review):
    review = clean_text(review)
    vector = vectorizer.transform([review]).toarray()
    
    prob = model.predict_proba(vector)[0]
    confidence = max(prob) * 100
    prediction = model.predict(vector)[0]
    
    if confidence < 60:
        return "Suspicious ⚠️", round(confidence, 2)
    
    label = "Fake ❌" if prediction == 0 else "Genuine ✅"
    return label, float(round(confidence, 2))

# =========================
# TRUST SCORE FUNCTION
# =========================
def calculate_trust_score(reviews):
    fake_count = 0
    genuine_count = 0
    suspicious_count = 0
    
    for review in reviews:
        label, _ = predict_with_score(review)
        
        if "Fake" in label:
            fake_count += 1
        elif "Genuine" in label:
            genuine_count += 1
        else:
            suspicious_count += 1
    
    total = len(reviews)
    
    trust_score = (genuine_count / total) * 100
    
    return {
        "Total Reviews": total,
        "Fake Reviews": fake_count,
        "Genuine Reviews": genuine_count,
        "Suspicious Reviews": suspicious_count,
        "Trust Score (%)": round(trust_score, 2)
    }

# =========================
# TESTING
# =========================
sample_reviews = [
    "Amazing product! Must buy!",
    "Worst product ever",
    "Good quality and value for money",
    "Best best best best product!!!"
]

print("\nSingle Prediction:")
print(predict_with_score("This product is amazing!!!"))

print("\nTrust Score Output:")
print(calculate_trust_score(sample_reviews))