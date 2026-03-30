def calcular_area(base, altura, tipo):
    if tipo == "cuadrado":
        return base * base
    elif tipo == "rectangulo":
        return base * altura
    elif tipo == "triangulo":
        return (base * altura) / 2
    else:
        return "Tipo no válido"

print(calcular_area(5, 5, "cuadrado"))
print(calcular_area(4, 6, "rectangulo"))
print(calcular_area(4, 6, "triangulo"))
