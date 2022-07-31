"""
生日悖论是指当房间人数n超过23时，那么该房间里有两个人生日相同的可能性大于50%。
设计一个程序，通过随机数生成的生日实验来验证这个悖论，例如n=5/10/15/20/.../100测试。
"""

import time
import random
import typing


def random_birthday() -> str:
    M = random.randint(1, 12)
    if M in [1, 3, 5, 7, 8, 10, 12]:
        D = random.randint(1, 31)
    elif M in [4, 6, 9, 11]:
        D = random.randint(1, 30)
    else:
        D = random.randint(1, 28)
    return str(M) + "/" + str(D)


def check_same(bd_list: typing.List[str]) -> bool:
    bd_list = sorted(bd_list)
    for i in range(len(bd_list) - 1):
        if bd_list[i] == bd_list[i + 1]:
            return True
    return False


if __name__ == "__main__":
    for n in range(5, 105, 5):
        result = 0
        random.seed(time.time())
        for i in range(100):
            bd_list = [random_birthday() for _ in range(n)]
            result += int(check_same(bd_list))
        print(n, result / 100)
