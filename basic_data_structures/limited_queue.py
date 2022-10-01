"""
Ограниченная очередь
https://contest.yandex.ru/contest/23758/problems/I/
Астрологи объявили день очередей ограниченного размера.
Тимофею нужно написать класс MyQueueSized, который принимает
параметр max_size, означающий максимально допустимое количество
элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать
работу такой очереди. Функции, которые надо поддержать, описаны
в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error».
При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.

Пример 1
Ввод	
8
2
peek
push 5
push 2
peek
size
size
push 1
size
Вывод
None
5
2
2
error
2
Пример 2
Ввод	
10
1
push 1
size
push 3
size
push 1
pop
push 1
pop
push 3
push 3
Вывод
1
error
1
error
1
1
error
"""


class QueueEmpty(Exception):
    """Очередь пуста."""

    pass


class QueueOverflow(Exception):
    """Очередь переполнена."""

    pass


class MyQueueSize:
    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size_queue = 0

    def push(self, x):
        if self.__size_queue == self.__max_size:
            raise QueueOverflow
        self.__queue[self.__tail] = x
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size_queue += 1

    def pop(self):
        if not self.size():
            raise QueueEmpty
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size_queue -= 1
        return x

    def peek(self):
        if not self.size():
            raise QueueEmpty
        return self.__queue[self.__head]

    def size(self):
        return self.__size_queue


def read_input():
    size_commands = int(input())
    max_size_queue = int(input())
    commands = [input() for _ in range(size_commands)]
    return max_size_queue, commands


def print_command(queue, commands):
    for command in commands:
        try:
            command, *args = command.split()
            result = getattr(queue, command)(*args)
            if result is not None:
                print(result)
        except QueueEmpty:
            print('None')
        except QueueOverflow:
            print('error')


def main():
    max_size_queue, commands = read_input()
    my_queue = MyQueueSize(max_size_queue)
    print_command(my_queue, commands)


if __name__ == '__main__':
    main()

