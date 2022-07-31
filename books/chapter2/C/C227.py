"""
对于2.3.5节中的Range，通过试验证明2 in Range(10000000)对比9999999 in Range(10000000)的相对速度。
请提供一种__contains__方法更有效的实现，以确定特定的值是否属于给定范围内。所提供方法的运行时间应独立于范围的大小。
"""

import time


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("step cannot be 0.")
        if stop is None:
            start, stop = 0, start
        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError("index out of range.")
        return self._start + k * self._step


class Range2(Range):
    def __contains__(self, n):
        if (n - self._start) % self._step == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    r = Range(10000000)
    start_time = time.time()
    if 2 in r:
        print("Find 2:", time.time() - start_time)
    if 9999999 in r:
        print("Find 9999999:", time.time() - start_time)
    r2 = Range2(10000000)
    start_time2 = time.time()
    if 2 in r2:
        print("Find 2:", time.time() - start_time2)
    if 9999999 in r2:
        print("Find 9999999:", time.time() - start_time2)
