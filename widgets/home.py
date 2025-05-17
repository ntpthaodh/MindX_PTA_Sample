from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QDialog, QGridLayout, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QPropertyAnimation, QRect, Qt
from widgets.product_item import ProductItemWidget
from controllers.ProductItemController import ProductItemController
from models.ProductItemModel import ProductItemModel
from widgets.product_item_editing import ProductItemEditingWidget
class HomeWidget(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        # Load giao diện từ file .ui
        uic.loadUi("ui/home.ui", self)

        self.controller = controller

        if self.controller.get_current_user():
            current_user = self.controller.get_current_user()
            self.current_user.setText(f"Xin chào, {current_user['username']}!")


        # Cài đặt ban đầu cho btn_menu
        self.btn_menu.setGeometry(0, 0, 50, 50)
        self.btn_menu.clicked.connect(self.toggle_menu)
        self.btn_menu.raise_()
        self.logo.raise_()
        # Tạo slider menu (menu_slider)
        self.menu_slider.setGeometry(-160, 0, 50, 740)  # Ban đầu ẩn ngoài màn hình
        # Cài đặt animation cho menu_slider
        self.animation = QPropertyAnimation(self.menu_slider, b"geometry")
        self.menu_visible = False

        # Kết nối sự kiện cho btn_logout
        self.btn_logout.clicked.connect(self.handle_logout)

        # Kết nối sự kiện cho btn_search    
        self.btn_search.clicked.connect(self.handle_search)
        # Kết nối sự kiện cho btn_create_product
        self.btn_create_product.clicked.connect(self.handle_create_product)

        # Cấu hình ban đầu cho list_product_items (chưa search)
        self.product_controller = ProductItemController()  
        self.initialize()

    def initialize(self):
        # Tạo danh sách sản phẩm ban đầu
        self.product_items = self.product_controller.search_product_items("")
        self.load_product_items()
        
    def clear_layout(self, layout):
        # Xóa tất cả các widget trong layout
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def load_product_items(self):  
        # Nếu đã có layout thì xóa nó đi
        # Nếu không thì tạo mới layout
        if hasattr(self, 'grid_layout'):
            self.clear_layout(self.grid_layout)
        else:
            self.grid_layout = QGridLayout(self.scroll_area_widget_contents)
            self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft) # Căn chỉnh lên trên cùng

        # Cấu hình layout để có 5 cột
        row, col = 0, 0
        for idx, product in enumerate(self.product_items):
            product_widget = ProductItemWidget(product, self, idx)  
            self.grid_layout.addWidget(product_widget, row, col)
            col += 1
            if col == 4:  #5 columns
                col = 0
                row += 1

    def handle_search(self):
        # Get the search term from the input field and update product list.
        search_term = self.input_search.text().strip()
        self.product_items = self.product_controller.search_product_items(search_term)
        self.load_product_items()

    def toggle_menu(self):
        if self.menu_visible:
            # Ẩn menu_slider
            self.animation.setDuration(250)
            self.animation.setStartValue(QRect(0, 0, 210, 740))
            self.animation.setEndValue(QRect(-160, 0, 210, 740))
        else:
            # Hiện menu_slider
            self.animation.setDuration(250)
            self.animation.setStartValue(QRect(-160, 0, 210, 740))
            self.animation.setEndValue(QRect(0, 0, 210, 740))

        self.animation.start()
        self.menu_visible = not self.menu_visible

    def handle_logout(self):
        self.controller.set_current_user(None)
        self.controller.navigate_to("login")

    
    def handle_create_product(self):
        # Create a new product with empty or default values; product_item model
        edit_dialog = ProductItemEditingWidget(None, self)
        edit_dialog.exec() 
        self.initialize()