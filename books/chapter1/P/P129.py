"""
编写一个Python程序，输出由字母c，a，t，d，o，g组成的所有可能的字符串（每个字母只能使用一次）。
"""

import typing


def randmerge(strs: typing.Sequence[str]) -> typing.List[str]:
    def words(
        letters: typing.Set[str], word: str = "", results: typing.List = []
    ) -> None:
        if not letters:
            results.append(word)
        for letter in letters:
            words(letters - {letter}, word + letter, results)

    results: typing.List[str] = []
    words(set(strs), results=results)
    return results


if __name__ == "__main__":
    strs = ["c", "a", "t", "d", "o", "g"]
    res = randmerge(strs)
    print(len(res))
    print(res)
