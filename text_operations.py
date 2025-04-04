from interfaces import ITextOperations

class TextOperations(ITextOperations):
    def __init__(self, text_area):
        self.text_area = text_area
    
    def cut_text(self):
        self.text_area.get_widget().event_generate("<<Cut>>")
    
    def copy_text(self):
        self.text_area.get_widget().event_generate("<<Copy>>")
    
    def paste_text(self):
        self.text_area.get_widget().event_generate("<<Paste>>") 