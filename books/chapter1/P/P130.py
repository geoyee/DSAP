"""
编写一个Python程序，输入一个大于2的正整数，求该数反复被2整除直到商小于2为止的次数。
"""


def number2(n: int) -> int:
    count = 0
    while n >= 2:
        n //= 2
        count += 1
    return count


if __name__ == "__main__":
    n = 101
    print(n, number2(n))
