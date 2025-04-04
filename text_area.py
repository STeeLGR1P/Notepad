import tkinter as tk
from interfaces import ITextArea

class TextArea(ITextArea):
    def __init__(self, root):
        self.text_widget = tk.Text(root, wrap="word")
        self.text_widget.pack(expand=True, fill="both")
    
    def get_text(self):
        return self.text_widget.get(1.0, tk.END)
    
    def set_text(self, text):
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(1.0, text)
    
    def clear(self):
        self.text_widget.delete(1.0, tk.END)
    
    def get_widget(self):
        return self.text_widget