# Iris Flower Prediction API

## Overview
End-to-end Data Science project:
- Load & preprocess Iris dataset
- Train a RandomForest pipeline
- Deploy model with Flask API

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Train model:
```bash
python train_model.py
```

3. Run API:
```bash
python app.py
```

4. Test endpoint:
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```
