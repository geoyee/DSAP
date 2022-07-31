"""
编写一个Python函数minmax(data)，用来在数的序列中找出最小数和最大数，并以一个长度为2的元组形式返回。
不能通过内置函数min和max来实现。
"""

import typing

Number = typing.TypeVar("Number", int, float)


def minmax(data: typing.Sequence[Number]) -> typing.Tuple[Number, Number]:
    if len(data) == 0:
        raise ValueError("The lenght of data must greater than or equal to 1.")
    mmin = data[0]
    mmax = data[0]
    for d in data:
        if d < mmin:
            mmin = d
        elif d > mmax:
            mmax = d
    return (mmin, mmax)


if __name__ == "__main__":
    data = [1, 58, 47, 2.44, 3.9, -41, 265, -0.47]
    print(data)
    print(minmax(data))
