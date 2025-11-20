import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit, QLineEdit, QMessageBox, QFileDialog

class SimpleNotesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Простой редактор заметок')
        self.setGeometry(100, 100, 500, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        title_label = QLabel('Название заметки:')
        self.title_input = QLineEdit()

        content_label = QLabel('Текст заметки:')
        self.content_text = QTextEdit()

        save_btn = QPushButton('Сохранить в файл')
        save_btn.clicked.connect(self.save_note)

        layout.addWidget(title_label)
        layout.addWidget(self.title_input)
        layout.addWidget(content_label)
        layout.addWidget(self.content_text)
        layout.addWidget(save_btn)

        central_widget.setLayout(layout)

    def save_note(self):
        title = self.title_input.text().strip()
        content = self.content_text.toPlainText().strip()

        if not title:
            QMessageBox.warning(self, 'Внимание', 'Введите название заметки!')
            return

        file_path, _ = QFileDialog.getSaveFileName(self, 'Сохранить заметку', f'{title}.txt', 'Текстовые файлы (*.txt)')

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                QMessageBox.information(self, 'Успех', 'Заметка сохранена!')
            except Exception as e:
                QMessageBox.critical(self, 'Ошибка', f'Ошибка сохранения: {str(e)}')

app = QApplication(sys.argv)
notes_app = SimpleNotesApp()
notes_app.show()
sys.exit(app.exec_())