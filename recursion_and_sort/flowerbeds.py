""""
https://contest.yandex.ru/contest/24734/problems/N/
Клумбы

Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам.
На схеме земельного участка клумбы обозначаются просто горизонтальными
отрезками, лежащими на одной прямой. Для ландшафтных работ было нанято
n садовников. Каждый из них обрабатывал какой-то отрезок на схеме.
Процесс был организован не очень хорошо, иногда один и тот же отрезок
или его часть могли быть обработаны сразу несколькими садовниками.
Таким образом, отрезки, обрабатываемые двумя разными садовниками,
сливаются в один. Непрерывный обработанный отрезок затем станет клумбой.
Нужно определить границы будущих клумб.
Формат ввода
В первой строке задано количество садовников n.
Число садовников не превосходит 100000.
В следующих n строках через пробел записаны координаты клумб в формате:
start end, где start —– координата начала, end —– координата конца.
Оба числа целые, неотрицательные и не превосходят 107.
start строго меньше, чем end.

Формат вывода
Нужно вывести координаты каждой из получившихся клумб в отдельных строках.
Данные должны выводится в отсортированном порядке —– сначала клумбы с
меньшими координатами, затем —– с бОльшими.
Пример 1
Ввод
4
7 8
7 8
2 3
6 10
Вывод
2 3
6 10
Пример 2
Ввод
4
2 3
5 6
3 4
3 4
Вывод
2 4
5 6
Пример 3
Ввод
6
1 3
3 5
4 6
5 6
2 4
7 10
Вывод
1 6
7 10
"""

def read():
    count_gardener = int(input())
    segments = [list(map(int, input().split())) for _ in range(count_gardener)]
    return segments


def get_new_segments(segments):
    if len(segments) == 1:
        return segments
    segments.sort()
    new_segments = []
    new_segments.append(segments[0])
    for i in range(1, len(segments)):
        start_previous = new_segments[-1][0]
        end_previous = new_segments[-1][1]
        start_segment = segments[i][0]
        end_segment = segments[i][1]
        if end_previous < start_segment:
            new_segments.append([start_segment, end_segment])
        elif end_previous == start_segment or end_previous < end_segment:
            new_segments[-1] = [start_previous, end_segment]
        else:
            new_segments[-1] = [start_previous, end_previous]
    return new_segments


def main():
    segments = read()
    new_segments = get_new_segments(segments)
    for a in new_segments:
        print(*a)


if __name__ == '__main__':
    main()
