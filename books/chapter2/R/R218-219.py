"""
给出一个Python代码片段，使用2.4.2节的Progression类，找到那个以2开始且以2作为前两个值的斐波那契数列的第8个值。
"""

import math


class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(" ".join(str(next(self) for j in range(n))))


class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._current + self._prev


if __name__ == "__main__":
    f = FibonacciProgression(2, 2)
    for i, n in enumerate(f):
        if i == 7:
            print(n)
            break
    print(math.ceil(2e63 / 128))
