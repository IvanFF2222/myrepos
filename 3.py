from math import *
x = float(input("Введите x:"))  # Вводим число x с клавиатуры
y = float(input("Введите y:"))  # Вводим число y с клавиатуры
z = float(input("Введите z:"))  # Вводим число z с клавиатуры
v = ((1+(sin(x+y))**2)/(abs(x-(2*y)/(1+x**2*y**2))))*x**abs(y)+(cos(atan(1/z)))**2  # Алгоритм решения уравнения
print("Результат: ", "\n", "u =", v)  # Вывод результата