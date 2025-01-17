'''Условие задачи "Факторизация":
Основная теорема арифметики говорит: любое число раскладывается на произведение простых множителей единственным образом,
с точностью до их перестановки. Например:

Число 8 можно представить как 2 * 2 * 2.
Число 50 – как 2 * 5 * 5 (или 5 * 5 * 2, или 5 * 2 * 5). Три варианта отличаются лишь порядком следования множителей.
Разложение числа на простые множители называется факторизацией числа.

Напишите программу, которая производит факторизацию переданного числа.
'''

'''Формат ввода:
В единственной строке дано число n, которое нужно факторизовать.
'''

'''Формат вывода:
Выведите в порядке неубывания простые множители, на которые раскладывается число n.
'''

# Пример ввода -> вывода:
inputs = [
    '8',    # -> 2 2 2
    '13',   # -> 13
    '100',  # -> 2 2 5 5
]

# тут ваше решение:


def Factor(n):
    fact_numb = []
    divider = 2
    while divider * divider <= n:
        if n % divider == 0:
            fact_numb.append(divider)
            n //= divider
        else:
            divider += 1
    if n > 1:
        fact_numb.append(n)
    return fact_numb


for input in inputs:
    i = int(input)
    print((' ').join(map(str, Factor(i))))
