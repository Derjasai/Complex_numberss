import math


def suma_compleja(c1, c2):
    a = c1[0] + c2[0]
    b = c1[1] + c2[1]
    result = (a, b)
    return result


def multiplicacion_compleja(c1, c2):
    a = (c1[0]*c2[0]) - (c1[1]*c2[1])
    b = (c1[1]*c2[0]) + (c1[0]*c2[1])
    result = (a, b)
    return result


def sustracion_compleja(c1, c2):
    a = c1[0] - c2[0]
    b = c1[1] - c2[1]
    result = (a, b)
    return result


def division_compleja(c1, c2):
    a = ((c1[0]*c2[0]) + (c1[1]*c2[1]))/(c2[0]**2 + c2[1]**2)
    b = ((c2[0]*c1[1]) - (c1[0]*c2[1]))/(c2[0]**2 + c2[1]**2)
    result = (a,b)
    return result


def modulo(c):
    result = math.sqrt(c[0]**2 + c[1]**2)
    return result


def conjugado(c):
    result = (c[0], c[1]*-1)
    return result


def polar_a_carte(polar):
    x = polar[0]*math.cos(polar[1])
    y = polar[0]*math.sin(polar[1])
    result = (round(x, 4), round(y, 4))
    return result


def carte_a_polar(coords):
    p = math.sqrt(coords[0]**2+coords[1]**2)
    ang = fase_compleja(coords)
    result = (p, ang)
    return result


def fase_compleja(c):
    fase = math.atan(c[1]/c[0])
    if c[0] < 0 and c[1] < 0:
        result = 180 + math.degrees(fase)
    elif c[0] < 0:
        result = 180 + math.degrees(fase)
    elif c[1] < 0:
        result = 360 + math.degrees(fase)
    else:
        result = math.degrees(fase)
    return result


def suma_vectores_complejos(v1: list, v2: list):
    result = list()
    for i in range(len(v1)):
        result.append(complex(v1[i]) + complex(v2[i]))
    return result


def inverso_vector(v: list):
    result = list()
    for i in range(len(v)):
        viner = complex(v[i]) * -1
        result.append(viner)
    return result


def vectorxescalar(v: list, a:int):
    result = list()
    for i in range(len(v)):
        result.append(complex(v[i]) * a)
    return result


def suma_matrices_complex(matriz1: list, matriz2: list):
    result = [[complex(matriz1[i][j]) + complex(matriz2[i][j]) for j in range(len(matriz1[i]))]
              for i in range(len(matriz1))]

    return result


def inverso_matriz(matriz: list):
    result = list()
    for i in range(len(matriz)):
        result.append(inverso_vector(matriz[i]))
    return result


def matrizxescalar(matriz: list, a: int):
    result = list()
    for i in range(len(matriz)):
        result.append(vectorxescalar(matriz[i], a))
    return result


def transponer(a: list):
    result = list()
    for i in range(len(a[0])):
        result.append([])
        for j in range(len(a)):
            result[i].append("None")

    for i in range(len(a)):
        for j in range(len(a[i])):
            result[j][i] = a[i][j]
    return result


def conjugar(a: list):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = a[i][j].conjugate()
    return a


def matriz_adjunta(matriz: list):
    matriz = transponer(matriz)
    return conjugar(matriz)


def matrizxmatriz(matriz1: list, matriz2: list):
    result = list()
    for i in range(len(matriz1)):
        fila = list()
        for j in range(len(matriz2[0])):
            suma = 0
            for k in range(len(matriz2)):
                producto = complex(matriz1[i][k]) * complex(matriz2[k][j])
                suma += producto
            fila.append(suma)
        result.append(fila)
    return result


def accion_matriz_vector(matriz: list, vector: list):
    result = list()


def producto_interno_vector(v1: list, v2: list):
    result = list()
    for i in range(len(v1)):
        result.append(list())
        v1[i] = complex(v1[i]).conjugate()
        result[i] = (complex(v1[i]) * complex(v2[i]))
    while len(result) > 1:
        result[0] = complex(result[0]) + complex(result[-1])
        result.pop()
    return result[0]


def norma(vector: list):
    result = 0
    for i in vector:
        result += i[0]**2 + i[1]**2
    return math.sqrt(result)


def distancia_vecotres(vector1: list, vector2: list):
    result = 0
    for i in range(len(vector1)):
        result += (vector1[i][0] - vector2[i][0])**2 + (vector1[i][1] - vector2[i][1])**2
    return math.sqrt(result)


def ishermitiana(matriz: list):
    return matriz == matriz_adjunta(matriz)


def producto_tensor(m1, m2):
    lista=[]
    filas = len(m1)*len(m2)
    columnas = len(m1[0])*len(m2[0])
    for x in range(filas):
        lista2=[]
        lista.append(lista2)
        for y in range(columnas):
            lista2.append([])
    for i in range(filas):
        for j in range(columnas):
            a = i//len(m2)
            b = j//len(m2[0])
            res = m1[a][b] * m2
            a2 = i % len(m2)
            b2 = j % len(m2[0])
            lista[i][j] = res[a2][b2]
    return lista


print(norma([(1, -3), (0, 2)]))
