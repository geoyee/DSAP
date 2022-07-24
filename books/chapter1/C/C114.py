"""
编写一个Python函数，用来接收一个整数序列，并判断该序列中是否存在一对乘积是奇数的互不相同的数。
"""

import typing


def check_req_opt(data: typing.Sequence[int]) -> bool:
    number_odd = 0
    for d in data:
        if d % 2 == 1:
            number_odd += 1
        if number_odd >= 2:
            return True
    return False


if __name__ == "__main__":
    data1 = list(range(2, 20000, 2))
    data2 = data1.copy()
    data2.extend([1, 3])
    print(check_req_opt(data1))
    print(check_req_opt(data2))
