# Real-Time Sentiment Analysis using MLOps and Cloud

A real-time sentiment analysis application built with Python, FastAPI, and TextBlob, with a deployed web interface and REST API.

## 🚀 Live Demo

- **Live Application:** https://sentiment-mlops-cw6k.onrender.com
- **Interactive API Documentation:** https://sentiment-mlops-cw6k.onrender.com/docs

> **Note:** This project uses Render's free hosting plan. The service may take around 50 seconds or more to respond after a period of inactivity.

## 📌 Overview

This project analyzes text and classifies its sentiment as **Positive, Negative, or Neutral** using TextBlob's sentiment polarity score. FastAPI exposes the prediction functionality through a REST API.

The application is deployed on Render and provides interactive API documentation through Swagger UI.

## 🧰 Tech Stack

- **Language:** Python
- **API Framework:** FastAPI
- **Sentiment Analysis:** TextBlob
- **Web Server:** Uvicorn
- **Deployment:** Render
- **Version Control:** Git and GitHub

## ✨ Features

- Real-time text sentiment prediction
- Positive, negative, and neutral classifications
- Polarity score returned with each prediction
- REST API endpoint using JSON
- Interactive Swagger API documentation
- Publicly accessible deployed application

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/DeepakGIT-CYBER/sentiment-mlops.git
cd sentiment-mlops
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
uvicorn app:app --reload
```

Open http://127.0.0.1:8000 to access the application.

Open http://127.0.0.1:8000/docs to explore and test the API.

## 🔌 API Usage

**Endpoint:** `POST /predict`

**Request body:**

```json
{
  "text": "I love this product. It is amazing!"
}
```

**Example response:**

```json
{
  "sentiment": "Positive",
  "polarity": 0.625
}
```

The polarity value depends on the input text.

## 🧪 Test with cURL

```bash
curl -X POST "https://sentiment-mlops-cw6k.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"I love cloud computing!\"}"
```

## 🐳 Docker

A Dockerfile is included in the repository to containerize the application.

## 🔄 MLOps and Automation

The repository includes a GitHub Actions workflow configured for Google Cloud Run deployment. The current live application is hosted on Render.

**Note:** Automated Google Cloud Run deployment has not been verified as working.

## 📁 Project Structure

```text
sentiment-mlops/
├── .github/
│   └── workflows/
