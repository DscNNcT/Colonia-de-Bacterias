# 1. Colonia de Bacterias

# Se desea simular la interacción entre un grupo de tres tipos de bacterias.
# Deberás escribir un programa que, a partir de un estado inicial, pueda predecir las siguientes generaciones.

# El ambiente:
# Las bacterias están en un ambiente toroidal el cual, visualmente, se representará a través de una cuadrícula de dimensiones N x N, de tal forma que la siguiente columna luego de la última, es la primera columna, y la siguiente fila luego de la última fila, es la primera fila.

# Bacterias:
# El tambiente tendrá 3 grupos de bacterias, apodadas según su comportamiento:
# - Bacteria "Piedra": Derrota a las bacterias tipo Tijera. Pierde ante bacterias tipo Papel.
# - Bacteria "Papel": Derrota a las bacterias tipo Piedra. Pierde ante bacterias tipo Tijera.
# - Bacteria "Tijera": Derrota a las bacterias tipo Papel. Pierde ante bacterias tipo Piedra.

# Input matriz inicial:
# Recibirás un numero entero n con el tamaño de la matriz del ambiente toroidal.
# Luego recibirás n veces n numeros separados por espacio.
# Bacterias
# - Piedra: 0
# - Papel: 1
# - Tijera: 2
# Finalmente recibirás un numero entero i con la cantidad de iteraciones o generaciones que debes calcular.

# Sample input 0:
# 5
# 2 2 2 2 2
# 2 1 1 1 2
# 2 1 0 1 2
# 2 1 1 1 2
# 2 2 2 2 2
# 2

#Sample Output 0
# 2 2 2 2 2
# 2 2 2 2 2
# 2 2 2 2 2
# 2 2 2 2 2
# 2 2 2 2 2

#Sample Input 1:
# 6
# 2 2 1 1 0 0
# 0 2 2 1 1 0
# 0 0 2 2 1 1
# 1 0 0 2 2 1
# 1 1 0 0 2 2
# 2 1 1 0 0 2
# 6

# Sample Output 1:
# 2 2 1 1 0 0
# 0 2 2 1 1 0
# 0 0 2 2 1 1
# 1 0 0 2 2 1
# 1 1 0 0 2 2
# 2 1 1 0 0 2

#Sample Input 2:
# 10
# 0 1 1 2 1 2 0 0 1 2
# 0 0 1 0 0 1 0 1 2 0
# 2 0 1 0 1 2 0 1 0 2
# 2 2 1 1 2 2 0 0 1 2
# 1 1 0 2 2 2 0 2 1 2
# 2 0 0 0 2 1 0 0 1 2
# 1 1 2 1 0 2 2 2 1 1
# 0 2 2 2 2 2 0 1 1 2
# 2 0 0 2 1 0 1 0 2 2
# 0 2 0 0 1 1 1 0 0 2
# 1

# Sample Output 2:
# 0 1 1 0 1 0 1 1 2 0
# 0 1 1 1 1 1 1 1 0 0
# 0 1 1 1 2 0 1 1 1 0
# 2 2 1 2 2 0 0 1 2 2
# 2 2 1 0 2 0 0 0 2 2
# 2 1 1 0 2 2 0 1 2 2
# 2 2 0 2 0 0 0 0 2 2
# 1 0 2 2 2 0 0 2 2 2
# 0 0 0 0 2 1 1 1 0 0
# 0 0 0 1 2 1 1 1 0 0

#Sample Input 3:
# 10
# 0 1 1 2 1 2 0 0 1 2
# 0 0 1 0 0 1 0 1 2 0
# 2 0 1 0 1 2 0 1 0 2
# 2 2 1 1 2 2 0 0 1 2
# 1 1 0 2 2 2 0 2 1 2
# 2 0 0 0 2 1 0 0 1 2
# 1 1 2 1 0 2 2 2 1 1
# 0 2 2 2 2 2 0 1 1 2
# 2 0 0 2 1 0 1 0 2 2
# 0 2 0 0 1 1 1 0 0 2
# 10

#Sample Output 3:
# 2 2 2 2 2 2 2 2 2 2
# 0 0 0 2 2 2 2 2 2 2
# 0 0 0 0 2 2 2 2 2 0
# 1 1 1 1 1 1 2 2 2 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 2 2 2 1 1 1 1 1 1
# 2 2 2 2 2 2 1 1 1 2

# ---------------------------------------
import copy

n = int(input()) #Tamaño de la matriz nxn
it = 0 #Número de iteraciones

i = 0
OriginalMat = []
while i < n+1:
    row = []
    for x in input().split():
        row.append(int(x))
    OriginalMat.append(row)
    if i == n-1:
        it = int(input())
        break
    i = i+1

# -- Función para crear la matriz de n+2 x n+2 --
    #Debemos crear una matriz de n+2 x n+2 para darle sentido de "continuidad".
def modMat(m):
    AddTopRow = m[-1] #Creo la primera fila
    AddBottomRow = m[0] #Creo la última fila

    m2 = [] #Esta será la matriz sobre la haremos adicion de columnas.

    m2.append(AddTopRow)

    for i in m:
        m2.append(i)

    m2.append(AddBottomRow)

    matriz = []

    for i in range(0, n+2):
        p = []
        p.append(m2[i][n-1]) #Aquí añadimos la última columna de la mat original como primera columna de la mat a trabajar.
        for j in range (0, n):
            p.append(m2[i][j]) #Aquí añadimos la lista2
        p.append(m2[i][0]) #Aquí añadimos la primera columna de la mat original como última columna de la mat a trabajar.
        matriz.append(p)
    return matriz

# -- Función para volver a la matriz de nxn desde la matriz de n+2 x n+2 --
def backToNxN(m):
    m.pop(0)  # Eliminamos la primera fila
    m.pop() # Eliminamos la última fila

    for i in range(0, n):
        del m[i][0] # Eliminamos la primera columna
        del m[i][-1] #Eliminamos la última columna
    return m

# -- Test de vida --
def lifeTest(m):
    matriz2 = copy.deepcopy(m)
    for i in range(1,n+1):    # i será el numero de fila
        for j in range(1,n+1):    # j será el numero de columna
            elemento = matriz2[i][j]
            v = [
                m[i-1][j-1],
                m[i-1][j],
                m[i-1][j+1],
                m[i][j-1],
                m[i][j+1],
                m[i+1][j-1],
                m[i+1][j],
                m[i+1][j+1],
            ]
            piedras = v.count(0)    # Piedra = 0 -> Gana v tijera // Pierde v Papel
            papeles = v.count(1)    # Papel = 1 -> Gana v piedra // Pierde v tijera
            tijeras = v.count(2)    #Tijera = 2 -> Gana v papel // pierde v piedra
            
            if elemento == 0:
                if papeles >= 3:
                    matriz2[i][j] = 1
                else:
                    elemento = elemento
            elif elemento == 1:
                if tijeras >= 3:
                    matriz2[i][j] = 2
                else:
                    elemento = elemento
            elif elemento == 2:
                if piedras >= 3:
                    matriz2[i][j] = 0
                else:
                    elemento = elemento
            else:
                print("La matriz tiene bacterias no identificadas.")
    return matriz2

m = copy.deepcopy(OriginalMat)

iteracion = 0
while iteracion < it:
    # -- Crea matriz a trabajar --
    matriz = modMat(m)

    # -- Test de vida --
    mat = lifeTest(matriz)

    # -- Volvemos a la matriz de n x n --
    MatNxN = backToNxN(mat)

    m = MatNxN
    iteracion += 1


# -- Definimos el output que nos pidieron --
OutMat = m
out = []

for i in range(0,n):
    o = str(OutMat[i])
    o = o.replace(',', '', n-1)
    o = o.replace('[', '')
    o = o.replace(']', '')
    out.append(o)

for i in range(0,n):
    print(out[i])