"""
https://contest.yandex.ru/contest/24734/problems/C/
Подпоследовательность

Гоша любит играть в игру «Подпоследовательность»: даны 2 строки, и нужно понять, является ли первая из них подпоследовательностью второй. Когда строки достаточно длинные, очень трудно получить ответ на этот вопрос, просто посмотрев на них. Помогите Гоше написать функцию, которая решает эту задачу.

Формат ввода
В первой строке записана строка s.

Во второй —- строка t.

Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000. Строки не могут быть пустыми.

Формат вывода
Выведите True, если s является подпоследовательностью t, иначе —– False.

Пример 1
Ввод	
abc
ahbgdcu
Вывод
True
Пример 2
Ввод	
abcp
ahpc
Вывод
False
"""


def is_subsequence(str_1, str_2):
    start = 0
    for symbol in str_1:
        start = str_2.find(symbol, start)
        if start == -1:
            return False
        start += 1
    return True


def main():
    str_1 = input()
    str_2 = input()
    print(is_subsequence(str_1, str_2))


if __name__ == '__main__':
    main()
