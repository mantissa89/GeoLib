import math

# Square
def area_sqr(side):
    return side * side  

def perim_sqr(side):
    return side * 4

# Rectangle
def area_rect(length, width):
    return length * width

def perim_rect(length, width):
    return (2 * length) + (2 * width)

# Triangle
def area_tri(base, height):
    return (base * height) / 2

def perim_tri(a, b, c): # a, b and c are indicative of the lengths of each side
    return a + b + c

def pythagoras_hyp(a, b):
    csq = (a * a) + (b * b)
    return math.sqrt(csq)