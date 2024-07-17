"""
Julienne Tucker
Grade 7- C6
Hypotenuse Project
"""
import math
def hypotenuse(a, b):
    asquared = a**2
    bsquared = b**2
    sum_of_sqrs = a**2 + b**2
    hypo = math.sqrt(sum_of_sqrs)

    return hypo

print (hypotenuse(3, 4))