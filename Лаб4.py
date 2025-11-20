import tkinter as tk
from tkinter import messagebox


class ListboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Listbox - Выбор элемента")
        self.root.geometry("400x300")

        self.items = [
            "Python", "JavaScript", "Java", "C++", "C#",
            "Ruby", "Go", "Swift", "Kotlin", "Rust"
        ]

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Выберите язык программирования:")
        title_label.pack(pady=10)

        self.listbox = tk.Listbox(self.root, height=8)

        for item in self.items:
            self.listbox.insert(tk.END, item)

        self.listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.listbox.bind('<Double-Button-1>', self.on_double_click)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        select_btn = tk.Button(button_frame, text="Выбрать элемент", command=self.on_select)
        select_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = tk.Button(button_frame, text="Очистить выбор", command=self.clear_selection)
        clear_btn.pack(side=tk.LEFT, padx=5)

        self.selected_label = tk.Label(self.root, text="Выбранный элемент: ничего")
        self.selected_label.pack(pady=10)

    def on_select(self):
        selection = self.listbox.curselection()

        if selection:
            index = selection[0]
            selected_item = self.listbox.get(index)
            self.selected_label.config(text=f"Выбранный элемент: {selected_item}")
            messagebox.showinfo("Выбор", f"Вы выбрали: {selected_item}")
        else:
            messagebox.showwarning("Внимание", "Пожалуйста, выберите элемент из списка!")

    def on_double_click(self, event):
        self.on_select()

    def clear_selection(self):
        self.listbox.selection_clear(0, tk.END)
        self.selected_label.config(text="Выбранный элемент: ничего")


def main():
    root = tk.Tk()
    app = ListboxApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()