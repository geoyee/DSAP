"""
编写一个函数用来逆置n个整数的列表，并将该方法与可以实现相同功能的Python函数进行比较。
"""

import typing


def my_reverse(data: typing.List[int]) -> typing.List[int]:
    tmp = data.copy()
    result = []
    while len(tmp) != 0:
        result.append(tmp.pop(-1))
    return result


if __name__ == "__main__":
    data = [1, 2, 3, 45, 8, 99, 21]
    print(my_reverse(data))
    print(list(reversed(data)))
    print(data[::-1])
