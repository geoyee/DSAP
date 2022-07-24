"""
编写norm函数，即norm(v, p)，返回向量v的p范数的值，norm(v)，返回v的欧几里得范数。你可以假设v是一个数字列表。
"""

import typing

Number = typing.TypeVar("Number", int, float)


def norm(v: typing.List[Number], p: int = 2) -> Number:
    return sum([vi**p for vi in v]) ** (1 / p)


if __name__ == "__main__":
    v = [4, 3]
    print(norm(v))
    print(norm(v, 3))
