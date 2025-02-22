#chain of responsibility pattern
from abc import ABC, abstractmethod
import typing
class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor
     
    @abstractmethod  
    def handle_request(self, amount):
        pass
        
class ManagerHandler(Handler):
    def handle_request(self, amount):
        if amount < 1000:
            print("Manager handles the request")
        elif self._successor is not None:
             self._successor.handle_request(amount)
    
class DirectorHandler(Handler):
    def handle_request(self, amount):
        if amount > 1000 and amount<10000:
            print("Director handles the request")
        elif self._successor is not None:
            self._successor.handle_request(amount)
            
class CeoHandler(Handler):
    def handle_request(self, amount):
        if amount > 10000:
            print("CEO handles the request")
        else:
            print("No one can handle the request")
    
    
def main():
    manager = ManagerHandler()
    director = DirectorHandler()
    ceo = CeoHandler()
  
    #set the chain
    manager._successor = director
    director._successor = ceo
    
    manager.handle_request(500) 
    manager.handle_request(5000)
    manager.handle_request(15000)
    
if __name__ == "__main__":
    main()
    