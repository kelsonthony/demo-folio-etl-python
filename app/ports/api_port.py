from abc import ABC, abstractmethod

class ApiPort(ABC):
    @abstractmethod
    def send_user(self, user_json):
        pass