"""
Ближайший ноль
https://contest.yandex.ru/contest/23390/problems/
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить,
имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.
Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка.
Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому
их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке
записаны n целых неотрицательных чисел — номера домов и обозначения
пустых участков на карте (нули). Гарантируется, что в последовательности
есть хотя бы один ноль. Номера домов (положительные числа) уникальны и
не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля.
Числа выводите в одну строку, разделяя их пробелами.

Пример 1
Ввод	
5
0 1 4 9 0
Вывод
0 1 2 1 0
Пример 2
Ввод	
6
0 7 9 4 8 20
Вывод
0 1 2 3 4 5
"""

from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    number_houses = int(input())
    houses = list(map(int, input().split()))
    return number_houses, houses


def get_distance_to_nearest_null(
        number_houses: int, houses: List[int]) -> List[int]:
    distance_null = [0 for _ in range(number_houses)]
    # максимальная дистанция на 1 меньше длины списка
    index_null_pre = number_houses - 1
    for i in range(number_houses):
        if houses[i] == 0:
            index_null_pre = i
        else:
            distance_null[i] = abs(i - index_null_pre)

    for i in range(number_houses - 1, -1, -1):
        if houses[i] == 0:
            index_null_pre = i
        else:
            if abs(i - index_null_pre) < distance_null[i]:
                distance_null[i] = abs(i - index_null_pre)
    return distance_null


def main():
    number_houses, houses = read_input()
    print(*get_distance_to_nearest_null(number_houses, houses))


if __name__ == '__main__':
    main()
