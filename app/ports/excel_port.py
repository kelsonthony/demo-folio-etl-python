from abc import ABC, abstractmethod

class ExcelPort(ABC):
    @abstractmethod
    def read_users(self):
        pass
