"""SQLite helpers for dice roll storage."""

from __future__ import annotations

import sqlite3
from pathlib import Path

DEFAULT_DB_PATH = Path("dice_rolls.db")


def get_connection(db_path: Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    return sqlite3.connect(db_path)


def init_db(db_path: Path = DEFAULT_DB_PATH) -> None:
    with get_connection(db_path) as con:
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS rolls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                result TEXT NOT NULL,
                rolled_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        con.commit()


def insert_roll(result: str, db_path: Path = DEFAULT_DB_PATH) -> None:
    with get_connection(db_path) as con:
        con.execute("INSERT INTO rolls (result) VALUES (?)", (result,))
        con.commit()


def fetch_counts(db_path: Path = DEFAULT_DB_PATH) -> list[tuple[str, int]]:
    with get_connection(db_path) as con:
        rows = con.execute(
            """
            SELECT result, COUNT(*) as n
            FROM rolls
            GROUP BY result
            ORDER BY n DESC, result ASC
            """
        ).fetchall()
    return rows

