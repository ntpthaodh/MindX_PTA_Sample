from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt6.QtGui    import QPixmap
from PyQt6 import uic
from widgets.product_item_detail import ProductItemDetailDialog  # Import the detail dialog

class ProductItemWidget(QWidget):
    def __init__(self, product, parent=None, index =0):
        super().__init__(parent)
        self.product = product
        self.index = index
        uic.loadUi('ui/product_item.ui', self)
        self.name.setText(product.name)
        
        # Đặt hình ảnh sản phẩm
        image_pixmap = QPixmap(product.image)
        self.image.setPixmap(image_pixmap)
        self.image.setScaledContents(True)  
        self.image.setMaximumHeight(223)  # Giới hạn chiều cao hình ảnh

        # Đặt giá sản phẩm
        self.price.setText(f"{product.price} VND")
        
        self.setFixedSize(250, 350)  # Adjust as needed

    def mousePressEvent(self, event):
        detail_dialog = ProductItemDetailDialog(self.product, self, self.index)
        detail_dialog.exec()