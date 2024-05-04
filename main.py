import random
from math import tan, sin, sqrt
import decimal

# Размеры матриц
glen = 4
mlen = 5
nlen = 6

# Матрицы
g = [[0] * glen for _ in range(glen)]
m = [[0] * mlen for _ in range(mlen)]
n = [[0] * nlen for _ in range(nlen)]


# Ввод матрицы
def input_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        s = [int(k) for k in (input().split())]
        for j in range(n):
            matrix[i][j] = s[j]


# Инициализация матрицы случайными числами
def random_init(matrix, left, right):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(left, right)


# Вывод матрицы
def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        print(matrix[i])


# Вычисление значения функции
def Y(x, a, b, d, c, t, k):
    ab = abs(a**2 - b**2)
    dc = decimal.Decimal(str(sqrt(abs(tan(d)**2 - sin(c)**2))))
    tk = sqrt(abs(t**2 - k**2))

    return sqrt(ab * x + dc) / tk


print("Выберите_способ задания_матриц:")
print("1 - ручной ввод")
print("2 - автоматический ввод")

try:
    while True:
        ch = input()
        match ch:
            case '1':
                print("Введите матрицу g")
                input_matrix(g)
                print("Введите матрицу m")
                input_matrix(m)
                print("Введите матрицу n")
                input_matrix(n)
            case '2':
                random_init(g, -1000, 1000)
                random_init(m, -1000, 1000)
                random_init(n, -1000, 1000)
            case _:
                print("Неверный ввод, повторите попытку")

        if ch == '1' or ch == '2':
            break

    print("Матрица g:")
    print_matrix(g)
    print("Матрица m:")
    print_matrix(m)
    print("Матрица n:")
    print_matrix(n)

    a = 0
    b = 0

    # Вычисление a и b
    for i in range(glen):
        for j in range(i):
            if g[i][j] >= 0:
                a += g[i][j]
                b += 1

    print("a = ", a, ", b = ", b)

    d = 0
    c = 0

    # Вычисление d и c
    for i in range(mlen):
        for j in range(i):
            if m[i][j] >= 0:
                d += m[i][j]
                c += 1

    print("d = ", d, ", c = ", c)

    t = 0
    k = 0

    # Вычисление t и k
    for i in range(nlen):
        for j in range(i):
            if n[i][j] >= 0:
                t += n[i][j]
                k += 1

    print("t = ", t, ", k = ", k)

    print("\nВведите xs, st и h:")

    xs = decimal.Decimal(input())
    xt = decimal.Decimal(input())
    h = decimal.Decimal(input())

    # Таблица значений
    table = {}

    # Вычисление таблицы
    x = xs

    while (x <= xt):
        table[x] = Y(x, a, b, d, c, t, k)
        x += h

    for key, value in table.items():
        print(f"{key}: {value}")

except ZeroDivisionError:
    print("Деление на ноль!")
except IndexError:
    print("Выход за пределы массива")

# 1 2 3 4
# -1 -1 -1 -1
# -1 -1 -1 -1
# -1 -1 -1 -1
#
# 1 2 3 4 5
# -1 -1 -1 -1 -1
# -1 -1 -1 -1 -1
# -1 -1 -1 -1 -1
# -1 -1 -1 -1 -1
#
# 1 2 3 4 5 6
# 1 0 0 0 0 0
# 1 1 0 0 0 0
# 1 1 1 0 0 0
# 1 1 1 1 0 0
# 1 1 1 1 10 0
