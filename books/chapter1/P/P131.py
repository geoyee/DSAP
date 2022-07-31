"""
编写一个Python程序。程以需要支付的钱数和已支付的钱数为输入，返回需要找零的钱的类型和数量。
尽可能返回少的钱币。
"""

import typing


CYN = [100, 50, 20, 10, 5, 1, 0.5, 0.1]
Number = typing.TypeVar("Number", int, float)


def give_change(price: Number, payment: Number) -> typing.Dict[str, int]:
    results = {str(cyn): 0 for cyn in CYN}
    change = int(10 * (payment - price))
    for k in results.keys():
        nk = int(float(k) * 10)
        results[k] = change // nk
        change %= nk
    return results


if __name__ == "__main__":
    price = 1121.4
    payment = 2050
    print(give_change(price, payment))
