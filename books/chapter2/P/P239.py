"""
基于拥有抽象方法area()和perimeter()的Polygon类发展继承层次结构。
实现扩展自基类的Triangle, Quadrilateral, Pentagon, Hexagon和Octagon类，伴随着具有明显意义的area()和perimeter()方法。
同时实现IsoscelesTriangle, EquilateralTriangle, Rectangle和Square类，它们有适当的继承关系。
最后，写一个简单的程序，允许用户创建各种类型的多边形，输入它们的几何尺寸，输出面积和周长。
附加功能：允许用户通过指定顶点坐标输入多边形，并能够测试两个多边形是否相似。
"""

from abc import ABCMeta, abstractmethod
import typing
from math import atan2, degrees

Number = typing.Union[int, float]  # typing.TypeVar("Number", int, float)


class Polygon(metaclass=ABCMeta):
    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        self.points: typing.List[typing.Tuple[Number, Number]] = points

    @abstractmethod
    def area(self) -> float:
        raise NotImplemented

    @abstractmethod
    def perimeter(self) -> float:
        raise NotImplemented


class AnyPolygon(Polygon):
    NAME = "AnyPolygon"

    @property
    def area(self) -> float:
        area = 0.0
        point_list = self.points.copy()
        point_list.append(point_list[0])
        for i in range(len(self.points)):
            x1, y1 = point_list[i]
            x2, y2 = point_list[i + 1]
            area += x1 * y2 - x2 * y1
        return 0.5 * abs(area)

    @property
    def perimeter(self) -> float:
        perimeter = 0.0
        point_list = self.points.copy()
        point_list.append(point_list[0])
        for i in range(len(self.points)):
            x1, y1 = point_list[i]
            x2, y2 = point_list[i + 1]
            perimeter += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return perimeter


class Triangle(AnyPolygon):
    NAME = "Triangle"

    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        if len(points) == 3:
            super().__init__(points)
        else:
            raise ValueError("This is not a triangle.")


class Quadrilateral(AnyPolygon):
    NAME = "Quadrilateral"

    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        if len(points) == 4:
            super().__init__(points)
        else:
            raise ValueError("This is not a quadrilateral.")


class Pentagon(AnyPolygon):
    NAME = "Pentagon"

    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        if len(points) == 5:
            super().__init__(points)
        else:
            raise ValueError("This is not a pentagon.")


class Hexagon(AnyPolygon):
    NAME = "Hexagon"

    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        if len(points) == 6:
            super().__init__(points)
        else:
            raise ValueError("This is not a hexagon.")


class Octagon(AnyPolygon):
    NAME = "Octagon"

    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        if len(points) == 8:
            super().__init__(points)
        else:
            raise ValueError("This is not an octagon.")


class IsoscelesTriangle(Triangle):
    NAME = "IsoscelesTriangle"

    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        if self.check(points):
            super().__init__(points)
        else:
            raise ValueError("This is not an isosceles triangle.")

    def check(
        self, points: typing.List[typing.Tuple[Number, Number]], same: int = 2
    ) -> bool:
        lines = []
        point_list = points.copy()
        point_list.append(point_list[0])
        for i in range(len(points)):
            x1, y1 = point_list[i]
            x2, y2 = point_list[i + 1]
            lines.append(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        if len(list(set(lines))) <= same:
            return True
        else:
            return False


class EquilateralTriangle(IsoscelesTriangle):
    NAME = "EquilateralTriangle"

    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        if self.check(points, 1):
            super().__init__(points)
        else:
            raise ValueError("This is not an equilateral triangle.")


class Rectangle(Quadrilateral):
    NAME = "Rectangle"

    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        if self.check(points):
            super().__init__(points)
        else:
            raise ValueError("This is not a rectangle.")

    def check(
        self, points: typing.List[typing.Tuple[Number, Number]], same: int = 2
    ) -> bool:
        lines = []
        point_list = points.copy()
        point_list.append(point_list[0])
        for i in range(len(points)):
            x1, y1 = point_list[i]
            x2, y2 = point_list[i + 1]
            lines.append(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        if len(list(set(lines))) <= same:
            return True
        else:
            return False


class Square(Rectangle):
    NAME = "Square"

    def __init__(self, points: typing.List[typing.Tuple[Number, Number]]) -> None:
        if self.check(points, 1):
            super().__init__(points)
        else:
            raise ValueError("This is not a square.")


def is_similar(poly1: AnyPolygon, poly2: AnyPolygon) -> bool:
    def _get_lines(
        points: typing.List[typing.Tuple[Number, Number]]
    ) -> typing.List[Number]:
        lines = []
        point_list = points.copy()
        point_list.append(point_list[0])
        for i in range(len(points)):
            x1, y1 = point_list[i]
            x2, y2 = point_list[i + 1]
            lines.append(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        lines = sorted(lines)
        return lines

    def _get_angles(
        points: typing.List[typing.Tuple[Number, Number]]
    ) -> typing.List[Number]:
        angs = []
        point_list = points.copy()
        point_list.insert(0, point_list[-1])
        point_list.append(point_list[1])
        for i in range(1, len(points) + 1):
            x1, y1 = point_list[i - 1]
            x2, y2 = point_list[i]
            x3, y3 = point_list[i + 1]
            deg1 = (360 + degrees(atan2(x1 - x2, y1 - y2))) % 360
            deg2 = (360 + degrees(atan2(x3 - x2, y3 - y2))) % 360
            angs.append(deg2 - deg1 if deg1 <= deg2 else 360 - (deg1 - deg2))
        angs = sorted(angs)
        return angs

    if poly1.NAME != poly2.NAME:
        return False
    lines1 = _get_lines(poly1.points)
    lines2 = _get_lines(poly2.points)
    rates = lines1[0] / lines2[0]
    for l1, l2 in zip(lines1, lines2):
        if abs((l1 / l2) - rates) > 1e-6:
            return False
    angs1 = _get_angles(poly1.points)
    angs2 = _get_angles(poly2.points)
    for a1, a2 in zip(angs1, angs2):
        if abs(a1 - a2) > 1e-6:
            return False
    return True


POLYGONS = [
    Triangle,
    Quadrilateral,
    Pentagon,
    Hexagon,
    Octagon,
    IsoscelesTriangle,
    EquilateralTriangle,
    Rectangle,
    Square,
]


if __name__ == "__main__":
    cps = []
    while True:
        name = input("Please input a polygon : ")
        if name.lower() == "esc":
            break
        for idx, polygon in enumerate(POLYGONS):
            if name == polygon.NAME:
                current_polygon = POLYGONS[idx]
                points = []
                while True:
                    inp = input(
                        "Please input a point, like (x1, y1) and input Q to exit : "
                    )
                    if inp.lower() == "q":
                        break
                    data = inp.split(",")
                    if len(data) == 2:
                        try:
                            points.append(
                                (float(data[0].strip()), float(data[1].strip()))
                            )
                        except:
                            raise ValueError("Input error.")
                    else:
                        raise ValueError("Input error.")
                cp = current_polygon(points)
                cps.append(cp)
                print("area is {} and perimeter is {}.".format(cp.area, cp.perimeter))
                if len(cps) == 2:
                    print(
                        "They are similar."
                        if is_similar(cps[0], cps[1])
                        else "They are not similar."
                    )
                    break
