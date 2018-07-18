import math

class Simple_Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return (self.a-self.b)
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b

class Scientific_Calculator:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b
    def sine(self):
        return math.sin(self.a)
    def cosine(self):
        return math.cos(self.a)
    def powerof(self):
        return math.pow(self.a, self.b)
    def square_root(self):
        return math.sqrt(self.a)
