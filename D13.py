# DAY 13

# 47. Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

# METHOD 1 (Mine)
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

circle = Circle(7)
print(circle.area())



# 48. Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# METHOD 1 (Mine)
class Rectangle():
    def __init__(self, l, b):
        self.length = l
        self.bredth = b
    def area(self):
        return self.length * self.bredth

rectangle = Rectangle(2,3)
print(rectangle.area())



# 49. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# METHOD 1 (Mine)
class Shape():
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length = 0):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

square = Square(5)
print(square.area())
print(Shape().area())



# 50. Please raise a RuntimeError exception.

raise RuntimeError("Kuch to gadbad hai Abhijeet!")