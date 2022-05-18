import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


class Coord:
    def __init__(self, x1, y1):
        self.point = np.array((x1, y1))

    def distance(self, other):
        return sqrt((self.point[0] - other.point[0])**2 + (self.point[1] - other.point[1])**2)


class Polygon:
    def __init__(self, *args):
        self.points = np.array([point for point in args])

    def perimeter(self):
        distances = [p0.distance(p1) for p0, p1 in zip(self.points[1:], self.points[:-1])]
        distances.append(self.points[0].distance(self.points[-1]))
        return sum(distances)

    def plot(self):
        fig, ax = plt.subplots()
        points = np.array([coord.point for coord in self.points])
        ax.fill(points.T[0], points.T[1], edgecolor='black', linewidth=3)
        plt.show()


class Triangle(Polygon):
    def __init__(self, p0, p1, p2):
        super().__init__(p0, p1, p2)

    def area(self):
        a = self.points[0].distance(self.points[1])
        b = self.points[1].distance(self.points[2])
        c = self.points[2].distance(self.points[0])
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    poly = Polygon(Coord(1, 1), Coord(2, 1), Coord(3, 3), Coord(2, 4), Coord(0, 2))
    poly.plot()
