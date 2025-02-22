#https://refactoring.guru/design-patterns/python

#Absract factory pattern

from abc import ABC, abstractmethod
#abstract class
class Shape(ABC):   
    @abstractmethod
    def draw(self):
        pass
 
#concrete class   
class Circle(Shape):
    
    def __init__(self, radius=None):
        self.radius = radius      
    def draw(self):
        return 22/7*self.radius*self.radius
    
#concrete class 
class Square(Shape):
    def __init__(self, side=None):
        self.side = side
        
    def draw(self):
        return self.side*self.side  

#abstract factory   
class ShapeFactory(ABC): 
    @abstractmethod
    def create_circle(self):
        pass
    
    @abstractmethod
    def create_square(self):
        pass
    
#concrete factory

class SimpleShapeFactory(ShapeFactory):
    
    def create_circle(self, radius):
        return Circle(radius)
    
    def create_square(self, side):
        return Square(side)
    

def main():
    factory = SimpleShapeFactory()
    circle = factory.create_circle(7)
    square = factory.create_square(7)
    print(circle.draw())
    print(square.draw())
    
if __name__ == "__main__":
    main()


