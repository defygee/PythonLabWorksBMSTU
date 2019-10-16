from lab_python_oop.Figure import Figure
from lab_python_oop.ColorF import ColorF
import math
class Circle(Figure):
    def __init__(self, R, color, name="круг"):
        self.R = R
        self.color=color
        color=ColorF(self.color)
        self.name=name

    def S(self,R):
        return self.R * self.R*math.pi
    def __repr__(self):
            return '{} {} радиусом {} с площадью {}'.format(self.color, self.name, self.R, self.S(self.R))

