import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox, QLineEdit, QTextEdit

class LoginWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Окно входа')
        self.setGeometry(400, 300, 300, 200)

        layout = QVBoxLayout()

        title_label = QLabel('Вход в систему')
        login_label = QLabel('Логин:')
        self.login_input = QLineEdit()
        password_label = QLabel('Пароль:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton('Войти')
        login_btn.clicked.connect(self.check_login)

        layout.addWidget(title_label)
        layout.addWidget(login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def check_login(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if login == "admin" and password == "1234":
            self.hide()
            self.main_app.show_main_window()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль!')

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Информационное окно')
        self.setGeometry(350, 250, 350, 200)

        layout = QVBoxLayout()

        title_label = QLabel('Дополнительная информация')
        info_label = QLabel('Это независимое окно.')
        close_btn = QPushButton('Закрыть окно')
        close_btn.clicked.connect(self.close)

        layout.addWidget(title_label)
        layout.addWidget(info_label)
        layout.addWidget(close_btn)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.second_windows = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Главное окно программы')
        self.setGeometry(200, 200, 500, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        welcome_label = QLabel('Добро пожаловать в главное окно!')
        self.text_edit = QTextEdit()

        message_btn = QPushButton('Показать мой текст')
        message_btn.clicked.connect(self.show_message)

        open_window_btn = QPushButton('Открыть новое окно')
        open_window_btn.clicked.connect(self.open_second_window)

        exit_btn = QPushButton('Выйти из программы')
        exit_btn.clicked.connect(self.close)

        layout.addWidget(welcome_label)
        layout.addWidget(self.text_edit)
        layout.addWidget(message_btn)
        layout.addWidget(open_window_btn)
        layout.addWidget(exit_btn)

        central_widget.setLayout(layout)

    def show_message(self):
        text = self.text_edit.toPlainText()
        if text:
            QMessageBox.information(self, 'Ваш текст', f'Вы написали:\n{text}')
        else:
            QMessageBox.warning(self, 'Внимание', 'Пожалуйста, введите текст!')

    def open_second_window(self):
        second_win = SecondWindow()
        second_win.show()
        self.second_windows.append(second_win)

class MultiWindowApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow(self)
        self.main_window = MainWindow()

    def show_main_window(self):
        self.main_window.show()

    def run(self):
        self.login_window.show()
        sys.exit(self.app.exec_())

app = QApplication(sys.argv)
multi_app = MultiWindowApp()
multi_app.run()