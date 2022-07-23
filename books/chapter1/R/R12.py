"""
编写一个Python函数is_even(k)，用来接收一个k，如果k是偶数返回True，否则返回False。但是，函数中不能使用乘法、除法或取余操作。
"""


def is_even(k: int) -> bool:
    return bin(k)[-1] == "0"


if __name__ == "__main__":
    k1 = 10
    k2 = 11
    print(k1, is_even(k1))
    print(k2, is_even(k2))
