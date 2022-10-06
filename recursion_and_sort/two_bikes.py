"""
https://contest.yandex.ru/contest/24734/problems/L/
Два велосипеда

Вася решил накопить денег на два одинаковых велосипеда — себе и сестре.
У Васи есть копилка, в которую каждый день он может добавлять деньги
(если, конечно, у него есть такая финансовая возможность).
В процессе накопления Вася не вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у
Васи в копилке было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить
первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения
за Васиными накоплениями. 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел.
Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.

В третьей строке записано целое положительное число s — стоимость
велосипеда. Это число не превосходит 106.

Формат вывода
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.

Пример 1
Ввод	
6
1 2 4 4 6 8
3
Вывод
3 5
Пример 2
Ввод
6
1 2 4 4 4 4
3
Вывод
3 -1
Пример 3
Ввод
6
1 2 4 4 4 4
10
Вывод
-1 -1
"""


def read():
    amount_days = int(input())
    accumulations = list(map(int, input().split()))
    price = int(input())
    return amount_days, accumulations, price


def binary_search(arr, x, left, right):
    mid = (left + right) // 2
    if right == left:
        if x <= arr[mid]:
            return mid + 1
        return -1
    if x <= arr[mid]:
        return binary_search(arr, x, left, mid)
    return binary_search(arr, x, mid + 1, right)


def main():
    amount_days, accumulations, price_one_bike = read()
    days_one_bike = binary_search(
        accumulations,
        price_one_bike,
        left=0,
        right=amount_days - 1
    )
    price_two_bike = 2 * price_one_bike
    days_two_bikes = binary_search(
        accumulations,
        price_two_bike,
        left=days_one_bike - 1,
        right=amount_days - 1
    )
    print(days_one_bike, days_two_bikes)


if __name__ == '__main__':
    main()
