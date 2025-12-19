def calcular_area_triangulo():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    return (base * altura) / 2

area = calcular_area_triangulo()
print("Área del triángulo:", area)
