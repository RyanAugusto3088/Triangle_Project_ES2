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
    t = Triangle(10, 3, 7)
    assert t.type == TriangleType.INVALID

def test_exact_boundary():
    t = Triangle(2, 3, 5)
    assert t.type == TriangleType.INVALID

def test_float_values():
    t = Triangle(7.1, 7.1, 7.1)
    assert t.type == TriangleType.EQUILATERAL

def test_one_side_too_long():
    t = Triangle(1, 1, 100)
    assert t.type == TriangleType.INVALID

# ── Triângulo Retângulo ────────────────────────────────────────

def test_right_triangle_3_4_5():
    """Terna pitagórica clássica → is_right True."""
    t = Triangle(3, 4, 5)
    assert t.is_right is True

def test_right_triangle_5_12_13():
    """Outra terna pitagórica → is_right True."""
    t = Triangle(5, 12, 13)
    assert t.is_right is True

def test_right_triangle_sides_out_of_order():
    """Hipotenusa não precisa ser o último argumento."""
    t = Triangle(5, 3, 4)
    assert t.is_right is True

def test_right_triangle_large_values():
    """Terna pitagórica com valores grandes."""
    t = Triangle(30000, 40000, 50000)
    assert t.is_right is True

def test_not_right_obtuse():
    """Triângulo obtusângulo não é retângulo."""
    t = Triangle(4, 6, 8)  
    assert t.is_right is False

def test_not_right_equilateral():
    """Equilátero nunca é retângulo."""
    t = Triangle(5, 5, 5)
    assert t.is_right is False

def test_invalid_is_right_returns_false():
    """Triângulo inválido → is_right deve retornar False sem quebrar."""
    t = Triangle(0, 4, 5)
    assert t.is_right is False

def test_right_scalene_type_and_is_right():
    """3-4-5 é escaleno E retângulo ao mesmo tempo."""
    t = Triangle(3, 4, 5)
    assert t.type == TriangleType.SCALENE
    assert t.is_right is True