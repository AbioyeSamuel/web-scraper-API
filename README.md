**AI News Web Scraper & API**

This project is a web scraper that extracts AI-related news articles, stores them in an SQLite database, and serves them through a FastAPI-based API. The API allows users to retrieve all articles and perform keyword-based search queries.

**1. How to Run the Project**
Prerequisites:

Ensure you have the following installed:

Python (≥3.8)

pip (Python package manager)

Git

Clone the Repository

git clone https://github.com/AbioyeSamuel/web-scraper-API.git

cd web-scraper-API

Install Dependencies:

pip install -r requirements.txt

Run the Web Scraper:

The scraper fetches AI-related news articles and stores them in an SQLite database.

python scraper.py

Start the FastAPI Server:

uvicorn main:app --reload

The API will now be accessible at http://127.0.0.1:8000/

**2. Submission Links**

🔗 Live API

All Articles Endpoint: https://web-scraper-ai-news-a960f7403339.herokuapp.com/articles

Keyword Search Endpoint: https://web-scraper-ai-news-a960f7403339.herokuapp.com/articles?keyword=AI

Swagger UI (API Documentation): https://web-scraper-ai-news-a960f7403339.herokuapp.com/docs


📽 Video Demonstrations

Motivation Video: https://www.loom.com/share/ed80c2c236f74cffbc1c89fcbf5d9093?sid=8529dab8-5848-4c45-a45c-d3e155c98e5e

Task Walkthrough: https://www.loom.com/share/0ebf1c17ba574615b4275b728b503215?sid=816807b3-e109-4585-9378-3d1b75029944

**3. Features Implemented**

Web Scraper – Extracts AI news articles and saves them to a database.

Database Storage – Uses SQLite for lightweight data storage.

API Endpoints – Retrieves all articles and performs keyword searches.

Deployed API – Hosted on Heroku for live access.

**4. Technologies Used**

Python – Backend development

FastAPI – API framework

BeautifulSoup – Web scraping

SQLite – Database storage

Heroku – Deployment