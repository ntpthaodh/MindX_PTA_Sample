from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtGui import QPixmap

class ProductItemDetailDialog(QDialog):
    def __init__(self, product, parent=None, index = 0):
        super().__init__(parent)
        self.product = product
        self.index = index
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
        self.btn_del.clicked.connect(self.delete_product)

    def delete_product(self):
        parent = self.parent()     #ProductItemWidget
        while parent and not hasattr(parent, "product_controller"):
            parent = parent.parent() #HomeWidget
        if parent:
            #Gọi đến hàm delete_product_item trong ProductItemController của HomeWidget
            parent.product_controller.delete_product_item(self.index)
            QMessageBox.information(self, "Success", "Product item deleted successfully!")
            #Cập nhật lại danh sách sản phẩm sau khi xóa
            parent.initialize()
        super().accept()