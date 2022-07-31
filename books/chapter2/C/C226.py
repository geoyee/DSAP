"""
实现一个名为ReversedSequenceIterator的类，以此作为任何Python序列的反向迭代器。
第一次调用next返回序列的最后一个元素，第二次调用next返回倒数第二个元素，以此类推。
"""

import typing


class ReversedSequenceIterator:
    def __init__(self, sequence: typing.Sequence) -> None:
        self._seq = sequence
        self._k = len(sequence)

    def __next__(self) -> typing.Any:
        self._k -= 1
        if self._k >= 0:
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self


if __name__ == "__main__":
    data = list("Iterator")
    iters = ReversedSequenceIterator(data)
    for d in iters:
        print(d)
