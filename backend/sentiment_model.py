from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle
from .dummy_tweets import tweets, labels

def train_sentiment_model():
    # Build a pipeline: Vectorizer + Logistic Regression
    model = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', LogisticRegression())
    ])

    model.fit(tweets, labels)

    # Save model to disk
    with open('backend/sentiment_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("Model trained and saved!")

def load_model():
    with open('backend/sentiment_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

if __name__ == "__main__":
    train_sentiment_model()
