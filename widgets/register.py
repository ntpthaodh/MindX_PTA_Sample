from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from data.accounts import accounts

class RegisterWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        uic.loadUi("ui/register.ui", self)

        self.btn_login.clicked.connect(self.handle_login)
        self.btn_register.clicked.connect(self.handle_register)

    def handle_login(self):
        """Xử lý đăng ký"""
        self.controller.navigate_to("login")
    def handle_register(self):
        username = self.input_username.text()
        password = self.input_password.text()
        confirm_password = self.input_confirm_password.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đầy đủ thông tin")
        elif password != confirm_password:
            QMessageBox.warning(self, "Thông báo", "Mật khẩu xác nhận không trùng khớp")
        elif self.add_account(username, password):
            self.controller.navigate_to("home")
        else:
            QMessageBox.warning(self, "Thông báo", "Tên đăng nhập đã tồn tại")
           

    def add_account(self, username, password):
        for account in accounts:
            if account["username"] == username:
                return False
        
        accounts.append({"username": username, "password": password})
        # Ghi lại file accounts.py
        with open("data/accounts.py", "w") as file:
            file.write("accounts = " + str(accounts))
        return True