import json
from models.ProductItemModel import ProductItemModel

class ProductItemController:
    def __init__(self):
        self.product_item_list = []
        self.load_from_json("data/product_items.json")
    
    def load_from_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                product_item = ProductItemModel.from_json(data = item)
                self.product_item_list.append(product_item)
    
    def find_product_item_by_name(self, keyword):
        result = []
        for item in self.product_item_list:
            if item.matches(keyword):
                result.append(item)
                
        return result
