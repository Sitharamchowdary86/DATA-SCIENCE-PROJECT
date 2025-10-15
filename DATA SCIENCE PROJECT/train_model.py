import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import os

# Create directories
os.makedirs("model", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.to_csv("data/iris.csv", index=False)

# Split data
X = df[iris.feature_names]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline (scaler + model)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, "model/iris_model.pkl")
print("✅ Model trained and saved at model/iris_model.pkl")
