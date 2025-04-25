# core/models/shopping/shopping_item.py
from dataclasses import dataclass

@dataclass
class ShoppingItem:
    id: int
    name: str
    is_bought: bool = False
