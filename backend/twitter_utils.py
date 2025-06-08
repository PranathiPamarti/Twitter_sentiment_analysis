import time

def fetch_tweets(topic):
    BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {
        'query': topic + " -is:retweet lang:en",
        'max_results': 10,
        'tweet.fields': 'text'
    }
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

    response = requests.get(search_url, headers=headers, params=query_params)
    if response.status_code == 429:
        reset_time = int(response.headers.get("x-rate-limit-reset", 0))
        wait_seconds = max(reset_time - int(time.time()), 60)  # wait at least 60 sec
        print(f"Rate limit hit. Sleeping for {wait_seconds} seconds.")
        time.sleep(wait_seconds)
        return fetch_tweets(topic)  # retry once after waiting
    elif response.ok:
        tweets = response.json().get("data", [])
        return [tweet["text"] for tweet in tweets]
    else:
        print("Twitter API error:", response.status_code, response.text)
        return []
