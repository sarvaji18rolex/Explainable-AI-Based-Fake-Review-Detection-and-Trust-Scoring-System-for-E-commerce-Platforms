# 🛒 Explainable AI-Based Fake Review Detection and Trust Scoring System

## 📌 Project Overview

The rapid growth of e-commerce platforms has led to an increase in fake and misleading product reviews. This project presents an AI-based solution that detects fake reviews using Natural Language Processing (NLP) and Machine Learning techniques.

The system not only classifies reviews as **Fake or Genuine**, but also provides a **confidence score**, identifies **suspicious reviews**, and calculates a **trust score** for products. A user-friendly web interface and interactive dashboard make the system practical and easy to use.

---

## 🎯 Objectives

* Detect fake and spam reviews automatically
* Provide confidence-based predictions
* Identify suspicious or borderline reviews
* Calculate product trust score
* Visualize review authenticity using charts

---

## 🚀 Features

* 🔍 Fake vs Genuine Review Classification
* 📊 Confidence Score Prediction
* ⚠️ Suspicious Review Detection
* 📈 Trust Score Calculation
* 🌐 Web Application using Flask
* 🎨 Attractive UI with CSS animations
* 📊 Interactive Dashboard (Chart.js)

---

## 🧠 Technologies Used

### 👨‍💻 Programming & Frameworks

* Python
* Flask

### 📚 Machine Learning & NLP

* Scikit-learn
* TF-IDF Vectorizer
* NLTK

### 🌐 Frontend

* HTML
* CSS (Animations, Gradient UI)
* JavaScript (Chart.js)

---

## 🏗️ System Architecture

```
User Input (Review)
        ↓
Text Preprocessing (Cleaning, Stopwords Removal)
        ↓
TF-IDF Vectorization
        ↓
Machine Learning Model (Logistic Regression)
        ↓
Prediction + Confidence Score
        ↓
Trust Score Calculation
        ↓
Web UI + Visualization Dashboard
```

---

## 📂 Project Structure

```
project/
│
├── main.py                # ML Model & Logic
├── app.py                 # Flask Backend
├── requirements.txt       # Dependencies
│
├── templates/
│     └── index.html       # Frontend UI
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd project
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧪 Sample Outputs

### 🔍 Single Review Prediction

**Input:**

```
"This product is amazing!!! Must buy!!!"
```

**Output:**

```
Genuine ✅
Confidence: 82.45%
```

---

**Input:**

```
"Best best best product!!! Buy now!!!"
```

**Output:**

```
Suspicious ⚠️
Confidence: 55.21%
```

---

### 📊 Trust Score Analysis

**Input Reviews:**

```
Amazing product!
Worst product ever
Good quality and value
Best best best product!!!
```

**Output:**

```
Total Reviews: 4
Fake Reviews: 1
Genuine Reviews: 2
Suspicious Reviews: 1
Trust Score: 50%
```

---

## 📈 Visualization

* Pie chart showing:

  * Fake Reviews
  * Genuine Reviews
  * Suspicious Reviews

---

## 🧠 Machine Learning Details

* **Algorithm Used:** Logistic Regression
* **Feature Extraction:** TF-IDF (Term Frequency - Inverse Document Frequency)
* **Dataset Size:** ~40,000 reviews
* **Accuracy Achieved:** ~86%

---

## ⚡ Unique Features (Project Highlights)

* Explainable AI with confidence scores
* Suspicious review classification
* Trust score system for products
* Real-time web interface
* Interactive data visualization

---

## 🔮 Future Enhancements

* 🌐 Deploy as a live web application
* 🧩 Chrome extension for real-time detection
* 🌍 Multi-language support (Tamil + English)
* 🤖 Deep learning models (BERT)
* 👤 Reviewer behavior analysis

---

## 👨‍💻 Author

**Sarvaji M**
B.Tech Information Technology

---

## 📌 Conclusion

This project successfully demonstrates how AI can be used to improve trust in e-commerce platforms by identifying fake reviews and providing transparent insights through explainable models and visual analytics.

---
<img width="1365" height="767" alt="Screenshot 2026-03-19 204535" src="https://github.com/user-attachments/assets/f7de2ddb-b829-4eaf-b168-ccbccc421a64" />


