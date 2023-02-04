from functools import reduce

def combine_coins(coin, numbers):
    return ', '.join([coin + str(n) for n in numbers])


def double_letter(my_str):
    return "".join(list(map(two_chars, my_str)))


def two_chars(char):
    return char + char


def four_dividers(number):
    return list(filter(is_four_mult, range(1, number + 1)))


def is_four_mult(number):
    return number % 4 == 0


def sum_of_digits(number):
    return reduce(add, list(map(int, str(number))))


def add(a, b):
    return a + b


print(combine_coins('$', range(5)))
print(double_letter("Hello my name is Tal"))
print(four_dividers(9))
print(four_dividers(3))
print(sum_of_digits(104))
