"""
编写一个Python程序来模拟手持计算器。程序可以处理控制台（表示push按钮）的输入，每个操作完成后将内容输出到屏幕。
计算器至少要有基本运算和清除操作。
"""

if __name__ == "__main__":
    result = 0.0
    while True:
        inp = input()
        if inp == "cls":
            result = 0
        elif inp[0] in ["+", "-", "*", "/"]:
            result = float(eval(str(result) + inp))
        else:
            try:
                result = float(inp)
            except ValueError:
                result = float(eval(inp))
        print("Output:", result)
