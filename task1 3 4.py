# Нахождение корней квадратного уравнения
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


import math
from typing import Callable
import csv
import json


def deco_takes_values_from_csv(func: Callable):
    def wrapper(*args, **kwargs):
        with open('pull.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                a, b, c = line
                x: int
                my_dict = {}
                my_dict['параметр a'] = a
                my_dict['параметр b'] = b
                my_dict['параметр c'] = c
                print(my_dict)
                func_res = func(int(a), int(b), int(c))

                if (func_res is not None):
                    if (len(func_res) == 1):
                        my_dict[f'результат x'] = func_res
                    elif len(func_res) == 2:
                        x1, x2 = func_res
                        my_dict[f'результат x1'] = x1
                        my_dict[f'результат x2'] = x2
                else:
                    my_dict[f'результат '] = 'корней нет'
                print(my_dict)
                with open('save_results.json', 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, indent=2, ensure_ascii=False, separators=(',', ':'))
        return
    return wrapper


@deco_takes_values_from_csv
def square_root(a: int, b: int, c: int):
    print('_________________________________')
    print("ax^2 + bx + c = 0:")
    print(f'a = {a}, b = {b}, c = {c}')

    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f    x2 = %.2f" % (x1, x2))
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
        return x
    else:
        print("Корней нет")
        return None


square_root(2, 7, 5)
