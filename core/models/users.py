# core/models/user.py
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    password_hash: str
