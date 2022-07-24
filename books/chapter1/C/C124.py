"""
编写一个Python函数，计算所给字符串中的元音字母个数。
"""

VOWEL = ["a", "e", "i", "o", "u"]


def count_vowel(strs: str) -> int:
    count = 0
    for s in strs:
        if s.lower() in VOWEL:
            count += 1
    return count


if __name__ == "__main__":
    strs = "It is a good day!"
    print(count_vowel(strs))
