import sys

def sumar(n1: int, n2: int):
    return n1+n2

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
except IndexError:
    print('Se necesitan dos números como argumentos, saliendo...')
    exit(1)

print(sumar(n1, n2))
