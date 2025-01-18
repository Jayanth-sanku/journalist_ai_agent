# AI-Powered News Summarizer

## Overview

This project leverages the **News API** and **transformers** library to build an AI-driven news summarization tool. The system fetches news articles, processes them using a pre-trained **T5-base** model to generate concise summaries, and provides users with easily digestible content.

## Key Features:

- **Fetch News**: Utilizes the News API to retrieve recent articles based on user queries.
- **Summarization**: Employs the `pipeline` from `transformers` to summarize lengthy articles using the T5-base model.
- **Customization**: Allows users to specify the number of articles per page and customize summarization parameters (like `max_length`).
- **User-Friendly**: Outputs summarized news articles in JSON format, making it easy for developers and consumers to integrate into their applications.

## Prerequisites

- Python 3.x
- `transformers` library (`pip install transformers`)
- `requests` library (`pip install requests`)
- **News API Key** (Sign up for free at [News API](https://newsapi.org/) and get your API key)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Jayanth-sanku/journalist_ai_agent.git
   ```
