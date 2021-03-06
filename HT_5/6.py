"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
   https://docs.python.org/3/library/stdtypes.html#range
"""


def range2(min_value, max_value=0, step=1):
    if max_value != 0:
        value = min_value
        if step > 0:
            while value < max_value:
                yield value
                value += step
        else:
            while value > max_value:
                yield value
                value += step
    else:
        value_1 = min_value
        min_value = max_value
        max_value = value_1
        value = min_value
        if step > 0:
            while value < max_value:
                yield value
                value += step


print(range2(0, 20))
print(list(range2(20)))
print(list(range2(0, 20)))
print(list(range2(0, 20, 2)))
print(list(range2(20, 1, -2)))
