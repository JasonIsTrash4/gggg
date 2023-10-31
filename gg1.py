import turtle
turtle.shape('turtle')
turtle.speed(0)
def draw_square(side, color):
    counter = 0
    while counter < 4:
        pencolor(color)
        turtle.fd(side)
        turtle.right(90)
        counter +=1

draw_square(100, "green")
draw_square(110, "red")
draw_square(120, blue)
draw_square(130, purple)
turtle.done()

