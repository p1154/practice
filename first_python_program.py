import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("blue")

    anton = turtle.Turtle()
    anton.shape("turtle")
    anton.color("green")
    anton.forward(100)
    anton.right(50)
    anton.forward(100)
    anton.right(50)
    anton.forward(100)
    anton.right(50)
    anton.forward(100)
    anton.right(50)

    window.exitonclick()


draw()
