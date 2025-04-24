from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from data.accounts import accounts


class LoginWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        uic.loadUi("ui/login.ui", self)

        # Kết nối nút đăng nhập
        self.btn_login.clicked.connect(self.handle_login)
        self.btn_register.clicked.connect(self.handle_register)
    def handle_register(self):
        """Xử lý đăng ký"""
        self.controller.navigate_to("register")

    def handle_login(self):
        """Xử lý đăng nhập"""
        global current_user  # Để lưu tài khoản user hiện tại
        username = self.input_username.text()
        password = self.input_password.text()

        account = self.validate_credentials(username, password)
        if account:
            self.controller.set_current_user(account) # Lưu thông tin tài khoản vào biến global
            self.controller.navigate_to("home")
            self.input_username.setText("")
            self.input_password.setText("")
        else:
            QMessageBox.warning(self, "Thông báo", "Sai tên đăng nhập hoặc mật khẩu!")

    def validate_credentials(self, username, password):
        """Kiểm tra thông tin đăng nhập"""
        for account in accounts:
            if account["username"] == username and account["password"] == password:
                return account  # Trả về tài khoản nếu hợp lệ
        return None
    