import sqlite3
from django.conf import settings

DB_PATH = settings.DATABASES["default"]["NAME"]


def fetch_all_bloggers():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bloggers;")
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]


def fetch_blogger_by_id(blogger_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bloggers WHERE id = ?;", (blogger_id,))
    row = cursor.fetchone()

    conn.close()
    return dict(row) if row else None


def fetch_blogger_by_slug(slug):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bloggers WHERE slug = ?;", (slug,))
    row = cursor.fetchone()

    conn.close()
    return dict(row) if row else None
