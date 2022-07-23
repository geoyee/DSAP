"""
基于Python的解析语法和内置函数sum，写一个单独的命令来计算练习R16中的和。
"""


def sum_of_squares(n: int) -> int:
    return sum([i**2 for i in range(1, n + 1) if i % 2 == 1])


if __name__ == "__main__":
    n = 10
    print(n, sum_of_squares(n))
