import math
class Shape:
    def __init__(self,height=None,width=None):
        self.height = height
        self.width = width
        
    def area(self):
        raise NotImplementedError("derived classes need to override this method")
class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)
    def area(self):
        return self.height* self.width
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def area(self):
      return math.pi * self.radius ** 2
    


    