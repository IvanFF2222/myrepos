from math import *
x = float(input("Введите x:"))  # Вводим число x с клавиатуры
y = float(input("Введите y:"))  # Вводим число y с клавиатуры
z = float(input("Введите z:"))  # Вводим число z с клавиатуры
t = (2*cos(x-(pi/6)))/(0.5+(sin(y))**2)*(1+((z**2)/(3-z**2/5)))  # Алгоритм решения уравнения
print("Результат: ", "\n", "t =", t)  # Вывод результата