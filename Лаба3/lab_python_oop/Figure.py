from abc import ABCMeta, abstractmethod
class Figure(object):
    __metaclass__ = ABCMeta
@abstractmethod
def S(self, x, y):
    pass



