import turtle

joe = turtle.Turtle()
bob = turtle.Turtle()

# This is supposed to draw a hexagon using the turtle
# passed into the parameter turt:
def hexagon(turt):
    for i in range(5):
        bob.fd(100)
        bob.rt(90)

hexagon(joe)