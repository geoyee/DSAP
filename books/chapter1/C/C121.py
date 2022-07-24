"""
编写一个Python程序，反复从标准输入读取一行直到抛出EOFError异常，然后以相反的顺序输出这些行（用户可以通过键按Ctrl+D（windows是Ctrl+Z）结束输入）。
"""

if __name__ == "__main__":
    inputs = []
    while True:
        try:
            inputs.append(input())
        except EOFError:
            break
    print(list(reversed(inputs)))
