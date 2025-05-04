from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QScrollArea, QGridLayout, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QPropertyAnimation, QRect, Qt
from widgets.product_item import ProductItemWidget
from controllers.ProductItemController import ProductItemController
class HomeWidget(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        # Load giao diện từ file .ui
        uic.loadUi("ui/home.ui", self)

        self.controller = controller
        self.product_item_controller = ProductItemController()

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

        self.product_controller = ProductItemController()  

        # Kết nối sự kiện cho btn_search    
        self.btn_search.clicked.connect(self.handle_search)
        
        # Cấu hình ban đầu cho list_product_items (chưa search)
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
            self.grid_layout.setSpacing(10)  # Khoảng cách giữa các widget
            self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft) # Căn chỉnh lên trên cùng

        # Cấu hình layout để có 5 cột
        row, col = 0, 0
        for product in  self.product_items:
            product_widget = ProductItemWidget(product, self)  
            self.grid_layout.addWidget(product_widget, row, col)
            col += 1
            if col == 5:  #5 columns
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
