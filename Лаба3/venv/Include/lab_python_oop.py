import math
from abc import ABCMeta, abstractmethod
class Figure(object):
    __metaclass__ = ABCMeta
@abstractmethod
def S(self, x, y):
    pass

class ColorF:
    def __init__(self, color):
        self.color = color
    @property
    def svoistv(self):
        return self.color

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


class Square(Rectangle):
    def __init__(self, d, color, name="квадрат"):
        self.d=d
        self.color=color
        self.name=name
    def __repr__(self):
            return '{} {} со стороной {} с площадью {}'.format(self.color, self.name, self.d, self.S(self.d))
    def S(self, d):
        return self.d*self.d

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

