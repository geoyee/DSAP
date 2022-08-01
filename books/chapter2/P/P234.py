"""
写一个Python程序，如输入一个文件，则输出一个柱形图表，以显示文档中每个字母字符出现的频率。
"""

from string import punctuation
import typing
import matplotlib.pyplot as plt


def state_words(strs: str) -> None:
    word_dict: typing.Dict[str, int] = dict()
    for s in strs:
        if s not in list(punctuation) and s != " ":
            s = s.lower()
            if s not in word_dict.keys():
                word_dict[s] = 1
            else:
                word_dict[s] += 1
    label = sorted(list(word_dict.keys()))
    data = [word_dict[lab] for lab in label]
    plt.bar(range(len(data)), data)
    plt.xticks(range(len(data)), label)
    plt.show()


if __name__ == "__main__":
    # # Read file
    # with open("file", "r") as f:
    #     strs = f.read()
    # strs = strs.strip()
    strs = "Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python."
    state_words(strs)
