import json
from models.ProductItemModel import ProductItemModel

class ProductItemController:
    def __init__(self):
        self.product_item_list = []
        self.load_from_json("data/product_items.json")
    
    def get_product_item_list(self):
        return self.product_item_list
    
    def load_from_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            product_items_data = json.load(file)
            for item in product_items_data:
                product_item = ProductItemModel.from_dict(item)
                self.product_item_list.append(product_item)

    def save_to_json(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            product_items_data = []
            for item in self.product_item_list:
                item_data = item.to_dict()
                product_items_data.append(item_data)
            json.dump(product_items_data, file, indent=4)
    
    def search_product_items(self, search_term):
        return [item for item in self.product_item_list if item.matches(search_term)]
    
    def filter_product_items_by_price(self, min_price, max_price):
        return [item for item in self.product_item_list if item.is_within_price_range(min_price, max_price)]

    def add_product_item(self, name, price, description, image):
        product_item = ProductItemModel(None, name, price, description, image)
        self.product_item_list.append(product_item)
        self.save_to_json("data/product_items.json")
    
    def delete_product_item(self, index):
        self.product_item_list.pop(index)   
        self.save_to_json("data/product_items.json")