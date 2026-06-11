from abc import ABC, abstractmethod

class Clients(ABC):
    @abstractmethod
    def balance(self):
        pass  # Abstract method

class Payment(Clients):
    def balance(self):
        return "self.balance"

client2 = Payment(34534)
print(client2.balance())