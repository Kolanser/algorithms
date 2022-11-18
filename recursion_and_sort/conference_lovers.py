"""
https://contest.yandex.ru/contest/24734/problems/I/
Любители конференций

На IT-конференции присутствовали студенты из разных вузов со всей страны. Для каждого студента известен ID университета, в котором он учится.

Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло больше всего учащихся.

Формат ввода
В первой строке дано количество студентов в списке —– n (1 ≤ n ≤ 15 000).

Во второй строке через пробел записаны n целых чисел —– ID вуза каждого студента. Каждое из чисел находится в диапазоне от 0 до 10 000.

В третьей строке записано одно число k.

Формат вывода
Выведите через пробел k ID вузов с максимальным числом участников. Они должны быть отсортированы по убыванию популярности (по количеству гостей от конкретного вуза). Если более одного вуза имеет одно и то же количество учащихся, то выводить их ID нужно в порядке возрастания.

Пример 1
Ввод	Вывод
7
1 2 3 1 2 3 4
3
1 2 3
Пример 2
Ввод	Вывод
6
1 1 1 2 2 3
1
1
"""


def read():
    _ = int(input())
    id_students = list(map(int, input().split()))
    numbers_id = int(input())
    return id_students, numbers_id


def get_universities(id_students, numbers_id):
    id_counts = {}
    for id_student in id_students:
        if id_student not in id_counts:
            id_counts[id_student] = 0
        id_counts[id_student] += 1
    id_counts = dict(
        sorted(id_counts.items(), key=lambda item: item[0], reverse=True)
    )
    return list(id_counts.keys())[:numbers_id]


def main():
    id_students, numbers_id = read()
    id_universities = get_universities(id_students, numbers_id)
    print(*id_universities)


if __name__ == '__main__':
    main()