"""
编写一个Python程序来模拟简单计算器。计算器每一次输入为一个单独行，可以是数值或操作符。每次输入后显示结果。
"""

import typing


Number = typing.TypeVar("Number", int, float)


if __name__ == "__main__":
    inputs = []
    while True:
        inp = input()
        inputs.append(inp)
        if inp == "=":
            break
    display = "".join(inputs)
    display += str(eval(display[:-1]))
    print("Output:", display)
