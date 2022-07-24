"""
编写一个Python函数，用来接收一个整数序列，并判断该序列中是否存在一对乘积是奇数的互不相同的数。
"""

import typing

Number = typing.TypeVar("Number", int, float)


def check_same(data: typing.Sequence[Number]) -> bool:
    tmp = sorted(data)
    for i in range(len(tmp) - 1):
        if tmp[i] == tmp[i + 1]:
            return True
    return False


if __name__ == "__main__":
    data1 = [1, 2, 3, 5, 4, 8, 8.9, 4.0, 3.0, 99]
    data2 = [1, 2, 3, 5, 4, 8, 8.9, 4, 3.0, 99]
    data3 = [1, 2.2, 3, 5, 4.4, 8, 9, 7, 30, 99]
    print(data1, check_same(data1))
    print(data2, check_same(data2))
    print(data3, check_same(data3))
