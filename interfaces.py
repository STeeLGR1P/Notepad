from abc import ABC, abstractmethod

class IFileOperations(ABC):
    @abstractmethod
    def new_file(self):
        pass
    
    @abstractmethod
    def open_file(self):
        pass
    
    @abstractmethod
    def save_file(self):
        pass

class ITextOperations(ABC):
    @abstractmethod
    def cut_text(self):
        pass
    
    @abstractmethod
    def copy_text(self):
        pass
    
    @abstractmethod
    def paste_text(self):
        pass

class ITextArea(ABC):
    @abstractmethod
    def get_text(self):
        pass
    
    @abstractmethod
    def set_text(self, text):
        pass
    
    @abstractmethod
    def clear(self):
        pass 