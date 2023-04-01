import turtle
import random
random.seed()
Dict = {'Flower': 5, 'Star Vortex': 10, 'Hexagonal Vortex': 3, 'Square Vortex': 4, 'Triangular Vortex': 6, 'Detailed Flower': 7, 'Octagonal Vortex Flower': 8, 'Nightmare Vortex': 9, 'Star Rose with Eyes': 11, 'Basic Rotated Sun': 1,
        'Star Nightmare Flower': 12, 'Tendriled Star Nightmare Flower': 13, 'Thin Spiral Star Vortex': 14, 'Deodecagonal Star Vortex': 15, 'Eye': 91, 'Tendriled Eye': 100, 'Arc Reactor': 120, 'Cyborg Eye': 180, 'Sun': 36}
# n = int(random.random()*360)
n = Dict['Star Vortex']
print(n)
spiral = turtle.Turtle()
spiral.speed(0)
a = n-2
a = a*180
a = a/n
a = a-1
for i in range(n*18):
    spiral.forward(i*2)
    spiral.right(a)
turtle.done()
