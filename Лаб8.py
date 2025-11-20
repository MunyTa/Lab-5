import tkinter as tk
from tkinter import filedialog

class SimpleFileDialog:
    def __init__(self, root):
        self.root = root
        self.root.title("Выбор файла")
        self.root.geometry("400x150")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Выберите файл")
        title_label.pack(pady=10)

        select_btn = tk.Button(self.root, text="Открыть файл", command=self.select_file)
        select_btn.pack(pady=10)

        self.file_label = tk.Label(self.root, text="Файл не выбран")
        self.file_label.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            self.file_label.config(text=f"Выбран: {file_path}")
        else:
            self.file_label.config(text="Файл не выбран")

root = tk.Tk()
app = SimpleFileDialog(root)
root.mainloop()