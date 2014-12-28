import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("blue")

    anton = turtle.Turtle()
    anton.shape("turtle")
    anton.color("green")

    for i in range(0,36):
        anton.right(10)
        for i in range (0,4):
            anton.forward(100)
            anton.right(90)
    
    window.exitonclick()


draw()
