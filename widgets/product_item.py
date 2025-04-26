from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt6.QtGui    import QPixmap
from PyQt6 import uic

CARD_W, CARD_H = 200, 300          # chiều cao cố định
IMG_H          = 140

class ProductItemWidget(QWidget):
    def __init__(self, product, parent=None):
        super().__init__(parent)
        self.product = product
        uic.loadUi("ui/product_item.ui", self)

        self.name.setText(product.name) 
        self.price.setText(f"{product.price} VNĐ")

        image_pixmap = QPixmap(product.image)
        self.image.setPixmap(image_pixmap)
        self.image.setMaximumHeight(200)  # Giới hạn chiều cao của hình ảnh

        self.setFixedSize(200, 300)  # Thiết lập kích thước cố định cho widget