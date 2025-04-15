import math
def add(a, b):
    return a + b

# <<<<<<< HEAD
def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

# =======
# One function per operation, in order.
"""
import math
def add(a, b):
    answer = a + b
    return answer
def subtract(a, b):
    answer = a - b
    return answer
def mul(a, b):
    answer = a * b
    return answer
>>>>>>> 0199d376043995971a5d83c90330c9200430df01
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a
# <<<<<<< HEAD

def log(a, b):
    if b <= 0:
        raise ValueError
    return log(a, b)

def exp(a, b):
    return a ** b
# =======
def logarithm(a, b):
    if b < 0:
        return ValueError
    return math.log(a, b)
def exp(a, b):
    answer = a ** b
    return answer

def square_root(a):
    if a < 0:
        return ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
# >>>>>>> 0199d376043995971a5d83c90330c9200430df01


