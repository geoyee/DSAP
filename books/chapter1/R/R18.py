"""
编写一个Python程序，找出一个长度为n的字符串s中负索引对应的正索引值。
"""


def find_index(n: str, k: int) -> int:
    return len(n) + k


if __name__ == "__main__":
    n = "Hello python!"
    k = -4
    print(n[k], n[find_index(n, k)])
