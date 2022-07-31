"""
修改2.14中的Sequence使其包含__eq__方法，用于判断两个序列相等。
添加__lt__支持字典比较seq1<seq2。
"""

from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        raise NotImplemented

    @abstractmethod
    def __getitem__(self, j):
        raise NotImplemented

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("value not in sequence.")

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True


class List(Sequence):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, j):
        return self.data[j]


class Dict(Sequence):
    def __init__(self, data):
        self.data = dict(sorted(data.items(), key=lambda x: x[0]))

    def __len__(self):
        return len(self.data.keys())

    def __getitem__(self, j):
        key = list(self.data.keys())[j]
        return key

    def __lt__(self, other):
        if len(self) < len(other):
            return True
        elif len(self) > len(other):
            return False
        else:
            for k1, k2 in zip(self, other):
                if k1 < k2:
                    return True
                elif k1 > k2:
                    return False
                else:
                    if self.data[k1] < other.data[k2]:
                        return True
                    elif self.data[k1] > other.data[k2]:
                        return False
            return False


if __name__ == "__main__":
    a = List([1, 2, 3])
    b = List([1, 2, 3])
    c = List([1, 2, 4])
    print(a == b, a == c)
    a2 = Dict({"a": 1, "b": 2})
    b2 = Dict({"a": 1, "b": 2})
    c1 = Dict({"a": 2, "b": 2})
    c2 = Dict({"c": 1, "b": 2})
    c3 = Dict({"a": 2, "b": 2, "c": 3})
    print(a2 < b2, a2 < c1, a2 < c2, a2 < c3)
