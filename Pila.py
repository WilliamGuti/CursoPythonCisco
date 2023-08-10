# el metodo pila explica la manera en como se apilan los elementos de manera de torre, lo cual hace que los
# ultimos elementos en entrar, sean los primeros en salir, por ejemplo
pila = []

def push(val):
    pila.append(val)


def pop():
    val = pila[-1]
    del pila[-1]
    return val


push(3)
push(2)
push(1)
print(pila)
print(pop())
print(pop())
print(pop())