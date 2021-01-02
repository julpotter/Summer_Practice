import math
import sys

testlist = [(1, 3), (2, 5), (10, 6), (14, 15), (13, 14), (45, 81)]
min_distance = sys.maxsize
closest_points = [testlist[0], testlist[1]]

for point in testlist:
    i = testlist.index(point) + 1

    for second_point in testlist[i:]:
        y_length = second_point[1] - point[1]
        x_length = second_point[0] - point[0]
        distance = math.sqrt(y_length**2 + x_length**2)
        if distance < min_distance:
            min_distance = distance
            closest_points = [point, second_point]

print(closest_points)




