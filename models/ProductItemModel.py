
class ProductItemModel:
    def __init__(self, id, name, price, description, image):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.image = image

    def matches(self, keywords):
        return keywords.lower() in self.name.lower()
    
    @staticmethod
    def from_json(data):
        return ProductItemModel(
                    id=data["id"],
                    name=data["name"],
                    price=data["price"],
                    description=data["description"],
                    image=data["image"]
                )