print("Введите кол-во чисел, отличных от нуля:")
imin = 1000
i = 1
N = 0
B = [0] * 1000
while i != 0:
    i = int(input())
    N = N + 1
    B[N] = i
    if i != 0:
        if i < imin:
            imin = i
    if i == 0:
        break
print("Минимальное значение:", imin)
N = 0
for i in range (0,999):
    if B[i] == imin:
        N = N + 1
print("Кол-во минимальных значений:", N)