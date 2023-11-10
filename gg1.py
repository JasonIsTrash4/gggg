import turtle
turtle.shape('turtle')
turtle.speed(1)
turtle.fillcolor('')      
def draw_square(x, color):
    counter = 0
    while counter < 4:
        base_color='green'
        turtle.fd(x)
        turtle.right(90)
        counter += 1

draw_square(100, 'green')
turtle.fd(100)
turtle.left(135)   
turtle.fd(80)
turtle.left(98)
turtle.fd(76)
turtle.goto()
turtle.done()

