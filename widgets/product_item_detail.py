from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QPixmap

class ProductItemDetailDialog(QDialog):
    def __init__(self, product, parent=None):
        super().__init__(parent)
        self.product = product
        uic.loadUi("ui/product_item_detail.ui", self)

        # Assume in product_item_detail.ui:
        # - QLabel "name" for the product name
        # - QLabel "price" for the product price
        # - QLabel "description" for the product description
        # - QLabel "label" for the product image

        self.name.setText(product.name)
        self.price.setText(f"{product.price} VNĐ")
        self.description.setText(product.description)

        image_pixmap = QPixmap(product.image)
        self.image.setPixmap(image_pixmap)