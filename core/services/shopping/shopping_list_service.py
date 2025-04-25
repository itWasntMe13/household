from core.models.shopping.shopping_list import ShoppingList
from core.models.shopping.shopping_item import ShoppingItem

class ShoppingListService:
    def __init__(self):
        self.shopping_lists: list[ShoppingList] = []
        self.next_list_id = 1
        self.next_item_id = 1

    def create_list(self, name: str, owner_id: int) -> ShoppingList:
        shopping_list = ShoppingList(id=self.next_list_id, name=name, owner_id=owner_id)
        self.shopping_lists.append(shopping_list)
        self.next_list_id += 1
        return shopping_list

    def get_user_lists(self, owner_id: int) -> list[ShoppingList]:
        return [lst for lst in self.shopping_lists if lst.owner_id == owner_id]

    def add_item_to_list(self, list_id: int, item_name: str) -> ShoppingItem:
        item = ShoppingItem(id=self.next_item_id, name=item_name)
        for lst in self.shopping_lists:
            if lst.id == list_id:
                lst.add_item(item)
                self.next_item_id += 1
                return item
        raise ValueError("Lista nie znaleziona")

    def mark_item_as_bought(self, list_id: int, item_id: int):
        for lst in self.shopping_lists:
            if lst.id == list_id:
                lst.mark_item_as_bought(item_id)

    def clear_bought_items(self, list_id: int):
        for lst in self.shopping_lists:
            if lst.id == list_id:
                lst.clear_bought_items()

    def remove_list(self, list_id: int):
        self.shopping_lists = [lst for lst in self.shopping_lists if lst.id != list_id]
