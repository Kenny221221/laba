from random import *
try:
    n = int(input("Введите число: "))
    lst = []


    for i in range(n):
        lst += [randint(-10, 10)]


    indx1 = indx2 = -1

    for i in range(n):
        if lst[i] == 0:
            indx1 = i
            break


    for i in range(indx1 + 1 , n):
        if lst[i] == 0:
            indx2 = i
            break

    ans = 1

    for i in range(indx1+1 , indx2):
        ans *= lst[i]

    lst1, lst2 = [], []

    for i in range(n):
        if i % 2 == 0:
            lst1 += [lst[i]]
        else:
            lst2 += [lst[i]]

    new_lst = lst1 + lst2

    print("Изначальные списки:",lst)
    if indx1 == -1 or indx2 == -1:
        print('Нет 2-х нулей')
    else:
        print("Произведение:", ans)
    print("Список с порядком(нечёт/чёт):",new_lst)
except:
    print("Введено неверное значение")