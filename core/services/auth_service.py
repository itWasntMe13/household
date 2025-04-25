# core/services/auth_service.py
import hashlib
from core.models.user import User
from core.utils.db import get_db_connection

class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def register_user(name: str, password: str) -> bool:
        conn = get_db_connection()
        cur = conn.cursor()

        if AuthService.is_name_taken(name):
            return False

        password_hash = AuthService.hash_password(password)
        cur.execute("INSERT INTO users (name, password_hash) VALUES (?, ?)", (name, password_hash))
        conn.commit()
        conn.close()
        return True

    @staticmethod
    def is_name_taken(name: str) -> bool:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE name = ?", (name,))
        user = cur.fetchone()
        conn.close()
        return user is not None

    @staticmethod
    def authenticate_user(name: str, password: str) -> bool:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT password_hash FROM users WHERE name = ?", (name,))
        row = cur.fetchone()
        conn.close()

        if row:
            stored_hash = row[0]
            return stored_hash == AuthService.hash_password(password)
        return False
