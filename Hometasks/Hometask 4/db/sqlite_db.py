import sqlite3
import time
from .base import Database

class SQLiteDatabase(Database):
    def __init__(self, path: str):
        self._path = path
        self._conn: sqlite3.Connection | None = None

    def _log(self, level: str, message: str) -> None:
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{ts}] [{level}] {message}")

    def connect(self) -> None:
        try:
            self._conn = sqlite3.connect(self._path)
            self._conn.execute("PRAGMA foreign_keys=ON")
            self._log("INFO", f"connected to sqlite at {self._path}")
        except Exception as e:
            self._log("ERROR", f"connect failed: {e}")
            self._conn = None

    def close(self) -> None:
        if self._conn is not None:
            try:
                self._conn.close()
                self._log("INFO", "connection closed")
            except Exception as e:
                self._log("ERROR", f"close failed: {e}")
            finally:
                self._conn = None

    def is_connected(self) -> bool:
        return self._conn is not None

    def execute(self, sql: str, params: tuple | dict | None = None) -> int:
        if not self._conn:
            self._log("ERROR", "execute attempted without connection")
            return 0
        try:
            cur = self._conn.cursor()
            self._log("SQL", f"{sql} | params={params}")
            cur.execute(sql, params or ())
            self._conn.commit()
            rc = cur.rowcount if cur.rowcount is not None else 0
            self._log("INFO", f"success rowcount={rc}")
            return 0 if rc is None or rc < 0 else rc
        except Exception as e:
            self._log("ERROR", f"execute failed: {e}")
            return 0

    def executemany(self, sql: str, seq_of_params: list[tuple] | list[dict]) -> int:
        if not self._conn:
            self._log("ERROR", "executemany attempted without connection")
            return 0
        try:
            cur = self._conn.cursor()
            self._log("SQL", f"{sql} | batch size={len(seq_of_params)}")
            cur.executemany(sql, seq_of_params)
            self._conn.commit()
            rc = cur.rowcount if cur.rowcount is not None else len(seq_of_params)
            self._log("INFO", f"success rowcount={rc}")
            return 0 if rc is None or rc < 0 else rc
        except Exception as e:
            self._log("ERROR", f"executemany failed: {e}")
            return 0

    def fetchone(self, sql: str, params: tuple | dict | None = None) -> tuple | None:
        if not self._conn:
            self._log("ERROR", "fetchone attempted without connection")
            return None
        try:
            cur = self._conn.cursor()
            self._log("SQL", f"{sql} | params={params}")
            cur.execute(sql, params or ())
            row = cur.fetchone()
            self._log("INFO", "fetchone success")
            return row
        except Exception as e:
            self._log("ERROR", f"fetchone failed: {e}")
            return None

    def fetchall(self, sql: str, params: tuple | dict | None = None) -> list[tuple]:
        if not self._conn:
            self._log("ERROR", "fetchall attempted without connection")
            return []
        try:
            cur = self._conn.cursor()
            self._log("SQL", f"{sql} | params={params}")
            cur.execute(sql, params or ())
            rows = cur.fetchall()
            self._log("INFO", f"fetchall success rows={len(rows)}")
            return rows
        except Exception as e:
            self._log("ERROR", f"fetchall failed: {e}")
            return []
