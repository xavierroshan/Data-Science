#https://refactoring.guru/design-patterns/python

## Observer pattern 

class SubjectNotification:
    def __init__(self):
        self.observers = []
        
    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        return self.observers
    
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        return self.observers
    
    def notify(self, notification):
        for observer in self.observers:
            observer.update(notification)
            
    

class Observer:
    
    def __init__(self, name):
        self.name = name
        
    def update(self, notification):
        print (f"Notification received by: {self.name}: {notification}")
        
    
observer1 = Observer("roshan")
observer2 = Observer("Deepa")

subject = SubjectNotification()
subject.add_observer(observer1)
subject.add_observer(observer2)
subject.notify("msg")
