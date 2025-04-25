import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from widgets.login import LoginWidget
from widgets.register import RegisterWidget
from widgets.home import HomeWidget
from PyQt6.QtCore import pyqtSignal, QObject

class MainController(QObject):    
    user_logged_in = pyqtSignal(str) 
    def __init__(self):
        super().__init__()
        self.current_user = None  # Quản lý trạng thái user hiện tại

        self.screens = {
            "login":  LoginWidget(self),
            "register": RegisterWidget(self),
            "home": HomeWidget(self)
        }

        
        # Hiển thị màn hình đăng nhập đầu tiên
        self.current_screen = self.screens["login"]
        self.current_screen.show()
        
        self.user_logged_in.connect(lambda username: self.screens["home"].current_user.setText(f"Xin chào, {username}!"))


    def set_current_user(self, user):
        self.current_user = user
        self.user_logged_in.emit(user["username"])  # Gửi tín hiệu khi user đăng nhập

    def get_current_user(self):
        return self.current_user
    
    def navigate_to(self, screen_name): #truyền tên màn hình muốn di chuyển đến
        """Điều hướng giữa các màn hình"""
        # if screen_name == "home":
        #     self.login_screen.close()  # Đóng màn hình login
        #     self.home_screen.show()

        # elif screen_name == "register":
        #     self.login_screen.close()
        #     self.register_screen.show()

        # elif screen_name == "login":
        #     self.register_screen.close()
        #     self.login_screen.show()
        self.current_screen.close()
        self.screens[screen_name].show()
        self.current_screen = self.screens[screen_name]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec())
