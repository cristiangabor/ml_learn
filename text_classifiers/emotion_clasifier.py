from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Text(BaseModel):
    text: str

texts = [
    "I am so happy today!",
    "I am really sad and depressed.",
    "I love this.",
    "This is terrible, I hate it",
    "I am verry exited about the trip.",
    "I feel so lonely and hearthbroken.",
    "I had a wanderfully day",
    "I need some rest. This was bad for me"
]

labels = ['happy', 'sad', 'happy', 'sad', 'happy', 'sad', 'happy', 'sad'] # emotion

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)


# Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the training data
X_train_bow = vectorizer.fit_transform(X_train)
# Transform the test data
X_test_bow = vectorizer.transform(X_test)

# Initialize the classifier
classifier = MultinomialNB()

# Train the classifier
classifier.fit(X_train_bow, y_train)

@app.post("/predict/")
async def predict_sentiment(text: Text):
    # Transform the input text
    text_bow = vectorizer.transform([text.text])
    # Predict the sentiment
    prediction = classifier.predict(text_bow)

    # Return the prediction
    return {"sentiment": prediction[0]}