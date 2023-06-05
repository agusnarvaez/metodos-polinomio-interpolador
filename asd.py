import random
import matplotlib.pyplot as plt
import numpy as np

# Generar 20 pares de números con cotas establecidas y ordenarlos según x

# Establecer cotas para los números por teclado
cota_inferior = float(input("Ingrese la cota inferior: "))
cota_superior = float(input("Ingrese la cota superior: "))
pares = []

for _ in range(20):
    x = random.uniform(cota_inferior, cota_superior)
    y = random.uniform(cota_inferior, cota_superior)
    pares.append((x, y))

pares = sorted(pares, key=lambda pair: pair[0])  # Ordenar los pares según x

# Calcular diferencias divididas
def calcular_diferencias_divididas(pares):
    n = len(pares)
    diferencias = [[0] * n for _ in range(n)]

    for i in range(n):
        diferencias[i][0] = pares[i][1]

    for j in range(1, n):
        for i in range(n - j):
            diferencias[i][j] = (diferencias[i + 1][j - 1] - diferencias[i][j - 1]) / (pares[i + j][0] - pares[i][0])

    return diferencias[0]

diferencias_divididas = calcular_diferencias_divididas(pares)

# Calcular polinomio interpolador
def calcular_polinomio_interpolador(pares, diferencias):
    n = len(pares)
    polinomio = []

    for i in range(n):
        termino = [diferencias[i]]
        for j in range(i):
            termino.insert(0, f"(x - {pares[j][0]})")
        polinomio.append(termino)

    return polinomio

polinomio_interpolador = calcular_polinomio_interpolador(pares, diferencias_divididas)

# Obtener grado del polinomio
grado_polinomio = len(polinomio_interpolador) - 1

# Graficar polinomio interpolador y pares de datos
x_vals = np.linspace(cota_inferior, cota_superior, 100)
y_vals = []

for x in x_vals:
    y = 0
    for termino in polinomio_interpolador:
        producto = 1
        for factor in termino[:-1]:
            producto *= eval(factor.replace("x", str(x)))
        y += termino[-1] * producto
    y_vals.append(y)

plt.plot(x_vals, y_vals, label="Polinomio Interpolador")
plt.scatter(*zip(*pares), color="red", label="Pares de Datos")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polinomio Interpolador - Datos Ordenados")
plt.show()

# Ordenar los pares al revés y obtener otro polinomio interpolador
pares_reverso = sorted(pares, key=lambda pair: pair[0], reverse=True)
diferencias_divididas_reverso = calcular_diferencias_divididas(pares_reverso)
polinomio_interpolador_reverso = calcular_polinomio_interpolador(pares_reverso, diferencias_divididas_reverso)
grado_polinomio_reverso = len(polinomio_interpolador_reverso) - 1

# Verificar si los polinomios son iguales
es_mismo_polinomio = polinomio_interpolador == polinomio_interpolador_reverso

# Graficar segundo polinomio interpolador
y_vals_reverso = []

for x in x_vals:
    y = 0
    for termino in polinomio_interpolador_reverso:
        producto = 1
        for factor in termino[:-1]:
            producto *= eval(factor.replace("x", str(x)))
        y += termino[-1] * producto
    y_vals_reverso.append(y)

plt.plot(x_vals, y_vals_reverso, label="Polinomio Interpolador Reverso")
plt.scatter(*zip(*pares), color="red", label="Pares de Datos")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polinomio Interpolador Reverso - Datos Ordenados")
plt.show()

# Desordenar los pares de datos
random.shuffle(pares)

# Calcular nuevo polinomio interpolador
diferencias_divididas_desordenado = calcular_diferencias_divididas(pares)
polinomio_interpolador_desordenado = calcular_polinomio_interpolador(pares, diferencias_divididas_desordenado)
grado_polinomio_desordenado = len(polinomio_interpolador_desordenado) - 1

# Graficar tercer polinomio interpolador
y_vals_desordenado = []

for x in x_vals:
    y = 0
    for termino in polinomio_interpolador_desordenado:
        producto = 1
        for factor in termino[:-1]:
            producto *= eval(factor.replace("x", str(x)))
        y += termino[-1] * producto
    y_vals_desordenado.append(y)

plt.plot(x_vals, y_vals_desordenado, label="Polinomio Interpolador Desordenado")
plt.scatter(*zip(*pares), color="red", label="Pares de Datos")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polinomio Interpolador - Datos Desordenados")
plt.show()

# Imprimir información de los polinomios
print("Grado del Polinomio Interpolador (Datos Ordenados):", grado_polinomio)
print("Grado del Polinomio Interpolador Reverso:", grado_polinomio_reverso)
print("¿Es el mismo polinomio?:", es_mismo_polinomio)
print("Grado del Polinomio Interpolador (Datos Desordenados):", grado_polinomio_desordenado)

# Mostrar el polinomio interpolador en forma polinómica sin factorizar
polinomio_str = "P(x) = "
for termino in polinomio_interpolador:
    coeficiente = termino[-1]
    grado = len(termino) - 2
    if grado == 0:
        polinomio_str += f"{coeficiente:.2f} "
    elif grado == 1:
        polinomio_str += f"{coeficiente:.2f}x + "
    else:
        polinomio_str += f"{coeficiente:.2f}x^{grado} + "
polinomio_str = polinomio_str[:-3]  # Eliminar el último "+"
print(polinomio_str)