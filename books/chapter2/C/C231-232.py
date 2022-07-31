"""
扩展Progression类，使每个值都是前两个值差的绝对值，使用2和200作为默认值。
扩展Progression类，使每个值都是前一个值的平方根，使用65536作为默认值。
"""


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


class Progression1(Progression):
    def __init__(self, first=2, second=200):
        super().__init__(first)
        self._prev = self._current + second

    def _advance(self):
        self._current, self._prev = abs(self._prev - self._current), self._current


class Progression2(Progression):
    def __init__(self, start=65536):
        super().__init__(start)

    def _advance(self):
        self._current = self._current**0.5


if __name__ == "__main__":
    p1 = Progression1()
    p2 = Progression2()
    for i, (d1, d2) in enumerate(zip(p1, p2)):
        if i == 10:
            break
        print(d1, d2)
