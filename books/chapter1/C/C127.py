"""
在1.8节中，我们对于计算所给整数的因子时提供了3种不同的生成器的实现方法。1.8节末尾的第三种方法是最有效的，但我们注意到，它没有按照递增顺序来产生因子。修改生成器，使其按照递增顺序来产生因子，同时保持其性能优势。
"""


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        future = a + b
        a = b
        b = future


if __name__ == "__main__":
    for idx, i in enumerate(fibonacci()):
        print(i)
        if idx == 10:
            break
