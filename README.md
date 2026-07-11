# 📧 Spam Email Detector + AI Assistant

An AI-powered Spam Email Detection web application built using **Machine Learning**, **Logistic Regression**, **Scikit-Learn**, **Streamlit**, and **Groq AI**.

The application classifies emails as **Spam** or **Safe (Ham)**, provides a confidence score, explains the prediction using AI, displays email statistics, analytics dashboard, and maintains prediction history.

---

# 🚀 Features

- 📧 Spam / Safe Email Detection
- 🤖 AI-Powered Email Explanation (Groq LLM)
- 🎯 Confidence Score
- 📊 Spam Risk Meter
- 📈 Analytics Dashboard
- 📜 Prediction History
- 📋 Email Statistics
- 💡 Security Recommendations
- 🌙 Modern Dark UI
- ⚡ Fast Streamlit Web App

---

# 🛠 Technologies Used

- Python
- Streamlit
- Scikit-Learn
- Logistic Regression
- TF-IDF Vectorizer
- Pandas
- NumPy
- Plotly
- Joblib
- Groq API

---

# 📂 Project Structure

```
AI_Project/
│
├── app.py
├── predictor.py
├── chatbot.py
├── train_model.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── data/
│   └── spam.csv
│
├── assets/
│
└── .streamlit/
```

---

# 📊 Machine Learning Model

### Dataset

SMS Spam Collection Dataset

### Preprocessing

- Removed duplicate emails
- Removed unnecessary columns
- TF-IDF Vectorization

### Algorithm

- Logistic Regression

### Model Performance

| Metric | Score |
|---------|---------|
| Accuracy | 97.29% |
| Precision | 98.61% |
| Recall | 82.76% |

---

# 💻 Application Features

### 🔹 Email Classification

Predicts whether an email is:

- 🚨 Spam
- ✅ Safe (Ham)

---

### 🔹 AI Assistant

Explains:

- Why the email is spam or safe
- Suspicious keywords
- Possible scam indicators
- Safety advice

---

### 🔹 Email Statistics

Displays

- Number of Words
- Number of Characters
- Uppercase Letters
- Digits
- Special Characters

---

### 🔹 Analytics Dashboard

Includes

- Total Emails Analyzed
- Spam Emails
- Safe Emails
- Average Confidence
- Spam vs Safe Pie Chart
- Confidence Distribution
- Confidence Trend Graph

---

### 🔹 Prediction History

Stores every prediction with

- Date & Time
- Prediction
- Confidence
- Word Count
- Character Count


# 🚀 Future Improvements

- Email File Upload (.txt)
- Drag & Drop Email Support
- Phishing Detection
- URL Scanner
- Attachment Scanner
- Multi-Model Comparison
- PDF Report Export
- Email Language Detection

---

# 👨‍💻 Author

**Uzair Arain** **(2K23/CSE/106)**
**Abdullah Rajput** **(2K23/CSE/17)**

Data Science | Machine Learning | Artificial Intelligence

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
