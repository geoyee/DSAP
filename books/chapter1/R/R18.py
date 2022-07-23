"""
Python允许负整数作为序列的索引值，如一个长度为n的字符串s，当索引值为-n<=k<0时，所指的元素为s[k]，那么求一个正整数索引值j>=0，是的s[j]指向的也是相同的元素。
"""


def find_index(n: str, k: int) -> int:
    return len(n) + k


if __name__ == "__main__":
    n = "Hello python!"
    k = -4
    print(n[k], n[find_index(n, k)])
