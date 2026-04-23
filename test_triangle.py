from triangle import Triangle, TriangleType

def test_equilateral():
    t = Triangle(7, 7, 7)
    assert t.type == TriangleType.EQUILATERAL

def test_isosceles():
    t = Triangle(7, 7, 8)
    assert t.type == TriangleType.ISOSCELES

def test_scalene():
    t = Triangle(7, 8, 9)
    assert t.type == TriangleType.SCALENE

def test_negative_sides():
    t = Triangle(-7, -8, -9)
    assert t.type == TriangleType.INVALID

def test_zero_sides():
    t = Triangle(0, 0, 0)
    assert t.type == TriangleType.INVALID

def test_invalid_triangle_inequality():
    t = Triangle(1, 1, 5)
    assert t.type == TriangleType.INVALID

def test_invalid_triangle_inequality_permutation():
    t = Triangle(5, 1, 1)
    assert t.type == TriangleType.INVALID

def test_degenerate_triangle():
    t = Triangle(10,3,7)
    assert t.type == TriangleType.INVALID

def test_exact_boundary():
    t = Triangle(2, 3, 5)
    assert t.type == TriangleType.INVALID

def test_float_values():
    t = Triangle(7.1, 7.1, 7.1)
    assert t.type == TriangleType.EQUILATERAL

def test_one_side_too_long():
    t = Triangle(1,1,100)
    assert t.type == TriangleType.INVALID