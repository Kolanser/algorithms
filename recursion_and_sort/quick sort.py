# 72152733
from dataclasses import dataclass


@dataclass
class Competitor:
    name: str
    number_tasks: int
    fine: int

    def __str__(self):
        return self.name

    def __add__(self, other):
        return self.number_tasks + other.number_tasks

    def __lt__(self, other):
        return (
            self.number_tasks > other.number_tasks
            or (
                self.number_tasks == other.number_tasks
                and self.fine < other.fine
            )
            or (
                self.number_tasks == other.number_tasks
                and self.fine == other.fine
                and self.name < other.name
            )
        )


def read():
    count = int(input())
    competitors = [None] * count
    for i in range(count):
        params = input().split()
        competitor = Competitor(params[0], int(params[1]), int(params[2]))
        competitors[i] = competitor
    return competitors


def split_competitors(competitors, pivot, left_cursor, right_cursor):
    while left_cursor <= right_cursor:
        if competitors[left_cursor] < pivot:
            left_cursor += 1
        else:
            while left_cursor <= right_cursor:
                if (competitors[right_cursor] < pivot
                        or competitors[right_cursor] == pivot):
                    competitors[left_cursor], competitors[right_cursor] = (
                        competitors[right_cursor], competitors[left_cursor]
                    )
                    right_cursor -= 1
                    left_cursor += 1
                    break
                else:
                    right_cursor -= 1
    return left_cursor, right_cursor


def quick_sort(competitors, left, right):
    if right - left <= 1:
        return competitors[left:right]
    pivot = competitors[(right + left) // 2]
    left_cursor, right_cursor = split_competitors(
        competitors, pivot, left, right - 1
        )
    if left_cursor == right and right_cursor == left:
        return competitors[left:right]
    return (
        quick_sort(competitors, left, left_cursor)
        + quick_sort(competitors, left_cursor, right)
        )


def main():
    competitors = read()
    quick_sort(competitors, 0, len(competitors))
    print(*competitors, sep='\n')


if __name__ == '__main__':
    main()
