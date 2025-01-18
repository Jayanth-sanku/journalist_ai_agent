from flask import Flask, request, render_template, jsonify
import requests
from transformers import pipeline

app = Flask(__name__)

API_KEY = ""  # Replace with your News API key

summarizer = pipeline("summarization", model="t5-base")

def fetch_news(query, pageSize=5):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}&pageSize={pageSize}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["articles"]
    else:
        return []

def summarize_articles(articles):
    summarized_news = []
    for article in articles:
        if len(article["content"] or "") > 100:
            summary = summarizer(article["content"], max_length=100, min_length=70, do_sample=False)
            summarized_news.append({
                "title": article["title"],
                "summary": summary[0]["summary_text"],
                "url": article["url"]
            })
    return summarized_news

@app.route('/news', methods=['GET'])
def news():
    query = request.args.get('query', default="latest", type=str)
    pageSize = request.args.get('pageSize', default=5, type=int)
    articles = fetch_news(query, pageSize)
    summarized_news = summarize_articles(articles)
    return jsonify(summarized_news)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
