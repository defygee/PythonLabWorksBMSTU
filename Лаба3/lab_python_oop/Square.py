from lab_python_oop.Figure import Figure
from lab_python_oop.ColorF import ColorF
from lab_python_oop.Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, d, color, name="квадрат"):
        self.d=d
        self.color=color
        self.name=name
    def __repr__(self):
            return '{} {} со стороной {} с площадью {}'.format(self.color, self.name, self.d, self.S(self.d))
    def S(self, d):
        return self.d*self.d