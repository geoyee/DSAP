"""
Python的random模块包括一个函数shuffle(data)，它可以接收一个元素列表和一个随机的重新排列元素，以使每个可能的序列发生概率相等。random模块还包括一个更基本的函数randint(a, b)，它可以返回一个从a到b（包括两端点）的随机数。只使用randint函数，实现自己的shuffle函数。
"""

import random
import typing


def my_shuffle(data: typing.List) -> None:
    tmp = data.copy()
    for i in range(len(data)):
        data[i] = tmp.pop(random.randint(0, len(tmp) - 1))


if __name__ == "__main__":
    data = list(range(20))
    print(data)
    random.shuffle(data)
    print(data)
    my_shuffle(data)
    print(data)
