import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, length / 3, depth - 1)
            t.left(angle)

# Setup
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0) # Fastest speed

# Move to starting position
t.penup()
t.goto(-150, 90)
t.pendown()

# Draw 3 sides of the snowflake
for _ in range(3):
    koch_curve(t, 300, 3)
    t.right(120)

turtle.done()
