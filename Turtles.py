import turtle

n = 1
# Making sure that the user inputs a valid value in the given range before proceeding.
while n > 90 or n < 3:
    n = int(input("Please input a number between 3 and 90. "))

spiral = turtle.Turtle()
spiral.speed(0)
# Calculating the angle of the spiral
a = (n - 2) * 180 / n - 1
# Drawing the spiral
for i in range(7200):
    spiral.forward(i / 3)
    spiral.right(180 - a)

turtle.done()
