"""
写一组Python类，可以模拟网络应用程序的其中一方Alice，定期创建一组她想发给Bob的包。
互联网进程不断检查是否Alice有想要发送的包，如果有，就发送至Bob的计算机。
Bob定期检查自己的计算机，以确定是否收到来自Alice的包，如果有，他将阅读并删除包。
"""

import time
import typing


class Alice:
    def __init__(self, interval: int) -> None:
        self.interval = interval

    def create_package(self) -> str:
        return "package_" + str(time.time())


class Bob:
    def __init__(self, interval: int) -> None:
        self.interval = interval
        self._packages: typing.List[str] = []

    def receive_package(self, package: str) -> None:
        self._packages.append(package)

    def read_and_delete_package(self) -> None:
        while len(self._packages) != 0:
            print("I have read {}.".format(self._packages.pop()))


class Network:
    def __init__(self, alice: Alice, bob: Bob) -> None:
        self._alice = alice
        self._bob = bob
        self._k = 0

    def monitor(self) -> None:

        while True:
            if self._k % self._alice.interval == 0:
                self._bob.receive_package(self._alice.create_package())
            if self._k % self._bob.interval == 0:
                self._bob.read_and_delete_package()
            time.sleep(1)
            self._k += 1


if __name__ == "__main__":
    alice = Alice(2)
    bob = Bob(3)
    network = Network(alice, bob)
    network.monitor()
