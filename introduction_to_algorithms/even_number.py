"""
Чётные и нечётные числа

Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку,
и на экране появляются три случайных числа. Если все три числа оказываются
одной чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода
В первой строке записаны три случайных целых числа a, b и c.
Числа не превосходят 109 по модулю.

Формат вывода
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.
"""


def is_even_number(number):
    if number % 2 == 0:
        return True
    return False


def check_parity(a: int, b: int, c: int) -> bool:
    return is_even_number(a) == is_even_number(b) == is_even_number(c)


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().split())
print_result(check_parity(a, b, c))
