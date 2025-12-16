import sqlite3
from datetime import datetime

DB_NAME = "database.db"


# -------------------------------
# Database Connection
# -------------------------------
def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


# -------------------------------
# Zoho-compatible datetime format
# Format: dd MMM, yyyy HH:mm:ss
# Example: 13 Dec, 2025 14:05:12
# -------------------------------
def get_zoho_timestamp(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%d %b, %Y %H:%M:%S")


# -------------------------------
# Create Tables (Run once on app start)
# -------------------------------
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            page TEXT,
            device TEXT,
            browser TEXT,
            time_spent INTEGER,
            timestamp TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT,
            event_value TEXT,
            page TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


# -------------------------------
# Log Visitor
# -------------------------------
def log_visitor(page, device, browser, time_spent=0):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO visitors (page, device, browser, time_spent, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        page,
        device,
        browser,
        int(time_spent),
        get_zoho_timestamp()
    ))

    conn.commit()
    conn.close()


# -------------------------------
# Log Event (Clicks, Scrolls, Forms, etc.)
# -------------------------------
def log_event(event_type, event_value, page):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO events (event_type, event_value, page, timestamp)
        VALUES (?, ?, ?, ?)
    """, (
        event_type,
        str(event_value),
        page,
        get_zoho_timestamp()
    ))

    conn.commit()
    conn.close()
