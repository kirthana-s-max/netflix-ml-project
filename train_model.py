"""
train_model.py
Train a Logistic Regression model on Netflix data
and save it as model.pkl using joblib.
"""

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


def train_and_save(data_path: str, model_path: str = "model.pkl") -> None:
    """Train model on Netflix data and save to disk."""

    df = pd.read_csv(data_path)

    # encode target: Movie=0, TV Show=1
    le = LabelEncoder()
    df["type_encoded"] = le.fit_transform(df["type"])

    # feature and target
    X = df[["release_year"]].fillna(0)
    y = df["type_encoded"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"Accuracy: {acc:.2%}")

    joblib.dump(model, model_path)
    joblib.dump(le, "label_encoder.pkl")
    print("Model saved as model.pkl")


if __name__ == "__main__":
    train_and_save("netflix_cleaned.csv") 