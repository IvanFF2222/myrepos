print("Принадлежит ли точка ромбу со следующими координатами. ")
x = float(input("Введите число x: "))  # Вводим число x с клавиатуры
y = float(input("Введите число y: "))  # Вводим число y с клавиатуры
if abs(x-y) <= 1 and abs(x+y) <= 1:  # Если условие верно, выводится строка ниже
    print("Точки принадлежат.")
else:  # Если условие не верно, выводится строка ниже
    print("Точки не принадлежат.")