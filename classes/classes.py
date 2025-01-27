#this function is about an animal
class Animal:
    #name1 = "roshan"
    def __init__(self, name):
        self.name = name
        
        
    def speak(self):
        return f"{self.name} make a sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} make woof woof"
    
any_animal = Animal("buddy")
print(any_animal.speak())


dog = Dog("Tony")
print(dog.speak())
#print(Animal.name1)
    
    
    





"""class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    pass

dalmation = Dog("buddy")
print(dalmation.speak())"""



"""class Walker:
    def __init__(self, name):
        self.name = name
    def walk(self):
        return f"{self.name} can walk"

class Swimmer:
    def __init__(self, name):
        self.name = name
    def swim(self):
        return f"{self.name} can swim"
    
class Duck (Walker, Swimmer):
    pass


black_duck = Duck("indian_duck")
print(black_duck.walk())
print(black_duck.swim())"""


"""class EncapsulatedClass:
    def __init__(self):
        self.__private_var ="I am Roshan"
        
    def get_private_var(self):
        return self.__private_var
    
enclass = EncapsulatedClass()
print(enclass.get_private_var())
"""

"""class EncapsulatedClass:
    def __init__(self):
        self.var ="I am Roshan"
        
    def __repr__(self):
        return self.var
    
enclass = EncapsulatedClass()
print(enclass)
print(enclass.var)"""


# class to explain encapsulation and get, set, delete and display methods

"""class EncapsulationClassLearn:
    
    def __init__(self):
        self.__private_var = "Roshan"
        
    #getter method    
    def get_private_var (self):
        return self.__private_var
    
    #setter method
    def set_private_var(self, value):
        self.__private_var = value
        
    #deleter method
    def del_private_var(self):
        del self.__private_var
        
    #display method
    def display_private_var(self):
        print(f"Current value of self.__private_var is {self.__private_var}")
        
    
        
        
enclass = EncapsulationClassLearn()
print(enclass.get_private_var())
enclass.display_private_var()
enclass.set_private_var("Deepa")
print(enclass.get_private_var())
enclass.display_private_var()
enclass.del_private_var()"""




"""class Bird:
    
    def character(self):
        return "can fly"
    
class Penguin(Bird):
    
    def character(self):
        return "cannot fly"
    
crow = Bird()
print(crow.character())


black_penguin = Penguin()
print(black_penguin.character())"""



"""class MyClass:
    class_var = 0
    
    @classmethod
    def increment_var(cls):
        cls.class_var += 1
        return cls.class_var
        
print(MyClass.increment_var())"""
        

"""class MathOperations:
    
    @staticmethod
    def add(a,b):
        return a+b
    
addition = MathOperations().add(2,3)
print(addition)"""


"""class Temperature:
    
    def __init__(self, celsius):
        self._celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    
    
    @celsius.setter
    def celsius(self, value):
        if value < -273:
            return f"temperature cannot be below -273"
        else:
            self._celsius = value
        
    @property
    def faretheit(self):
        return self._celsius*9/5+32
    
    
temp = Temperature(0)
print(temp.celsius)
print(temp.faretheit)
temp.celsius=40
print(temp.celsius)
print(temp.faretheit)

"""

"""from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area():
        pass
    @abstractmethod
    def circumference():
        pass
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 22/7*self.radius*self.radius
    
    def circumference(self):
        return 2*22/7*self.radius"""
        
        
"""class Secret:
    def __init__(self):
        self.public_info = "Public"
        self.__private_info = "Private"

    def __private_method(self):
        return "Private"
    
 
    def access_private(self):
        return self.__private_method()
    
confidential = Secret()
print(confidential.public_info)
print(confidential.access_private())
#print(confidential.__private_info)
#print(confidential.__private_method())"""


"""
class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)
    
    def __mul__(self,other):
        return Point(self.x*other.x, self.y*other.y) 
    
    def __truediv__(self,other):
        return Point(self.x/other.x, self.y/other.y)
    
    def __str__(self):
         return f"the value is ({self.x}, {self.y})"
     
    def __len__(self):
         return len(str(self.x))
    

p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1+p2
p4 = p1-p2
p5 = p1*p2
p6=p1/p2
print(f"the addition of points is ({p3.x},{p3.y})")
print(f"the substraction of the points is ({p4.x, p4.y})")
print(f"the multiplication of the points is ({p5.x}, {p5.y})")
print(f"the division of the points is ({p6.x}, {p6.y})")
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(len(p1))"""




"""
import dataclasses

@dataclasses.dataclass
class Employees:
    name: str
    age: int
    position: str
    
@dataclasses.dataclass
class Point:
    x:int
    y:int
    z:int
    
first_emp = Employees("roshan", 26, "TPM")
print(first_emp.name)

p1 = Point(1,2,3)
p2 = Point(4,5,6)
print(p1.x)"""


"""class Base:
    def __init__(self, name):
        self.name = name
        print("bass init")
        
    def base_method(self):
        print("this is the base class")
        
        
class Derived(Base):
    def __init__(self, name, age):
        super().__init__(name)
        print("derived init")
        self.age = age
    
    def base_method(self):
        print("this is the base class: checking overriding")
        
    def derived_method(self):
        print("this is derived class")


example = Derived("roshan",23)
example.base_method()"""



"""class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        
        
with FileManager('example.txt', 'w') as file:
    file.write('Hello, world!')"""
    

# added a file for emergency fix
