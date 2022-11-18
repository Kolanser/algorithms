"""
https://contest.yandex.ru/contest/24734/problems/H/
Большое число

Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из
них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из
которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.

Пример 1
Ввод
3
15 56 2
Вывод
56215
Пример 2
Ввод
3
1 783 2
Вывод
78321
Пример 3
Ввод
5
2 4 5 2 10
Вывод
542210
"""


def is_first_number_bigger(number_1, number_2):
    return int(number_1 + number_2) > int(number_2 + number_1)


def get_big_number(n, arr, more):
    for i in range(1, n):
        item_to_insert = arr[i]
        j = i
        while j > 0 and more(item_to_insert, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item_to_insert
    return arr


def main():
    n = int(input())
    arr = input().split()
    big_number = get_big_number(n, arr, is_first_number_bigger)
    print(''.join(big_number))


if __name__ == '__main__':
    main()
