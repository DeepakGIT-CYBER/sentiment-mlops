from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from textblob import TextBlob
import os

app = FastAPI(title="Sentiment Analysis API with MLOps")


class InputText(BaseModel):
    text: str


@app.post("/predict")
def predict_sentiment(data: InputText):

    text = data.text.strip()
    polarity = TextBlob(text).sentiment.polarity

    # Neutral range for mild/everyday sentences
    if polarity > 0.35:
        label = "Positive"
    elif polarity < -0.35:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "sentiment": label,
        "polarity": polarity
    }


@app.get("/")
def read_root():
    return FileResponse(
        os.path.join(os.path.dirname(__file__), "index.html")
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )