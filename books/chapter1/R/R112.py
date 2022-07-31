"""
在Python的random包中，只使用randrange函数，实现自己的choice函数。
"""

import random
import typing


def my_choice(data: typing.Sequence) -> typing.Any:
    end = len(data)
    return data[random.randrange(end)]


if __name__ == "__main__":
    data = [12, 0.54, -652, "r", 33, [1, 0], 69, True, 2.0]
    print(random.choice(data))
    print(my_choice(data))
