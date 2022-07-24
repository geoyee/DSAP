"""
编写一个Python函数，接收一个表示一个句子的字符串s，然后返回该字符串的删除了所有标点符号的副本。
"""

from string import punctuation
from copy import deepcopy


def remove_punctuation(strs: str) -> str:
    result = deepcopy(strs)
    for p in list(punctuation):
        result = result.replace(p, "")
    return result


if __name__ == "__main__":
    strs = "Let's try, Mike."
    print(strs)
    print(remove_punctuation(strs))
