"""
https://contest.yandex.ru/contest/24734/problems/D/
Печеньки

К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.

Но не всё так просто. Печенья могут быть разного размера. А у каждого ребёнка есть фактор жадности —– минимальный размер печенья, которое он возьмёт. Нужно выяснить, сколько ребят останутся довольными в лучшем случае, когда они действуют оптимально.

Каждый ребёнок может взять не больше одного печенья.

Формат ввода
В первой строке записано n —– количество детей.

Во второй —– n чисел, разделённых пробелом, каждое из которых –— фактор жадности ребёнка. Это натуральные числа, не превосходящие 1000.

В следующей строке записано число m –— количество печенек.

Далее —– m натуральных чисел, разделённых пробелом —– размеры печенек. Размеры печенек не превосходят 1000.

Оба числа n и m не превосходят 10000.

Формат вывода
Нужно вывести одно число –— количество детей, которые останутся довольными

Пример 1
Ввод	
2
1 2
3
2 1 3
Вывод
2
Пример 2
Ввод	
3
2 1 3
2
1 1
Вывод
1
"""


def read():
    _ = int(input())
    children_greed_factors = list(map(int, input().split()))
    _ = int(input())
    cookies = list(map(int, input().split()))
    return children_greed_factors, cookies


def get_number_satisfied(children_greed_factors, cookies):
    number_satisfied = 0
    children_greed_factors.sort()
    cookies.sort()
    start_cookies = 0
    for factor in children_greed_factors:
        for i in range(start_cookies, len(cookies)):
            if cookies[i] >= factor:
                number_satisfied += 1
                start_cookies = i + 1
                break
    return number_satisfied


def main():
    children_greed_factors, cookies = read()
    number_satisfied = get_number_satisfied(children_greed_factors, cookies)
    print(number_satisfied)


if __name__ == '__main__':
    main()