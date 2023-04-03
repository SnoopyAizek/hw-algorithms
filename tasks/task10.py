'''Условие задачи "Большое число":
Даны числа. Нужно определить, какое самое большое число можно из них составить.
'''

'''Формат ввода:
В строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.
'''

'''Формат вывода:
Нужно вывести самое большое число, которое можно составить из данных чисел.
'''

# Пример ввода -> вывода:
inputs = [
    '15 56 2',    # -> 56215
    '1 783 2',   # -> 78321
    '2 4 5 2 10',  # -> 542210
]

# тут ваше решение:


def comparing_arrays(array1, array2):
    if array1 + array2 > array2 + array1:
        return True
    return False


def big_number(num_list):
    for n in range(1, len(num_list)):
        comparison_num_list = num_list[n]
        x = n
        while x > 0 and comparing_arrays(comparison_num_list, num_list[x - 1]):
            num_list[x] = num_list[x - 1]
            x -= 1
        num_list[x] = comparison_num_list
    return num_list


for input in inputs:
    input_list_list = list(map(list, input.split()))
    input_list = list(map(('').join, big_number(input_list_list)))
    print(('').join(input_list))
