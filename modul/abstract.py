from abc import ABC, abstractmethod

class FiturAplikasi(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def tampilkan(self, no):
        pass
