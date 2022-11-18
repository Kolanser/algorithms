"""
https://contest.yandex.ru/contest/24734/problems/E/
Покупка домов

Тимофей решил купить несколько домов на знаменитом среди разработчиков Алгосском архипелаге.
Он нашёл n объявлений о продаже, где указана стоимость каждого дома в алгосских франках.
А у Тимофея есть k франков. Помогите ему определить, какое наибольшее количество домов на Алгосах он сможет приобрести за эти деньги.

Формат ввода
В первой строке через пробел записаны натуральные числа n и k.

n — количество домов, которые рассматривает Тимофей, оно не превосходит 100000;

k — общий бюджет, не превосходит 100000;

В следующей строке через пробел записано n стоимостей домов. Каждое из чисел не превосходит 100000. Все стоимости — натуральные числа.

Формат вывода
Выведите одно число —– наибольшее количество домов, которое может купить Тимофей.

Пример 1
Ввод	Вывод
3 300
999 999 999
0
Пример 2
Ввод	Вывод
3 1000
350 999 200
2
"""


def read():
    count_ad_and_franc = input().split()
    francs = int(count_ad_and_franc[1])
    ads = list(map(int, input().split()))
    return francs, ads


def get_count_houses(francs, ads):
    ads.sort()
    count_houses = 0
    free_franc = francs
    for ad in ads:
        if ad <= francs:
            free_franc -= ad
            if free_franc < 0:
                return count_houses
            elif free_franc == 0:
                return count_houses + 1
            count_houses += 1
    return count_houses


def main():
    francs, ads = read()
    count_houses = get_count_houses(francs, ads)
    print(count_houses)


if __name__ == '__main__':
    main()
