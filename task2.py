# 2. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0, 101)

def create_mn(k):
    my_list = [rnd() for i in range(k+1)]
    return my_list

def create_str(new_str):
    my_list = new_str[::-1]
    a = ''
    if len(my_list) < 1:
        a = 'x = 0'
    else:
        for i in range(len(my_list)):
            if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
                a += f'{my_list[i]}x^{len(my_list)-i-1}'
                if my_list[i+1] != 0 or my_list[i+2] != 0:
                    a += ' + '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                a += f'{my_list[i]}x'
                if my_list[i+1] != 0 or my_list[i+2] != 0:
                    a += ' + '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                a += f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                a += ' = 0'
    return a

def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  
    j = l-1  
    while j >= 0:
        if sq_mn(st[j]) != -1 and sq_mn(st[j]) == i:
            lst.append(k_mn(st[j]))
            j -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
    return lst

k1 = int(input("Введите натуральную степень для первого многочлена: k1 = "))
k2 = int(input("Введите натуральную степень для второго многочлена: k2 = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("task2_1.txt", create_str(koef1))
write_file("task2_2.txt", create_str(koef2))

with open('task2_1.txt', 'r') as data:
    st1 = data.readlines()
with open('task2_2.txt', 'r') as data:
    st2 = data.readlines()

my_list1 = calc_mn(st1)
my_list2 = calc_mn(st2)
my_new_list = len(my_list1)
if len(my_list1) > len(my_list2):
    my_new_list = len(my_list2)
my_list_new = [my_list1[i] + my_list2[i] for i in range(my_new_list)]
if len(my_list1) > len(my_list2):
    b = len(my_list1)
    for i in range(my_new_list, b):
        my_list_new.append(my_list1[i])
else:
    b = len(my_list2)
    for i in range(my_new_list, b):
        my_list_new.append(my_list2[i])
write_file("sum_result.txt", create_str(my_list_new))
with open('sum_result.txt', 'r') as data:
    st3 = data.readlines()
print(f"Сумма многочленов: {st3}")
