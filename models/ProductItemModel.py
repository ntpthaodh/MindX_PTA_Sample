import uuid

class ProductItemModel:
    def __init__(self, id, name, price, description, image):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.price = price
        self.description = description
        self.image = image

    def matches(self, search_term):
        return (search_term.lower() in self.name.lower() or
                search_term.lower() in self.description.lower())
    
    def is_within_price_range(self, min_price, max_price):
        return min_price <= self.price <= max_price
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "image": self.image
        }
    
    @staticmethod
    def from_dict(data):
        return ProductItemModel(
            id=data.get("id"),
            name=data["name"],
            price=data["price"],
            description=data["description"],
            image=data["image"]
        )