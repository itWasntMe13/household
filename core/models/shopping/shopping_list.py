# core/models/shopping/shopping_list.py
from dataclasses import dataclass, field
from typing import List
from core.models.shopping.shopping_item import ShoppingItem

@dataclass
class ShoppingList:
    id: int
    name: str
    owner_id: int
    items: List[ShoppingItem] = field(default_factory=list)

    def add_item(self, item: ShoppingItem):
        self.items.append(item)

    def remove_item(self, item_id: int):
        self.items = [item for item in self.items if item.id != item_id]

    def mark_item_as_bought(self, item_id: int):
        for item in self.items:
            if item.id == item_id:
                item.is_bought = True

    def clear_bought_items(self):
        self.items = [item for item in self.items if not item.is_bought]
