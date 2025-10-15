# 🌸 Iris Flower Prediction API

This project is a **Flask-based REST API** that predicts the species of an Iris flower using a trained machine learning model. It takes in sepal and petal measurements and returns the predicted class: `setosa`, `versicolor`, or `virginica`.

---

## 🚀 Features

- 📦 Accepts JSON input with flower measurements
- 🧠 Loads a pre-trained Scikit-learn model
- 🌐 Provides a /predict` endpoint for real-time predictions
- 🔄 Easy to test using tools like **Postman** or **cURL**

---

## 🧠 Model Info

The model is trained on the classic **Iris dataset** and saved as a `.pkl` file using `joblib`.  
Make sure to train and export the model before running the API.  
You can place your trained model at: model/iris_model.pkl.

---

## 📁 Project Structure


├── model/
│ └── iris_model.pkl # Trained ML model (required)
├── app.py # Flask application
└── README.md # Documentation


---

## 📦 Requirements

Install dependencies using:

``bash
pip install flask joblib numpy scikit-learn

▶️ How to Run

Train and save your model as iris_model.pkl inside the model/ folder
(You can create a script like train_model.py using scikit-learn’s Iris dataset)

Start the Flask server:

python app.py


API will be available at: http://127.0.0.1:5000/

📨 API Endpoints
🏠 GET /

Test the base URL.

Response:

🌸 Iris Flower Prediction API is running!

🔮 POST /predict

Predicts the Iris species based on input features.

Request (JSON):

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}


Response (JSON):

{
  "predicted_class": "setosa"
}

🧪 Testing with cURL
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 6.2, "sepal_width": 2.8, "petal_length": 4.8, "petal_width": 1.8}'

⚠️ Notes

Ensure the model file exists at model/iris_model.pkl or you'll get a FileNotFoundError.

You can modify class_names in app.py if using a custom model or label order.

📄 License

This project is licensed under the MIT License
.

🙌 Acknowledgements

Flask

Scikit-learn

UCI Iris Dataset


---

### ✅ Optional Additions You Might Want:
- train_model.py` script to generate the model
- requirements.txt` for easier setup
- Dockerfile (if deploying)

visualization:"C:\Users\Sitharam Chowdary\OneDrive\Pictures\An infographic-style.png"
