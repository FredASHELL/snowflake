import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(10)
t.color("blue")
t.pensize(2)

def draw_branch():
    for _ in range(3):
        for _ in range(3):
            t.forward(30)
            t.backward(30)
            t.right(45)
        t.left(90)
        t.backward(30)
        t.left(45)
    t.right(90)
    t.forward(90)

# Draw the full snowflake
for _ in range(6):
    draw_branch()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(60)

turtle.done()
