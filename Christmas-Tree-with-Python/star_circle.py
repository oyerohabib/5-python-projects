import turtle

def draw_star_circle():
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(250)
        turtle.left(245)
        print(turtle.pos())
        if abs(turtle.pos()) < 1:
            print("last")
            print(abs(turtle.pos()))
            break
    turtle.end_fill()
    turtle.done()

draw_star_circle()