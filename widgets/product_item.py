from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt6.QtGui    import QPixmap
from PyQt6 import uic

CARD_W, CARD_H = 200, 300          # chiều cao cố định
IMG_H          = 140

class ProductItemWidget(QWidget):
    def __init__(self, product, parent=None):
        super().__init__(parent)
        self.product = product
        # Layout cho mỗi sản phẩm
        # self.layout = QVBoxLayout(self)

        # # Thêm tên sản phẩm
        # self.name = QLabel(self.product['name'], self)
        # self.name.setStyleSheet("""
        #             color: "red"
        #             font-size: 16px;
        #             """)
        # self.layout.addWidget(self.name)

        # # Thêm ảnh sản phẩm
        # self.image = QLabel(self)
        # image_pixmap = QPixmap(self.product['image'])
        # self.image.setPixmap(image_pixmap)
        # # Đặt ảnh tự động thay đổi kích thước để phù hợp với QLabel
        # self.image.setFixedSize(200,140)
        # self.image.setScaledContents(True)
        # # Thêm ảnh vào layout
        # self.layout.addWidget(self.image)

        # # Thêm giá sản phẩm
        # self.price = QLabel(f"{self.product['price']} VND", self)
        # self.layout.addWidget(self.price)

        # # Thêm mô tả sản phẩm
        # self.description = QLabel("", self)
        # self.description.setWordWrap(True)
        # self.layout.addWidget(self.description)
        
        # self.setFixedSize(200, 300)
        uic.loadUi('ui/product_item.ui', self)
        self.name.setText(product['name'])
        
        # Đặt hình ảnh sản phẩm
        image_pixmap = QPixmap(product['image'])
        self.image.setPixmap(image_pixmap)
        self.image.setScaledContents(True)  

        # Đặt giá sản phẩm
        self.price.setText(f"{product['price']} VND")
        
        self.setFixedSize(250, 300)  # Adjust as needed