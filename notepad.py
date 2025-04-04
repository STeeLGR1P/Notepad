import tkinter as tk
from text_area import TextArea
from file_operations import FileOperations
from text_operations import TextOperations

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Блокнот")
        self.root.geometry("800x600")
        
        # Инициализация компонентов
        self.text_area = TextArea(root)
        self.file_operations = FileOperations(self.text_area)
        self.text_operations = TextOperations(self.text_area)
        
        # Создание меню
        self.create_menu()
    
    def create_menu(self):
        # Создание главного меню
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # Файловое меню
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Новый", command=self.file_operations.new_file)
        self.file_menu.add_command(label="Открыть", command=self.file_operations.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.file_operations.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.root.quit)
        
        # Меню правки
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Правка", menu=self.edit_menu)
        self.edit_menu.add_command(label="Вырезать", command=self.text_operations.cut_text)
        self.edit_menu.add_command(label="Копировать", command=self.text_operations.copy_text)
        self.edit_menu.add_command(label="Вставить", command=self.text_operations.paste_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop() 