"""
编写一个程序，需要从控制台输入3个整数a，b，c，并确定它们是否可以在一个正确的算术公式（给定顺序）下成立。
"""


def check_func(a: int, b: int, c: int, func: str) -> bool:
    try:
        letf, right = func.split("=")
        if eval(letf) == eval(right):
            return True
        else:
            return False
    except:
        return False


if __name__ == "__main__":
    print(check_func(1, 2, 3, "a+b=c"))
    print(check_func(1, 3, 2, "a=b-c"))
    print(check_func(3, 2, 1, "a*b=c"))
