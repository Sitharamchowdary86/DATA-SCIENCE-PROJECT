from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = "model/iris_model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError("Model not found! Run train_model.py first.")
model = joblib.load(model_path)

# Class names
class_names = ['setosa', 'versicolor', 'virginica']

@app.route("/")
def home():
    return "🌸 Iris Flower Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        features = [data['sepal_length'], data['sepal_width'],
                    data['petal_length'], data['petal_width']]
        features = np.array(features).reshape(1, -1)
        pred = model.predict(features)[0]
        return jsonify({"predicted_class": class_names[pred]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
