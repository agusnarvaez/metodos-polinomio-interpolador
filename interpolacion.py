import numpy as np
import warnings
import math
import matplotlib.pyplot as plt
import sympy as sp
from sympy import simplify, symbols, degree, degree_list
from decimal import Decimal, ROUND_DOWN
from tabulate import tabulate
import copy
from scipy.optimize import newton
from numpy import poly1d

# Ignorar advertencias de numpy
warnings.simplefilter(action='ignore', category=FutureWarning)
# Establecer opciones de alineación
options = {"floatfmt": ".0f", "stralign": "center"}

def generar_pares_aleatorios():
    """
    Genera 20 pares de números aleatorios en el rango de 0 a 100 inclusive.
    :return:
    """
    pares = []
    x_set = set()  # Conjunto para almacenar las coordenadas x generadas

    while len(pares) < 20:
        x = np.random.randint(0, 101)  # Generar x en el rango de 0 a 100 inclusive
        y = np.random.randint(0, 101)  # Generar y en el rango de 0 a 100 inclusive

        # Verificar si ya se generó un par con la misma coordenada x
        if x not in x_set:
            x_set.add(x)  # Agregar la coordenada x al conjunto
            pares.append((x, y))  # Agregar el par (x, y) a la lista de pares

    return pares

def ordenar_pares(pares):
    """
    Ordena los pares de menor a mayor por la coordenada x y en caso de empate por la coordenada y.
    :param pares:
    :return:
    """
    paresOrdenados = copy.copy(pares)
    # Ordenar primero por X y después por Y
    paresOrdenados.sort(key=lambda x: (x[0], x[1]))
    return paresOrdenados

def invertir_pares(pares):
    """
    Ordena los pares de mayor a menor por la coordenada x y en caso de empate por la coordenada y.
    :param pares: Lista de pares de coordenadas (x, y).
    :return: Lista ordenada de pares de coordenadas.
    """
    paresInvertidos = copy.copy(pares)
    paresInvertidos.sort(key=lambda x: (-x[0], x[1]))
    return paresInvertidos

def calcular_diferencias_divididas(x, y):
    """
    Calcula las diferencias divididas de Newton.
    :param x:
    :param y:
    :return:
    """
    n = len(x)
    diferencias = [y[0]]
    for j in range(1, n):
        diferencias.append((y[j] - y[j - 1]) / (x[j] - x[j - 1]))

        for i in range(j - 1, 0, -1):
            diferencias[i] = (diferencias[i] - diferencias[i - 1]) / (x[j] - x[j - 1])

    return diferencias

def calcular_coeficientes(x, y):
    """
    Calcula los coeficientes del polinomio interpolador.
    :param x:
    :param y:
    :return:
    """
    diferencias = calcular_diferencias_divididas(x, y)
    coeficientes = [diferencias[0]]
    for i in range(1, len(diferencias)):
        coeficientes.append(diferencias[i])
    return coeficientes

def calcular_raiz_polinomio(puntos, x0):
    x = [p[0] for p in puntos]
    y = [p[1] for p in puntos]
    coeficientes = calcular_coeficientes(x, y)
    polinomio = poly1d(coeficientes)
    raiz = newton(polinomio, x0)
    return raiz

def calcular_polinomio_interpolador(puntos):
    """
    Calcula el polinomio interpolador de Newton.
    :param puntos:
    :return:
    """
    x = [p[0] for p in puntos]
    y = [p[1] for p in puntos]
    coeficientes = calcular_coeficientes(x, y)
    n = len(coeficientes)
    polinomio = f"{coeficientes[0]:.6f}"
    for i in range(1, n):
        polinomio += f" + {coeficientes[i]:.6f}"
        for j in range(i):
            polinomio += f" * (x - {x[j]})"
    return simplify(polinomio)

def obtener_grado_polinomio(polinomio):
    grado = degree(polinomio)
    return grado

def graficar_polinomios_interpoladores(polinomio, puntos):
    """
    Grafica el polinomio interpolador junto con los puntos de datos.
    :param polinomio:
    :param puntos:
    """
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.array([p[0] for p in puntos])
    y = np.array([p[1] for p in puntos])

    # Obtener valores únicos de x y encontrar límites mínimo y máximo
    unique_x = np.unique(x)
    x_min, x_max = np.min(unique_x), np.max(unique_x)
    unique_y = np.unique(y)
    y_min, y_max = np.min(unique_y), np.max(unique_y)

    # Generar puntos para graficar el polinomio
    x_grafico = np.linspace(x_min, x_max, 100)
    eval_polinomio = sp.lambdify(sp.symbols('x'), polinomio)
    y_grafico = eval_polinomio(x_grafico)

    plt.figure(figsize=(8, 6))
    plt.plot(x_grafico, y_grafico, label='Polinomio Interpolador')
    plt.scatter(x, y, color='red', label='Puntos de Datos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polinomio Interpolador')
    plt.legend()
    plt.grid(True)
    plt.show()

def formateo_impresion(polinomio, pares):
    print(tabulate(pares, headers=["x", "y"], tablefmt="fancy_grid"))  # Imprimir pares en forma de tabla
    print("Grado Polinomio:")
    print(obtener_grado_polinomio(polinomio))
    print("Polinomio Interpolador:")
    print(polinomio)

def main():
    """
    Función principal.
    """
    # Presentación del TP
    print("Métodos Numéricos: TP Polinomio Interpolador")
    print("Integrantes:")
    print("    - Venturini, Tomás")
    print("    - Narvaez, Agustín")
    # * Genero números aleatorios
    #pares_desordenados = generar_pares_aleatorios()
    pares_desordenados = [(2,3),(1,-1),(0,2),(-1,5),(-2,7),(-3,9)]
    print(pares_desordenados)
    # * Ordeno los pares y los muestro, calculo el polinomio y lo muestro
    pares_ordenados = ordenar_pares(pares_desordenados)
    polinomio = calcular_polinomio_interpolador(pares_ordenados)

    raiz_polinomio = calcular_raiz_polinomio(pares_ordenados, -3)
    print("Raíz polinomio:")
    print(raiz_polinomio)

    formateo_impresion(polinomio, pares_ordenados)

    # * Invierto los pares y los muestro, calculo el polinomio y lo muestro
    pares_invertidos = invertir_pares(pares_ordenados)
    polinomio_invertido = calcular_polinomio_interpolador(pares_invertidos)
    formateo_impresion(polinomio_invertido, pares_invertidos)

    # * Calculo el polinomio con pares desordenados, muestro su grado y lo grafico
    polinomio_desordenado = calcular_polinomio_interpolador(pares_desordenados)
    formateo_impresion(polinomio_desordenado, pares_desordenados)

    graficar_polinomios_interpoladores(polinomio, pares_ordenados)

if __name__ == "__main__":
    main()
