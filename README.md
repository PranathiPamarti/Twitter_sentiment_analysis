# 🐦 Twitter Sentiment Analysis with LLMs

This project analyzes sentiment from tweets about a specific topic or hashtag using a lightweight LLM-based embedding model. It currently uses a proxy API (`AIPipe`) for sentiment classification and is structured to scale up with real Twitter data and better models in the future.

## 🚀 Features

- Input a topic/hashtag (e.g., `AI`, `#dogs`) to analyze
- Collects recent tweets using Twitter API via Tweepy
- Uses LLM-generated embeddings from AIPipe for sentiment classification
- Classifies tweets as Positive / Negative / Neutral
- Frontend UI built with basic HTML/JS to display results
- FastAPI backend with proper CORS support

---

## 🛠️ Tech Stack

- **Frontend:** HTML + JavaScript
- **Backend:** Python (FastAPI)
- **ML/LLM:** AIPipe proxy for OpenAI embeddings
- **Data Collection:** Tweepy (Twitter API)
- **Deployment-ready:** Structure allows easy deployment (e.g., Vercel, Docker)
- **IDE:** Developed in VS Code on Windows

---

## 📂 Project Structure
```text
tweet-llm-sentiment/
│
├── backend/
│ ├── main.py # FastAPI app entrypoint
│ ├── analyze.py # Logic for embedding + sentiment classification
│ ├── test_aipipe.py # Script to test AIPipe connection
│ └── .env # Contains your AIPIPE_API_KEY
│
├── frontend/
│ └── index.html # Basic UI for user input & results display
│
├── requirements.txt # Python dependencies
└── README.md # You're here!
```

## 🚀 Future Enhancements
-Improve Sentiment Classification
Replace basic keyword-based rules with a fine-tuned transformer-based sentiment model (e.g., BERT, DistilBERT) for better accuracy.

-Better LLM Integration
Use a more advanced prompt or fine-tuned model hosted locally or via an API to classify tweet sentiment directly through LLM reasoning.

-Frontend Polishing
Add charts (e.g., pie chart of sentiment distribution) and animate results using libraries like Chart.js or D3.js.

-Database Integration
Store historical analysis results using SQLite or PostgreSQL for dashboarding and trend tracking.

-Authentication and Rate Limits
Secure API access and manage rate limiting to comply with Twitter and OpenAI usage quotas.

-Deployment
Host the backend (FastAPI) on Render, Vercel, or Railway, and deploy the frontend as a static site.

-Multiple Topic Comparison
Allow users to compare sentiment across multiple hashtags or keywords side-by-side.
