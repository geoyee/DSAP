"""
演示如何使用Python列表解析语法在不输入所有26个英文字母的情况下产生列表["a", "b", ..., "z"]
"""

if __name__ == "__main__":
    print([chr(ord("a") + i) for i in range(26)])
