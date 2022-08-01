"""
写一个Python程序，如输入标准的代数多项式，则输出该多项式的一阶导数。
"""


def derivation(func: str) -> str:
    func = func.replace("-", "+-")
    every = func.split("+")
    result = []
    for e in every:
        axn = e.split("*")
        if len(axn) == 2:
            a, xn = axn
            _xn = xn.split("^")
            if len(_xn) == 1:
                result.append(a)
            else:
                x, n = _xn
                result.append(
                    "".join([str(int(a) * int(n)), "*", x, "^", str(int(n) - 1)])
                )
    output = "+".join(result)
    output = output.replace("+-", "-").replace("^1", "")
    return output


if __name__ == "__main__":
    func = "5*x^3-4*x^2+9*x+7"
    print(func)
    print(derivation(func))
