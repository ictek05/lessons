#task1.1  - Квадратную матрицу А произвольного размера умножте на квадратную матрицу B
#эквивалентного размера.

import numpy as np     #юзаем математику из модуля numpy

matrix1 = np.arange(9).reshape(3,3)   #создание матрица 3х3 - рендж 0-9
matrix2 = np.arange(9).reshape(3,3)

matrix_1x2 = np.dot(matrix1, matrix2)  #умножение 1 на 2

print("Матрица 1 -")
print(matrix1)
print("Матрица 2 -")
print(matrix2)


print("Умножение матриц = 1х2")
print(matrix_1x2)

#task1.2
#Возведите в степерь каждое значение квадратной матрицы А с произвольными значениями.

from numpy import linalg as la

matrix1 = np.arange(100).reshape(10,10)   #создаем матрицу 10 х 10 - рендж 0-100
print("Матрица 1 -")
print(matrix1)
stepen = int(input("В какую степень возводим? = "))
matrix1 = la.matrix_power(matrix1, stepen)     #liang.matrix_power позволяет возводить матрицу в степень
print("Матрица 1 возведенная в степень {}:".format(stepen))
print(matrix1)

#task1.3
#Переведите текст этой задачи в 2-хмерный список,
# где строки это 1 уровень списка,
# а слова - второй

stroki = 'Переведите текст этой задачи в 2-хмерный список,\n где строки это 1 уровень списка,\n а слова - второй'
stroki = stroki.split('\n')   #делим по \n
for i in range(len(stroki)):   # выводим построчно
    print(stroki[i])

x = len(stroki)
print("Первый уровень - колличество строк = {}".format(x))
print("Второй уровень - ")

z = []
for i in range(len(stroki)):
    z = stroki[i].split(' ')
    print("Список строки - {}".format(i))
    print(z)

