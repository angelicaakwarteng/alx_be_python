class Shape:
    def __init__(self):
        pass

    def area(self):
        return NotImplementedError
        
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()


class Circle(Shape):
    def __init__(self):
        super().__init__()