"""
https://contest.yandex.ru/contest/23389/problems/C/
Соседи
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дана матрица. Нужно написать функцию, которая для элемента возвращает
всех его соседей. Соседним считается элемент, находящийся от текущего
на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.

Формат ввода
В первой строке задано n — количество строк матрицы.
Во второй — количество столбцов m. Числа m и n не превосходят 1000.
В следующих n строках задана матрица. Элементы матрицы — целые числа,
по модулю не превосходящие 1000. В последних двух строках записаны
координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.

Пример 1
Ввод	
4
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0
Вывод
7 7
Пример 2
Ввод
4
3
1 2 3
0 2 6
7 4 1
2 7 0
0
0
Вывод
0 2
"""


from typing import List, Tuple


def is_matrix(n: int, m: int, row: int, col: int):
    return row < n and col < m and row >= 0 and col >= 0


def get_neighbours(n: int, m: int, matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbours = []
    if is_matrix(n, m, row, col-1):
        neighbours.append(matrix[row][col-1])
    if is_matrix(n, m, row-1, col):
        neighbours.append(matrix[row-1][col])
    if is_matrix(n, m, row, col+1):
        neighbours.append(matrix[row][col+1])
    if is_matrix(n, m, row+1, col):
        neighbours.append(matrix[row+1][col])
    return sorted(neighbours)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    row = int(input())
    col = int(input())
    return n, m, matrix, row, col


n, m, matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(n, m, matrix, row, col))))
