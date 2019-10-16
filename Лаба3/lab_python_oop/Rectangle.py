from lab_python_oop.Figure import Figure
from lab_python_oop.ColorF import ColorF

class Rectangle (Figure):
    def __repr__(self):
            return '{} {} высотой {} и шириной {} с площадью {}'.format(self.color, self.name, self.height, self.width, self.S(self.width, self.height))
    def __init__(self, width, height, color, name="прямоугольник"):
        self.width = width
        self.height = height
        self.color=color
        self.name=name
    def S(self, width, height):
        return self.width * self.height