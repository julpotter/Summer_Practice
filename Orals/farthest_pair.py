from turtle import *
from random import randint

# Create the points
N = 20
RANGE = 300
points = [(randint(0, RANGE), randint(0, RANGE)) for i in range(N)]


# parameter points : list of points
# Returns a list of two points [(x1, y1), (x2, y2)] that are
# furthest apart in the input list p
def farthest_pair(p):
    # Your work here
    return [p[0], p[1]]


# parameter points : list of points
# Returns a number B so that the vertical line x=B splits the input
# list into two equal parts.
# You may assume that no two points in the input list p have the same
# x-coordinate.
def vertical_divider(p):
    # Your work here
    return 0


# Create the drawing environment
setup(width=RANGE + 200, height=RANGE + 200, startx=0, starty=0)
speed("fastest")  # important! turtle is intolerably slow otherwise
tracer(False)  # This too: rendering the 'turtle' wastes time
penup()
hideturtle()

# Draw the points
for i in range(N):
    goto(points[i][0] - RANGE / 2, points[i][1] - RANGE / 2)
    dot(5)

# Connect the farthest pair
pair = farthest_pair(points)
color('red')
goto(pair[0][0] - RANGE / 2, pair[0][1] - RANGE / 2)
pendown()
goto(pair[1][0] - RANGE / 2, pair[1][1] - RANGE / 2)
penup()

# Draw the vertical dividing line
B = vertical_divider(points)
color('blue')
goto(B - RANGE / 2, -RANGE / 2)
pendown()
goto(B - RANGE / 2, RANGE / 2)
penup()

hideturtle()
done()