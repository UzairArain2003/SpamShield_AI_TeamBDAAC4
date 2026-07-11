import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report
)

# ---------------- LOAD DATA ----------------

df = pd.read_csv("data/spam.csv", encoding="latin-1")

# ---------------- CLEAN DATA ----------------

df = df[['v1', 'v2']]
df.columns = ['label', 'message']

df.drop_duplicates(inplace=True)

print("=" * 50)
print("Dataset Shape:", df.shape)
print("=" * 50)

# ---------------- FEATURES ----------------

X = df["message"]
y = df["label"]

# ---------------- TRAIN TEST SPLIT ----------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ---------------- TF-IDF ----------------

vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# ---------------- MODEL ----------------

model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

# ---------------- PREDICTION ----------------

y_pred = model.predict(X_test)

# ---------------- METRICS ----------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label="spam")
recall = recall_score(y_test, y_pred, pos_label="spam")

print("\nModel Performance")
print("-" * 50)

print(f"Accuracy : {accuracy*100:.2f}%")
print(f"Precision: {precision*100:.2f}%")
print(f"Recall   : {recall*100:.2f}%")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

# ---------------- SAVE ----------------

joblib.dump(model, "models/spam_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("\nModel Saved Successfully!")