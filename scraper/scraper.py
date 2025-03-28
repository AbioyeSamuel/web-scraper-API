import requests
import sqlite3
from bs4 import BeautifulSoup
import datetime
import os

# URL to scrape – here using TechCrunch AI tag for demonstration
SCRAPE_URL = "https://techcrunch.com/tag/artificial-intelligence/"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, "articles.db")

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT UNIQUE NOT NULL,
            summary TEXT,
            published DATE
        )
    ''')
    conn.commit()
    conn.close()

def store_article(title, url, summary, published):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO articles (title, url, summary, published)
            VALUES (?, ?, ?, ?)
        ''', (title, url, summary, published))
        conn.commit()
    except sqlite3.IntegrityError:
        # Article already exists
        print(f"Article already exists: {title}")
    finally:
        conn.close()

def fetch_article_summary(url):
    """
    Given an article URL, fetch the page and extract the summary from the 
    <p id="speakable-summary" class="wp-block-paragraph"> element.
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Summary not available."
        
        article_soup = BeautifulSoup(response.text, 'html.parser')
        summary_tag = article_soup.find('p', id='speakable-summary')
        if summary_tag:
            return summary_tag.get_text(strip=True)
        else:
            return "Summary not available."
    except Exception as e:
        print(f"Error fetching summary for {url}: {e}")
        return "Summary not available."

def scrape_articles():
    response = requests.get(SCRAPE_URL)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # For TechCrunch articles, the links are contained in <a> tags with class 'loop-card__title-link'
    articles = soup.find_all('a', class_='loop-card__title-link')
    
    for a in articles:
        title = a.get_text(strip=True)
        url = a['href']
        
        # Fetch summary from the article page
        summary = fetch_article_summary(url)
        
        # Find the first <time> element following the <a> tag
        time_tag = a.find_next("time", class_="loop-card__time")
        if time_tag and time_tag.has_attr("datetime"):
            # Extract just the date part from the ISO datetime string
            published = time_tag["datetime"][:10]
        else:
            published = datetime.date.today().isoformat()
        
        print(f"Storing article: {title}")
        store_article(title, url, summary, published)

if __name__ == "__main__":
    init_db()
    scrape_articles()
