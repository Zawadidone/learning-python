import turtle


def draw_square(square):

    for i in range(0, 4):
        square.forward(100)
        square.right(90)


def create_art():
    window = turtle.Screen()
    window.bgcolor("red")

    # creates the turtle brad and draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed("fast")

    for i in range(1, 36):
        draw_square(brad)
        brad.right(10)

    # creates the turtle angie and draws a circle
    angie = turtle.Turtle()
    angie.circle(100)
    angie.shape("arrow")
    angie.color("blue")

    window.exitonclick()


create_art()
