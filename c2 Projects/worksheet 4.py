# Worksheet 4 - Abhiram Avasarala C5
# Part 1
def sum_of_multiples(a, b, c):
    x = 0
    for i in range(a,b):
        if i % c == 0:
            x = x+i
    return x
print(sum_of_multiples(2, 10, 3))
        
# Part 2
def average_ints_loop(a, b):
    count = 0
    total = 0
    for i in range(a, b):
        count = count + 1
        total = total + i
    average = (total + b)/(count + 1)
    return average
print(average_ints_loop(12, 15))

# Part 3
import turtle
fred = turtle.Turtle()
def poly(ns, length, turt):
    angle = 360/ns
    for i in range(ns):
        turt.fd(length)
        turt.rt(angle)
poly(6, 150, fred)

