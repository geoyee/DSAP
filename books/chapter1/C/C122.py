"""
编写一个Python程序，用来接收长度为n的两个整型数组a和b并返回数组a和b的点积。
"""

import typing


def dot(a: typing.List[int], b: typing.List[int]) -> typing.List[int]:
    c = []
    for ai, bi in zip(a, b):
        c.append(ai * bi)
    return c


if __name__ == "__main__":
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8, 10]
    print(dot(a, b))
