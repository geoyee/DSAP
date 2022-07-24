"""
演示如何使用Python列表解析语法来产生列表[0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
"""

if __name__ == "__main__":
    print([i * (i + 1) for i in range(10)])
