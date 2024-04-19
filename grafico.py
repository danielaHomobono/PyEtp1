import random
import matplotlib.pyplot as plt

def generar_cumples(n):
# Genera cumples para n personas.
    cumples = [random.randint(1, 365) for _ in range(n)]
    return cumples

def hay_coincidencia(cumples):
# Comprueba si hay coincidencias en los cumples.
    return len(cumples) != len(set(cumples))

def simulacion(num_simulaciones, num_personas):
# Simula los cumpleaños para un número de personas dado.
    num_coincidencias = 0
    for _ in range(num_simulaciones):
        cumples = generar_cumples(num_personas)
        if hay_coincidencia(cumples):
            num_coincidencias += 1
    probabilidad = num_coincidencias / num_simulaciones
    return probabilidad

def main():
    num_simulaciones = 1000
    probabilidad_coincidencias = []

    for k in range(1, 51):
        probabilidad = simulacion(num_simulaciones, k)
        probabilidad_coincidencias.append(probabilidad)

    # Resultados
    plt.plot(range(1, 51), probabilidad_coincidencias, color='green')
    plt.xlabel('Numero de personas (k)')
    plt.ylabel('Probabilidad')
    plt.title('Probabilidad de que haya personas con el mismo cumple en un grupo')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()