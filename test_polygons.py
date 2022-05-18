import pytest
from polygons import Coord, Polygon, Triangle


@pytest.fixture
def test_square():
    return Polygon(Coord(1, 1), Coord(3, 1), Coord(3, 4), Coord(1, 4))


@pytest.fixture
def test_triangle():
    return Triangle(Coord(1, 1), Coord(3, 1), Coord(3, 4))


def test_distance():
    assert Coord(0, 0).distance(Coord(3, 4)) == 5
    assert Coord(4, 7).distance(Coord(2, 5)) == 8 ** 0.5
    assert Coord(-3, 6).distance(Coord(2, -5)) == (25 + 121) ** 0.5


def test_perimeter(test_square):
    assert test_square.perimeter() == pytest.approx(10)


def test_triangle_area(test_triangle):
    assert test_triangle.area() == pytest.approx(3)
