import os
from dotenv import load_dotenv
import tweepy

load_dotenv()  # loads variables from .env

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

def get_twitter_client():
    if not TWITTER_BEARER_TOKEN:
        raise Exception("Twitter Bearer Token not found. Please set it in your .env file.")
    client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
    return client
