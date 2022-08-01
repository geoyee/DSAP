"""
写一个Python程序来模拟生态系统，其中包含两种类型的动物——熊与鱼。
生态系统还包括一条河流，它被建模为一个比较大的列表。
列表中的每一个元素应该是一个Bear对象、一个Fish对象或者None。
在每一个时间步长，基于随机过程，每一个动物都试图进入一个相邻的列表位置或停留在原处。
如果两只相同类型的动物竞争同一单元格，那么它们留在原处，但它们创造了这种类型动物的新实例，实例放置在列表中的一个随机（即以前为None）位置。
如果一头熊和一条鱼竞争，那么鱼就会死亡（即它消失了)。
添加一个模拟器，添加一个布尔值gender字段和一个浮点strength字段到每一个动物，使用Animal类作为基础类。
如果两只同一类型的动物竞争，如果它们是不同性别的动物，那么这种类型只创建一个新的实例；否则，如果两只相同类型和性别的动物竞争，那么只有力量更大的动物才会生存。
"""

import random
import time
import typing
import os


class Animal:
    def __init__(
        self,
        loc: typing.Tuple[int, int],
        gender: typing.Optional[str] = None,
        strength: typing.Optional[float] = None,
    ) -> None:
        self.loc = loc
        self.type = ""
        self._gender = gender if gender is not None else random.choice(["F", "M"])
        self._strength = strength if strength is not None else random.random()

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def strength(self) -> float:
        return self._strength

    def move(self, i: int, j: int) -> None:
        self.loc = (i, j)


class Bear(Animal):
    def __init__(self, loc: typing.Tuple[int, int]) -> None:
        super().__init__(loc)
        self.type = "bear"


class Fish(Animal):
    def __init__(self, loc: typing.Tuple[int, int]) -> None:
        super().__init__(loc)
        self.type = "fish"


class Ecosystem:
    def __init__(self) -> None:
        self.init()
        self.create_animals()

    def init(self, size: int = 5) -> None:
        self.size = size
        self.range: typing.List[typing.List] = []
        for _ in range(size):
            _range: typing.List = []
            for _ in range(size):
                _range.append("□")
            self.range.append(_range)

    def create_animals(self, num_bear: int = 5, num_fish: int = 5):
        self.animals: typing.List[Animal] = []
        random.seed(time.time())
        self.num_animal = num_bear + num_fish
        locs = []
        while True:
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            if (i, j) not in locs:
                locs.append((i, j))
                if len(locs) == self.num_animal:
                    break
        for idx, loc in enumerate(locs):
            i, j = loc
            if idx < num_bear:
                self.animals.append(Bear((i, j)))
            else:
                self.animals.append(Fish((i, j)))

    def draw(self) -> None:
        self.init()
        for animal in self.animals:
            i, j = animal.loc
            if isinstance(animal, Bear):
                self.range[i][j] = "■"
            else:  # Fish
                self.range[i][j] = "●"
        os.system("cls")
        for i in range(self.size):
            for j in range(self.size):
                print(self.range[i][j] + " ", end="")
            print("\r")

    def update(self) -> None:
        _locs = []
        for animal in self.animals:
            while True:
                i, j = animal.loc
                dic = random.randint(0, 3)
                if dic == 0:
                    i -= 1
                elif dic == 1:
                    i += 1
                elif dic == 2:
                    j -= 1
                else:  # 3
                    j += 1
                if 0 <= i < self.size and 0 <= j < self.size:
                    break
            animal.move(i, j)
            _locs.append((i, j))
        del_list = []
        add_list = []
        for i in range(self.num_animal - 1):
            animal = self.animals[i]
            for j in range(i + 1, self.num_animal):
                oth_animal = self.animals[j]
                if animal.loc == oth_animal.loc:
                    if animal.type == oth_animal.type:
                        if animal.gender == oth_animal.gender:
                            del_list.append(
                                i if animal.strength <= oth_animal.strength else j
                            )
                        else:
                            while True:
                                i = random.randint(0, self.size - 1)
                                j = random.randint(0, self.size - 1)
                                if (i, j) not in _locs:
                                    add_list.append(
                                        Bear((i, j))
                                        if animal.type == "bear"
                                        else Fish((i, j))
                                    )
                                    break
                    else:
                        del_list.append(i if animal.type == "fish" else j)
        for element in [self.animals[i] for i in del_list]:
            if element in self.animals:
                self.animals.remove(element)
        self.animals.extend(add_list)
        self.num_animal = len(self.animals)


if __name__ == "__main__":
    ecosystem = Ecosystem()
    while True:
        ecosystem.update()
        ecosystem.draw()
        time.sleep(1)
