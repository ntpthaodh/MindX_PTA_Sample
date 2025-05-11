from PyQt6.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt6 import uic
from PyQt6.QtGui import QPixmap

class ProductItemEditingWidget(QDialog):
    def __init__(self, product, parent = None):
        super().__init__(parent)
        uic.loadUi('ui/product_item_editing.ui', self)
        self.setWindowTitle("Create Product Item")
        # Connect the button to choose an image
        self.btn_choose_image.clicked.connect(self.choose_image)

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
        parent = self.parent()
        if parent:
            parent.product_controller.add_product_item(name, price, description, image)
            QMessageBox.information(self, "Success", "Product item created successfully!")
            # Close the dialog after creation
        super().accept()
        