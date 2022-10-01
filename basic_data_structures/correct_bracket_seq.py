"""
Скобочная последовательность

Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.

Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:
пустая строка —– правильная скобочная последовательность;
правильная скобочная последовательность, взятая в скобки одного типа, –— правильная скобочная последовательность;
правильная скобочная последовательность с приписанной слева или справа правильной скобочной последовательностью —– тоже правильная.
На вход подаётся последовательность из скобок трёх видов: [], (), {}.

Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную последовательность и возвращает True,
если последовательность правильная, а иначе False.

Формат ввода
На вход подаётся одна строка, содержащая скобочную последовательность. Скобки записаны подряд, без пробелов.

Формат вывода
Выведите «True» или «False».

Пример 1
Ввод
{[()]}
Вывод
True
Пример 2
Ввод	
()
Вывод
True
"""


class Stack:

    def __init__(self):
        self.__items = []
        self.__size = 0

    def push(self, item):
        self.__items.append(item)
        self.__size += 1

    def pop(self):
        self.__items.pop()
        self.__size -= 1

    def peek(self):
        return self.__items[-1]

    def is_empty(self):
        return self.__size == 0


BRACKETS = {
    '(': ')',
    '{': '}',
    '[': ']',
}


def is_correct_bracket_seq(bracket_seq):
    stack = Stack()
    for bracket in bracket_seq:
        if bracket in BRACKETS:
            stack.push(bracket)
        elif not stack.is_empty() and BRACKETS[stack.peek()] == bracket:
            stack.pop()
        else:
            return False
    if stack.is_empty():
        return True
    return False


def main():
    bracket_seq = input()
    print(is_correct_bracket_seq(bracket_seq))


if __name__ == '__main__':
    main()
