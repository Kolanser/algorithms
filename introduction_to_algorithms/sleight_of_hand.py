"""
Ловкость рук
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек. На клавише
написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t. Гоша и Тимофей могут нажать в один момент
времени на k клавиш каждый. Если в момент времени t нажаты все нужные
клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей,
если будут нажимать на клавиши вдвоём.


Формат ввода
В первой строке дано целое число k (1 ≤ k ≤ 5).

В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой строке.
Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной
строки идут подряд и не разделены пробелами.

Формат вывода
Выведите единственное число –— максимальное количество баллов,
которое смогут набрать Гоша и Тимофей.

Пример 1
Ввод	
3
1231
2..2
2..2
2..2
Вывод
2
Пример 2
Ввод	
4
1111
9999
1111
9911
Вывод
1
Пример 3
Ввод	
4
1111
1111
1111
1111
Вывод
0
"""

from typing import Tuple


def read_input() -> Tuple[int, str]:
    number_of_clicks = int(input())
    size_matrix = 4
    matrix = [input() for _ in range(size_matrix)]
    return number_of_clicks, ''.join(matrix)


def get_max_ball(number_of_clicks: int, matrix: str) -> int:
    count_symbols = {}
    symbol_counter = 1
    start_counter = 0
    for symbol in matrix:
        if symbol != '.':
            if not count_symbols.get(symbol):
                count_symbols[symbol] = start_counter
            count_symbols[symbol] += symbol_counter
    max_ball = 0
    numbers_players = 2
    for count_symbol in count_symbols.values():
        if count_symbol <= number_of_clicks * numbers_players:
            max_ball = max_ball + 1
    return max_ball


def main():
    number_of_clicks, matrix = read_input()
    print(get_max_ball(number_of_clicks, matrix))


if __name__ == '__main__':
    main()
