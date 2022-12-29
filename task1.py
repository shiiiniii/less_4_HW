# 1. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 
# 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

k = int(input('Введите натуральную степень k: '))

def write_file(new_file):
    with open('task_1.txt', 'w') as data:
        data.write(new_file)

def rnd():
    return random.randint(1, 100)

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
                if my_list[i+1] != 0:
                    a += ' + '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                a += f'{my_list[i]}x'
                if my_list[i+1] != 0:
                    a += ' + '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                a += f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                a += ' = 0'
    return a

koef = create_mn(k)
write_file(create_str(koef))
