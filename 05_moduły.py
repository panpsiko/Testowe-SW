# https://docs.python.org/3/library/index.html

from turtle import *

def wielokat(n, dl):
    for _ in range(n):
        fd(dl)
        rt(360//n)

# shape("turtle")
# shapesize(2)
for _ in range(30, 200, 10):
    wielokat(5, _)

# poniżej zapobiegamy zamknięciu okna turtle
while True:
    pass