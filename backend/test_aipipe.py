import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

AIPIPE_URL = "https://aipipe.org/openai/v1/embeddings"
AIPIPE_API_KEY = os.getenv("AIPIPE_API_KEY")

if not AIPIPE_API_KEY:
    print("Error: AIPIPE_API_KEY not found in environment variables.")
    exit(1)

headers = {
    "Authorization": AIPIPE_API_KEY,  # Check if your key needs 'Bearer ' prefix (usually no for aipipe)
    "Content-Type": "application/json"
}

def test_embedding():
    data = {
        "model": "text-embedding-3-small",
        "input": "Hello world! Testing AIPipe connection."
    }
    try:
        response = requests.post(AIPIPE_URL, headers=headers, data=json.dumps(data))
        if response.ok:
            embedding = response.json()["data"][0]["embedding"]
            print(f"Success! Embedding received with length {len(embedding)}.")
            print(f"First 5 dims: {embedding[:5]}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print("Exception during request:", str(e))

if __name__ == "__main__":
    test_embedding()
