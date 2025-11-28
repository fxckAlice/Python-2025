import sqlite3
from pathlib import Path

BLOGGERS_DATA = [
    {
        "id": 1,
        "slug": "julia-verba",
        "name": "Julia Verba",
        "category": "education",
        "description": "Educational blogger",
        "followers_count": "1.2M",
        "youtube_url": "https://youtube.com/example",
        "instagram_url": "https://instagram.com/example",
        "tiktok_url": "https://tiktok.com/example"
    },
    {
        "id": 2,
        "slug": "mike-tech",
        "name": "Mike Tech",
        "category": "technology",
        "description": "Tech reviews and tutorials",
        "followers_count": "800K",
        "youtube_url": "https://youtube.com/example",
        "instagram_url": "https://instagram.com/example",
        "tiktok_url": "https://tiktok.com/example"
    }
]

PUBLICATIONS_DATA = [
    {
        "id": 1,
        "blogger_id": 1,
        "type": "video",
        "title": "How to learn Python fast",
        "short_description": "Quick guide for beginners",
        "published_at": "2024-01-10",
        "url": "https://youtube.com/example"
    },
    {
        "id": 2,
        "blogger_id": 1,
        "type": "article",
        "title": "Best study techniques",
        "short_description": "Scientific methods",
        "published_at": "2024-02-15",
        "url": "https://example.com/post"
    },
    {
        "id": 3,
        "blogger_id": 2,
        "type": "video",
        "title": "Top 5 budget laptops",
        "short_description": "2024 comparison",
        "published_at": "2024-01-28",
        "url": "https://youtube.com/example"
    }
]

NEWS_DATA = [
    {
        "id": 1,
        "title": "New collaboration announced",
        "short_description": "Famous bloggers launch a joint project",
        "date": "2024-02-01",
        "source_url": "https://news.example.com"
    },
    {
        "id": 2,
        "title": "Tech blogger hits milestone",
        "short_description": "1M subscribers celebration",
        "date": "2024-02-10",
        "source_url": "https://news.example.com"
    }
]

DB_PATH = Path("db.sqlite3")

def init_sqlite():
    print("INIT_SQLITE CALLED")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bloggers (
            id INTEGER PRIMARY KEY,
            slug TEXT,
            name TEXT,
            category TEXT,
            description TEXT,
            followers_count TEXT,
            youtube_url TEXT,
            instagram_url TEXT,
            tiktok_url TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publications (
            id INTEGER PRIMARY KEY,
            blogger_id INTEGER,
            type TEXT,
            title TEXT,
            short_description TEXT,
            published_at TEXT,
            url TEXT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY,
            title TEXT,
            short_description TEXT,
            date TEXT,
            source_url TEXT
        );
    """)

    cursor.execute("SELECT COUNT(*) FROM bloggers;")
    bloggers_count = cursor.fetchone()[0]

    if bloggers_count == 0:
        for b in BLOGGERS_DATA:
            cursor.execute("""
                INSERT INTO bloggers 
                (id, slug, name, category, description, followers_count, youtube_url, instagram_url, tiktok_url) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                b["id"],
                b["slug"],
                b["name"],
                b["category"],
                b["description"],
                b["followers_count"],
                b["youtube_url"],
                b["instagram_url"],
                b["tiktok_url"]
            ))

        for p in PUBLICATIONS_DATA:
            cursor.execute("""
                INSERT INTO publications
                (id, blogger_id, type, title, short_description, published_at, url)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                p["id"],
                p["blogger_id"],
                p["type"],
                p["title"],
                p["short_description"],
                p["published_at"],
                p["url"]
            ))

        for n in NEWS_DATA:
            cursor.execute("""
                INSERT INTO news
                (id, title, short_description, date, source_url)
                VALUES (?, ?, ?, ?, ?)
            """, (
                n["id"],
                n["title"],
                n["short_description"],
                n["date"],
                n["source_url"]
            ))

        conn.commit()

    conn.close()
    return True
