# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
stroka = input("Введите вещественное число: ")
chislo = float(stroka)
Sum = 0
while chislo != int(chislo):
    chislo = round(chislo*10,len(stroka))
print(chislo)
while chislo != 0:
    Sum += chislo%10
    chislo //= 10
print(Sum)