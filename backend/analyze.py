import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

AIPIPE_URL = "https://aipipe.org/openai/v1/embeddings"
AIPIPE_API_KEY = os.getenv("AIPIPE_API_KEY")

headers = {
    "Authorization": AIPIPE_API_KEY,
    "Content-Type": "application/json"
}

def get_embedding(text):
    data = {
        "model": "text-embedding-3-small",
        "input": text
    }
    response = requests.post(AIPIPE_URL, headers=headers, data=json.dumps(data))
    if response.ok:
        return response.json()["data"][0]["embedding"]
    else:
        print("Embedding error:", response.status_code, response.text)
        return None

def classify_sentiment(text):
    embedding = get_embedding(text)
    if not embedding:
        return "Unknown"
    # Naive rule: classify based on presence of strong words (placeholder logic)
    if any(word in text.lower() for word in ["love", "great", "happy", "good"]):
        return "Positive"
    elif any(word in text.lower() for word in ["bad", "terrible", "hate", "worst"]):
        return "Negative"
    else:
        return "Neutral"


def fetch_tweets(topic):
    # Simple Twitter API v2 search call
    # You need to set your BEARER_TOKEN env variable
    BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {
        'query': topic + " -is:retweet lang:en",
        'max_results': 10,
        'tweet.fields': 'text'
    }
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(search_url, headers=headers, params=query_params)
    if response.ok:
        tweets = response.json().get("data", [])
        return [tweet["text"] for tweet in tweets]
    else:
        print("Twitter API error:", response.status_code, response.text)
        return []

def analyze_topic(topic: str):
    tweets = fetch_tweets(topic)
    results = []
    for tweet in tweets:
        sentiment = classify_sentiment(tweet)
        results.append({"tweet": tweet, "sentiment": sentiment})

    return {
        "topic": topic,
        "results": results
    }



