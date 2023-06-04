import numpy as np
import warnings

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
    # Ordenar primero por X y después por Y
    pares.sort(key=lambda x: (x[0], x[1]))
    return pares


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
        print(y[j]-y[j-1], "/", x[j]-x[j-1])

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
    return polinomio


def main():
    """
    Función principal.
    """
    # Presentación del TP
    print("Métodos Numéricos: TP Polinomio Interpolador")
    print("Integrantes:")
    print("    - Venturini, Tomás")
    print("    - Narvaez, Agustín")
    pares = ordenar_pares(generar_pares_aleatorios())
    print(pares)
    print(calcular_polinomio_interpolador(pares))


if __name__ == "__main__":
    main()
