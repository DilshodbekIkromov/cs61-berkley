# practice section 2 
class Rectangle:
    def __init__(self, width, height):
        self.width =width
        self.height = height
    def area(self):
        return (self.height * self.width)
    def perimeter(self):
        return 2 * (self.height + self.width)

class Dog:
    def __init__(self, name):
        self.name = name 
    def bark(self):
        return self.name + " says woof"
    
class Counter:
    def __init__(self, n=0):
        self.n = n 
    def increment(self):
        self.n = self.n + 1
        return self.n
    def reset(self):
        self.n = 0
    def value(self):
        print(self.n)


# practice section 3
class Widget:
    count = 0 
    def __init__(self, n=0):
        self.n = n
        Widget.count += 1
a = Widget(0)
b = Widget(6)
c = Widget(34)
print(Widget.count)


class Playlist: 
    def __init__(self):
        self.songs = []
    def add(self, s):
        self.songs.append(s)
        

p1 = Playlist(); p2 = Playlist()
p1.add("A"); p2.add("B")
print(p1.songs, p2.songs)

class Point:
    count = 0 
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        Point.count +=1
    @classmethod
    def from_string(cls, s):
        x, y = s.split(",")
        return cls(int(x), int(y))
    def __repr__(self):
        return f"Point ({self.x}, {self.y})"
    
p = Point.from_string("3,4")
print(p) 
      

class Point3D(Point):
    def __init__(self, x, y, z=0):
        super().__init__(x, y)
        self.z = z

print(type(Point3D.from_string("1,2")))

# section 5 
# balance -> public _balance -> internal 

class Temp:
    def __init__(self, celcius):
        self.celcius = celcius
    @property
    def celcius(self):
        return self._celsius
    @celcius.setter
    def celsius(self, v):
        if v < - 273.15:
            raise ValueError("below absolute zero")
        self._celcius = v
    @property
    def fahrenheit(self):
        return self._celcius * 9/5 + 32

class Account:
    def __init__(self, balance):
        self._balance = balance
    @property
    def balance(self):
        return self._balance

# section 6 
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
    def describe(self):
        return f"vehicle with {self.wheels} wheels"

class Car(Vehicle):
    def __init__(self, wheels, brand):
        super().__init__(wheels)
        self.brand = brand
    def describe(self):
        return f"{self.brand}:" + super().describe()

class Person:
    def __init__(self, name):
        self.name = name 
    def greet(self):
        return "Hi, I am " + self.name
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Logger:
    def log(self, msg):
        return f"[LOG] {msg}"
class TimestampLogger(Logger):
    def log(self, msg):
        return "[2026] " + super().log(msg)






