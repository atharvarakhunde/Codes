import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# -------------------------------
# 1. Load Dataset
# -------------------------------
data = pd.read_csv("data/dataset.csv")

X = data["text"]
y = data["label"]

# -------------------------------
# 2. Train-Test Split (STRATIFIED)
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# -------------------------------
# 3. TF-IDF Vectorization
# -------------------------------
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.9,
    min_df=1
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# -------------------------------
# 4. Train Model
# -------------------------------
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# -------------------------------
# 5. Prediction
# -------------------------------
y_pred = model.predict(X_test_tfidf)

# -------------------------------
# 6. Evaluation Report
# -------------------------------
print("\n=== Classification Report ===\n")
print(classification_report(y_test, y_pred))

# -------------------------------
# 7. Confusion Matrix
# -------------------------------
labels = sorted(y.unique())
cm = confusion_matrix(y_test, y_pred, labels=labels)

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=labels,
    yticklabels=labels
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()

# -------------------------------
# 8. Save Model
# -------------------------------
with open("model/text_classifier.pkl", "wb") as f:
    pickle.dump(
        {
            "model": model,
            "vectorizer": vectorizer,
            "labels": labels
        },
        f
    )

print("\n✅ Model and vectorizer saved successfully!")
