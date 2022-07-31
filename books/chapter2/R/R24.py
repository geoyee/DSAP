"""
编写一个Python类Flower，该类具有str、int和float类型的三种实例变量，分别代表花的名字、花瓣数和价格。
该类包含一个构造函数，初始化为合适的值。该类包含设置和检索每种类型值的方法。
"""


class Flower:
    def __init__(
        self, name: str = "向日葵", petal_number: int = 21, price: float = 10
    ) -> None:
        self._name = name
        self._petal_number = petal_number
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def petal_number(self) -> int:
        return self._petal_number

    @petal_number.setter
    def petal_number(self, petal_number: int) -> None:
        self._petal_number = petal_number

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        self._price = price


if __name__ == "__main__":
    flower = Flower()
    print(flower.name)
    flower.name = "菊花"
    print(flower.name)
