"""编写一个Python函数is_multiple(n, m)，用来接收两个整数n和m，如果n是m的倍数，即存在整数i是的n=mi，那么函数返回True，否则返回False。
"""


def is_multiple(n: int, m: int) -> bool:
    if n % m == 0:
        return True
    return False


if __name__ == "__main__":
    n = 100
    m1 = 10
    m2 = 11
    print(n, m1, is_multiple(n, m1))
    print(n, m2, is_multiple(n, m2))
