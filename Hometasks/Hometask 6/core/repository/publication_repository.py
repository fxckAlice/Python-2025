import sqlite3
from django.conf import settings

DB_PATH = settings.DATABASES["default"]["NAME"]


def fetch_publications_by_blogger_id(blogger_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM publications WHERE blogger_id = ? ORDER BY published_at DESC;",
        (blogger_id,)
    )
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]


def fetch_publication_by_id(publication_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM publications WHERE id = ?;",
        (publication_id,)
    )
    row = cursor.fetchone()

    conn.close()
    return dict(row) if row else None


def fetch_all_publications():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM publications ORDER BY published_at DESC;")
    rows = cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]
