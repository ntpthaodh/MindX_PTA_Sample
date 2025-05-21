from PyQt6.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt6 import uic
from PyQt6.QtGui import QPixmap

class ProductItemEditingWidget(QDialog):
    def __init__(self, product, parent = None, index = 0):
        super().__init__(parent)
        uic.loadUi('ui/product_item_editing.ui', self)
        self.setWindowTitle("Create Product Item")
        self.product = product
        self.index = index
        # Connect the button to choose an image
        self.btn_choose_image.clicked.connect(self.choose_image)

        # If editing, prefill fields
        if product:
            self.setWindowTitle("Update Product Item")
            self.input_name.setText(product.name)
            self.input_price.setText(str(product.price))
            self.input_description.setPlainText(product.description)
            self.selected_image_path = product.image
            pixmap = QPixmap(product.image)
            self.preview_image.setPixmap(pixmap)
        else:
            self.selected_image_path = ""
    def choose_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.preview_image.setPixmap(pixmap)
            self.selected_image_path = file_path

    def accept(self):
         # Retrieve data from UI fields (ensure these names match your .ui file)
        name = self.input_name.text() 
        price = self.input_price.text() 
        description = self.input_description.toPlainText()
        image = self.selected_image_path
        # Save the product if parent has a product_controller with a save method
        parent = self.parent() #HomeWidget
        if parent:
            if self.product and self.index is not None:
                parent.product_controller.update_product_item(self.index, name, price, description, image)
            else:
                parent.product_controller.add_product_item(name, price, description, image)
                QMessageBox.information(self, "Success", "Product created successfully!")
        super().accept()