import sqlite3
from pathlib import Path

DB_PATH = Path("files/db/shopping.db")

def init_db():
    """
    Tworzy bazę danych oraz tabele, jeśli jeszcze nie istnieją.
    """
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabela użytkowników
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Tabela list zakupów
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS shopping_lists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            owner_id INTEGER NOT NULL,
            FOREIGN KEY (owner_id) REFERENCES users (id)
        )
    ''')

    # Tabela przedmiotów zakupowych
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS shopping_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            list_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            is_bought BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (list_id) REFERENCES shopping_lists (id)
        )
    ''')

    # Tabela udostępniania list
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS list_shares (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            list_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (list_id) REFERENCES shopping_lists (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()
    conn.close()
