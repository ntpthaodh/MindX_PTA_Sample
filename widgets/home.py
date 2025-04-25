from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QScrollArea, QGridLayout, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QPropertyAnimation, QRect
from widgets.product_item import ProductItemWidget
from controllers.ProductItemController import ProductItemController

class HomeWidget(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        # Load giao diện từ file .ui
        uic.loadUi("ui/home.ui", self)

        self.controller = controller

        print("Tìm QLabel current_user:", self.current_user)

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

        self.product_items = ProductItemController().search_product_items("")
        self.load_product_items()

    def load_product_items(self):  
        # Tạo layout QGridLayout
        self.grid_layout = QGridLayout(self.scroll_area_widget_contents)
        self.grid_layout.setSpacing(10)  # Khoảng cách giữa các widget

        # Cấu hình layout để có 5 cột
        row, col = 0, 0
        for product in  self.product_items:
            product_widget = ProductItemWidget(product, self)  
            self.grid_layout.addWidget(product_widget, row, col)
            col += 1
            if col == 4:  #4 columns
                col = 0
                row += 1
    
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
