"""
编写Python程序，将以下句子“I will never spam my friends agian.”写100次。程序应该对每个句子进行计数，另外，应有8次不同的随机输入错误。
"""

import random

WORDS = [chr(ord("a") + i) for i in range(26)]


def randomreplace(strs: str) -> str:
    rnd_idx = random.randrange(0, len(strs))
    str_list = list(strs)
    while True:
        rp_word = random.choice(WORDS)
        if rp_word != str_list[rnd_idx]:
            str_list[rnd_idx] = rp_word
            return "".join(str_list)


if __name__ == "__main__":
    strs = "I will never spam my friends agian."
    rnd_inds = [random.randrange(0, 100) for _ in range(8)]
    for i in range(100):
        if i in rnd_inds:
            print(i, randomreplace(strs))
        else:
            print(i, strs)
