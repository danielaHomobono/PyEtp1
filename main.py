import random
#tomamos a k(personas en un grupo) y devuelve números aleatorios entre 1 y 365.
def cumples(k):
    return [random.randint(1, 365) for _ in range(k)]

# devuelve true si hay repetido.
def hay_coincidencia(cumples):
    return len(cumples) != len(set(cumples))

#Toma a k(num de personas) y N(las veces que se repetirá). Usamos coincidencias para
#contar.Si hay coincidencia, se incrementa en 1 coincidencias y se la divide por N.
def probabilidad_coincidencia(k, N):
    coincidencias = 0
    for _ in range(N):
        if hay_coincidencia(cumples(k)):
            coincidencias += 1
    return coincidencias / N


# calculamos la probabilidad para k entre 1 y 50
probabilidades = [probabilidad_coincidencia(k, 1000) for k in range(1, 51)]

# enumerate(), toma la lista probabilidades y empieza a contar desde 0.Entonces, como queremos que empiece a contar en 1.
for k, prob in enumerate(probabilidades, 1):
    print(f"Para un grupo de {k} personas, la probabilidad estimada de que al menos dos personas cumplan años el mismo día es {prob}")










