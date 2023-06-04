import numpy as np
import warnings
from tabulate import tabulate

# Ignorar advertencias de numpy
warnings.simplefilter(action='ignore', category=FutureWarning)
# Establecer opciones de alineación
options = {"floatfmt": ".0f", "stralign": "center"}

def generarParesAleatorios():
    pares = []
    for i in range(0, 20):
        x = np.random.randint(0, 100)
        y = np.random.randint(0, 100)
        pares.append((x, y))
    return pares

def ordenarPares(pares):
    # Ordenar primero por X y después por Y
    pares.sort(key=lambda x: (x[0], x[1]))
    return pares


def calcular_diferencias_divididas(x, y):
    n = len(x)
    diferencias = []
    diferencias.append(y[0])
    for j in range(1, n):
        if x[j] - x[j-1] != 0:
            diferencias.append((y[j] - y[j-1]) / (x[j] - x[j-1]))
        else:
            diferencias.append(0)
        print(y[j]-y[j-1],"/",x[j]-x[j-1])

        for i in range(j-1, 0, -1):
            if x[j] - x[j-1] != 0:
                diferencias[i] = (diferencias[i] - diferencias[i-1]) / (x[j] - x[j-1])
            else:
                diferencias[i] = 0

    return diferencias

def calcular_coeficientes(x, y):
    diferencias = calcular_diferencias_divididas(x, y)
    coeficientes = [diferencias[0]]
    for i in range(1, len(diferencias)):
        coeficientes.append(diferencias[i])
    return coeficientes

def calcular_polinomio_interpolador(puntos):
    x = [p[0] for p in puntos]
    y = [p[1] for p in puntos]
    coeficientes = calcular_coeficientes(x, y)
    n = len(coeficientes)
    polinomio = f"{coeficientes[0]:.6f}"
    for i in range(1, n):
        polinomio += f" + {coeficientes[i]:.6f}"
        for j in range(i):
            polinomio += f" * (x - {x[j]})"
    return polinomio


def main():
     # * Presentación del TP
    print("Métodos Numéricos: TP Polinomio Interpolador")
    print("Integrantes:")
    print("    - Venturini, Tomás")
    print("    - Narvaez, Agustín")
    pares = ordenarPares(generarParesAleatorios())
    print(pares)
    print(calcular_polinomio_interpolador(pares))

if __name__ == "__main__":
    main()