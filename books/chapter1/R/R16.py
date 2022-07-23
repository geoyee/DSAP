"""
编写一个Python函数，用来接收正整数n，并返回1~n中所有奇数的平方和。
"""


def sum_of_squares(n: int) -> int:
    num = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            num += i**2
    return num


if __name__ == "__main__":
    n = 10
    print(n, sum_of_squares(n))
