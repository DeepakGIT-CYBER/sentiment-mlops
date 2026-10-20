# Real-Time Sentiment Analysis using MLOps and Cloud

## 🚀 Live Demo

- **Live Application:** https://sentiment-mlops-cw6k.onrender.com
- **API Documentation:** https://sentiment-mlops-cw6k.onrender.com/docs

> Note: Hosted on Render's free plan. The first request after inactivity may take around 50 seconds or more.

## 📌 Overview

A real-time sentiment analysis application built with Python, FastAPI, and TextBlob. It classifies text as Positive, Negative, or Neutral and returns a sentiment polarity score through a REST API.

## 🧰 Tech Stack

- Python
- FastAPI
- TextBlob
- Uvicorn
- Render
- Git and GitHub
- Docker

## ✨ Features

- Real-time sentiment prediction
- Positive, Negative, and Neutral classifications
- Polarity score in the API response
- REST API with JSON input and output
- Interactive Swagger documentation
- Live deployment

## ⚙️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app:app --reload
```

Open:
- Application: http://127.0.0.1:8000
- API documentation: http://127.0.0.1:8000/docs

## 🔌 API Usage

**Endpoint:** `POST /predict`

Example request:

```json
{
  "text": "I love this product. It is amazing!"
}
```

Example response:

```json
{
  "sentiment": "Positive",
  "polarity": 0.625
}
```

The polarity score depends on the input text.

## 🐳 Docker

A Dockerfile is included to containerize the application.

## 🔄 MLOps Integration

A GitHub Actions workflow is included and configured for Google Cloud Run deployment. The current live application is hosted on Render. The Google Cloud Run automation has not yet been verified.

## 📁 Project Structure

```text
sentiment-mlops/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app.py
├── index.html
├── requirements.txt
├── Dockerfile
└── README.md
```

## 👨‍💻 Author

**Deepak Reddy**

GitHub: https://github.com/DeepakGIT-CYBER
