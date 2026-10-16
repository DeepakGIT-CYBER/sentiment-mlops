# Real-Time Sentiment Analysis using MLOps and Cloud

## 🚀 Overview
This project demonstrates how to deploy a simple machine learning model for real-time sentiment analysis using **FastAPI**, **TextBlob**, and **Google Cloud Run**.  
It also integrates a lightweight **MLOps pipeline** using **GitHub Actions** for automated deployment.

## 🧰 Tech Stack
- **Python 3.9**
- **FastAPI**
- **TextBlob**
- **Google Cloud Run**
- **GitHub Actions (MLOps)**

## ⚙️ Run Locally
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
Then open: http://127.0.0.1:8000/docs

## ☁️ Deploy to Google Cloud Run
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/sentiment-api
gcloud run deploy sentiment-api --image gcr.io/YOUR_PROJECT_ID/sentiment-api --platform managed
```

## 🧪 Test
```bash
curl -X POST "https://YOUR_URL/predict" -H "Content-Type: application/json" -d '{"text": "I love cloud computing!"}'
```

## 📊 Example Output
```json
{
  "sentiment": "Positive",
  "polarity": 0.5
}
```

## 🧠 MLOps Integration
Every push to `main` branch automatically triggers deployment using GitHub Actions.
