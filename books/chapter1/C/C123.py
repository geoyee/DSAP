"""
给出一个Python代码片段的例子，编写一个索引可能越界的元素列表。如果索引越界，程序应该捕获异常结果并打印以下错误消息：
"Don't try buffer overflow attacks in Python!"
"""

if __name__ == "__main__":
    data = list(range(5))
    for i in range(6):
        try:
            print(data[i])
        except IndexError:
            print("Don't try buffer overflow attacks in Python!")
