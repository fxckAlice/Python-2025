import sqlite3
from django.conf import settings

DB_PATH = settings.DATABASES["default"]["NAME"]


def fetch_latest_news():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM news ORDER BY date DESC;")
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]
