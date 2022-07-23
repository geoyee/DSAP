"""
演示怎样使用Python列表解析语法来产生列表[1, 2, 4, 8, 16, 32, 64, 128, 256]。
"""

if __name__ == "__main__":
    end = 9
    print([2**i for i in range(end)])
