from fastapi import FastAPI, HTTPException, Query
import sqlite3
from typing import List, Optional
from pydantic import BaseModel
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, "articles.db")

app = FastAPI(title="Article API", description="API to search and retrieve scraped articles.")

# Pydantic model for an article
class Article(BaseModel):
    id: int
    title: str
    url: str
    summary: Optional[str] = None
    published: str

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/articles", response_model=List[Article])
def read_articles(keyword: Optional[str] = Query(None, description="Keyword to filter article titles")):
    conn = get_db_connection()
    cursor = conn.cursor()

    if keyword:
        query = "SELECT * FROM articles WHERE title LIKE ?"
        keyword_param = f"%{keyword}%"
        cursor.execute(query, (keyword_param,))
    else:
        query = "SELECT * FROM articles"
        cursor.execute(query)

    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        raise HTTPException(status_code=404, detail="No articles found")

    # Convert rows to list of dictionaries
    articles = [Article(**dict(row)) for row in rows]
    return articles

@app.get("/")
def read_root():
    return {"message": "Welcome to the Article API. Use /articles endpoint to search for articles."}
