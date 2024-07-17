import turtle
bob = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=0.56, height=0.92, startx=0, starty=0)
bob.speed(50)
bob.pensize(2)
bob.ht()

def magnet(turt):
    global saved_pos, saved_h
    saved_pos = turt.pos()
    saved_h = turt.heading()

def move(turt):
    turt.setpos(saved_pos)
    turt.seth(saved_h)

def arm(seg_size, turn_size, num_segments):
    for x in range(2):
        magnet(bob)
        for i in range(num_segments):
            if i % 2 == 0:
                bob.pd()
                bob.fd(seg_size)
            else:
                if x == 0:
                    bob.pd()
                    bob.lt(turn_size)
                    bob.fd(seg_size)
                    bob.rt(turn_size)
                else:
                    bob.pd()
                    bob.rt(turn_size)
                    bob.fd(seg_size)
                    bob.lt(turn_size)
                    
        
        bob.pu()
        move(bob)
    bob.pd()
    magnet(bob)
def mandala(seg_size, turn_size, num_arms, num_segments):
    turn_angle = 360/num_arms
    for i in range(12):
        arm(seg_size, turn_size, num_segments)
        bob.lt(turn_angle)
        magnet(bob)
        arm(seg_size, turn_size, num_segments)
        bob.lt(turn_angle)
bob.width(7)
bob.color(0, 6 ,1)
mandala(80, 20, 12, 5)
bob.width(5)
bob.color(1, 0, 1)
mandala(60, 90, 12, 5)
bob.width(4)
bob.color(0, 1, 5)
mandala(100, 48, 12, 5)
bob.width(6)
bob.color(3, 0, 7)
mandala(70, 53, 12, 5)