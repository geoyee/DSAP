"""
Python的random模块包括一个函数choice(data)，可以从一个非空序列返回一个随机元素。Random模块还包括一个更基本的randrange函数，参数化类似于内置的range函数，可以在给定范围内返回一个随机数。只使用randrange函数，实现自己的choice函数。
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
