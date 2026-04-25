def calcular_nivel(python, matematicas):
    return (python + matematicas) / 2


def evaluar(nivel, experiencia):
    if nivel >= 85 and experiencia:
        return "Acceso Total"
    elif nivel >= 70:
        return "Acceso Limitado"
    else:
        return "Acceso Denegado"


def sistema_ia(nombre, python, matematicas, experiencia=False):
    nivel = calcular_nivel(python, matematicas)
    resultado = evaluar(nivel, experiencia)
    return nombre, nivel, resultado

nombre, nivel, resultado = sistema_ia(
    nombre="Santiago",
    python=60,
    matematicas=60,
    experiencia=False
)

print("Nombre:", nombre)
print("Nivel:", nivel)
print("Resultado:", resultado)