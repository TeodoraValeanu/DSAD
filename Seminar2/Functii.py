import numpy as np

def randomAB(a, b, n): # presupunem ca a, b, n sunt numere intregi
    return a+np.random.rand(n)* (b - a)
    # operatorii + si * sunt supraincarcati pentru
    # adunare scalar la stanga unui vector, respectiv
    # inmultirea unui vector cu un scalar la dreapta

def interschimb(a, b): # presupunem ca a si b sunt variabile de tip numeric
    aux = a
    a = b
    b = aux
    print('interschimb in functie:', a, b)

def interschimbList(l): # presupunem ca l este o lista Python
    # interschimbam primele 2 elemente ale listei
    aux = l[0]
    l[0] = l[1]
    l[1] = aux
