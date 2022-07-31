"""
实现__sub__方法，返回u-v的向量实例。
实现__neg__方法，返回-v的向量实例。
实现__mul__方法，返回v*n的向量实例。
使add/sub/mul方法与列表/整数进行计算可以左右互换。
实现__mul__方法，返回v*u的向量实例。
修改构造函数，使它可以接收任意参数，整数或者序列
"""

import typing


class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        elif isinstance(d, typing.Iterable):
            self._coords = list(d)

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def _add(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree.")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        result._coords = -self._coords
        return result

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree.")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __rsub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree.")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j] - self[j]
        return result

    def _mul(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("dimensions must agree.")
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
            return result
        elif isinstance(other, (int, float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result
        else:
            raise TypeError("other must be vector or number.")

    def __mul__(self, other):
        return self._mul(other)

    def __rmul__(self, other):
        return self._mul(other)

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"


if __name__ == "__main__":
    a = Vector(3)
    print(a)
    b = Vector([2, 9, 4])
    print(b)
    c1 = a + [1, 2, 3]
    c2 = [1, 2, 3] + a
    print(c1, c2, c1 == c2)
    d1 = b * 2
    d2 = 2 * b
    print(d1, d2, d1 == d2)
    e1 = d1 - c1
    e2 = c1 - d1
    print(e1, e2, e1 != e2)
    f = c1 * d1
    print(f, -f)
