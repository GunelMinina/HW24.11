# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = input('Введите число: ')
S = 0
for i in range (0, len(n)):
    if n[i] != ',':
        S += int(n[i])
print(S)

