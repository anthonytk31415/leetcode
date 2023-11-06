import pytest
from regularpolygon import RegularPolygon

@pytest.mark.skip()
def test_length_triangle():
    triangle = RegularPolygon(3,1)
    assert triangle.length == 1

def test_perimeter():
    triangle = RegularPolygon(3,1)
    assert RegularPolygon.get_perimeter(triangle) == 3
