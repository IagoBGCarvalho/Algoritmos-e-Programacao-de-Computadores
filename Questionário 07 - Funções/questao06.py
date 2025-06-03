def areas(A, B, C):
    area_retangulo = (A * B)
    area_triangulo = ((B * C) // 2)
    area_trapzeio = ((C + B) * A) // 2
    tupla_areas = (area_retangulo, area_triangulo, area_trapzeio)
    return tupla_areas