#Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int.
from random import randint

list = [1,2,3,4,5,6,7]
print(f"Заданный список {list}")
for i in range(0,len(list)//2):
        index = randint(0,len(list)-1)
        list[i], list[index] = list[index], list[i]
print(f"Перемешанный заданный список {list}")