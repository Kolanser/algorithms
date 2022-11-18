"""
https://contest.yandex.ru/contest/26207/problems/I/
Разные деревья поиска

Ребятам стало интересно, сколько может быть различных деревьев поиска, содержащих в
своих узлах все уникальные числа от 1 до n. Помогите им найти ответ на этот вопрос.

Формат ввода
В единственной строке задано число n. Оно не превосходит 20.

Формат вывода
Нужно вывести число, равное количеству различных деревьев поиска, в узлах которых могут быть размещены
числа от 1 до n включительно.

Пример 1
Ввод	Вывод
2
2
Пример 2
Ввод	Вывод
3
5
Пример 3
Ввод	Вывод
4
14
"""


def get_number_trees(n):
    if n <= 1:
        return 1
    number_trees = 0
    for i in range(n):
        number_trees += get_number_trees(i) * get_number_trees(n - i - 1)
    return number_trees


def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


def get_number_trees_fac(n):
    # (2n)! / n! * (n+1)!
    return int(fac(2 * n) / (fac(n) * fac(n + 1)))


def main():
    n = int(input())
    print(get_number_trees_fac(n))


if __name__ == '__main__':
    main()
