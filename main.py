import random
import math


def generate_points(n: int) -> list:
    points = []
    for i in range(n):
        points.append((random.randint(-100, 100), random.randint(-100, 100)))
    return points
def calc_distance(point1: tuple, point2: tuple) -> float:
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def smallest_triangle(points: list) -> tuple:
    n = len(points)
    min_area = math.inf
    min_triangle = None
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                a = calc_distance(points[i], points[j])
                b = calc_distance(points[j], points[k])
                c = calc_distance(points[k], points[i])
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))

                if area < min_area:
                    min_area = area
                    min_triangle = (points[i], points[j], points[k])
    return min_triangle

while True:
    try:
        n = int(input("Please enter the number of points: "))
        if n < 3:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid number of points (at least 3)")
points = generate_points(n)
min_triangle = smallest_triangle(points)
print(f"The three points that can form the smallest triangle are:  {min_triangle}")