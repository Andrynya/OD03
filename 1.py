#Сложность алгоритма O(n^2)

mas = [1, 2, 4, 3, 8, 2, 9]
n = 6

for run in range(n - 1):
    for i in range(n - 1):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]

print(mas)