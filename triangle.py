from dataclasses import dataclass
from enum import Enum, auto


class TriangleType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    INVALID = auto()


@dataclass(frozen=True, slots=True)
class Triangle:
    side1: int
    side2: int
    side3: int

    # a soma de dois lados tem que ser maior que o terceiro

    @property
    def type(self) -> TriangleType:
        a, b, c = self.side1, self.side2, self.side3

        if a <= 0 or b <= 0 or c <= 0:
            return TriangleType.INVALID
        elif a == b == c:
            return TriangleType.EQUILATERAL
        elif a >= b + c or b >= a + c or c >= a + b:
            return TriangleType.INVALID
        elif a == b or a == c or b == c:
            return TriangleType.ISOSCELES
        else:
            return TriangleType.SCALENE

    @property
    # função pra verificar se é retângulo
    def is_right(self) -> bool:
        # verifica se é válido primeiro
        if self.type == TriangleType.INVALID:
            return False
            
        # ordenação para verificar o maior lado 
        # (o maior lado é o lados[2])
        lados = sorted([self.side1, self.side2, self.side3])
        cateto1, cateto2, hipotenusa = lados[0], lados[1], lados[2]
        
        # aplica o teorema de pitágoras pra verificar
        # retorno true/false
        return (cateto1 ** 2) + (cateto2 ** 2) == (hipotenusa ** 2)