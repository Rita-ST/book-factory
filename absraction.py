from abc import ABC, abstractmethod

class Clients(ABC):
    @abstractmethod
    def info(self):
        pass  # Abstract method

class Payment(Clients):
    def info(self):
        return "self.name"

client2 = Payment()
print(client2.info())