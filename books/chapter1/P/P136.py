"""
编写一个Python程序，输入一个由空格分隔的单词列表，并输出列表中的每个单词出现的次数，不用担心效率。
"""

import typing
from string import punctuation
from copy import deepcopy


def remove_punctuation(strs: str) -> str:
    result = deepcopy(strs)
    for p in list(punctuation):
        result = result.replace(p, "")
    return result


def state_word(strs: str) -> typing.Dict[str, int]:
    result: typing.Dict[str, int] = dict()
    strs = remove_punctuation(strs)
    word_list = strs.split(" ")
    for word in word_list:
        if word not in result.keys():
            result[word] = 1
        else:
            result[word] += 1
    return result


if __name__ == "__main__":
    letter = "PaddleSeg is an end-to-end high-efficent development toolkit for image segmentation based on PaddlePaddle, which helps both developers and researchers in the whole process of designing segmentation models, training models, optimizing performance and inference speed, and deploying models. A lot of well-trained models and various real-world applications in both industry and academia help users conveniently build hands-on experiences in image segmentation."
    print(state_word(letter))
