"""
在Python的random包中，只使用randint函数，实现自己的shuffle函数。
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
