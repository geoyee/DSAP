"""
写一个Python程序，模拟一个支持电子书阅读器的功能系统。
你应该为用户在系统中提供“买”新书, 查看他们所购买书的名单以及阅读所购买的书籍的方法。
系统应该使用实际的书籍（其版权已经过期并可在互联网上获得)，为系统用户“购买”和阅读提供可用的书籍。
"""

import typing


class User:
    def __init__(self, account: str, password: str) -> None:
        self.account = account
        self.__password = password
        self.books: typing.List[str] = []

    def check(self, account: str, password: str) -> bool:
        if account == self.account and password == self.__password:
            return True
        else:
            return False

    def buy(self, book: str) -> None:
        if book not in self.books:
            self.books.append(book)
            print("Successfully purchased {}.".format(book))
        else:
            print("You have purchased{}.".format(book))

    def read(self, book: str) -> None:
        if book in self.books:
            print("Start reading {}.".format(book))
        else:
            print("You did not purchased {}.".format(book))


class BookSystem:
    def __init__(self) -> None:
        self.books: typing.List[str] = [
            "水浒传",
            "西游记",
            "三国演义",
            "红楼梦",
            "西厢记",
            "聊斋志异",
            "儒林外史",
            "牡丹亭",
            "离骚",
            "金瓶梅",
        ]
        self.users: typing.List[User] = []
        self.current_user: typing.Optional[User] = None

    def register(self) -> None:
        account = input("Please input your account : ")
        password = input("Please input your password : ")
        user = User(account, password)
        for u in self.users:
            if user.account == u.account:
                print("Account already exists.")
                return
        self.users.append(user)
        print("Register successfully.")

    def login(self) -> None:
        account = input("Please input your account : ")
        password = input("Please input your password : ")
        for user in self.users:
            if user.check(account, password):
                self.current_user = user
                print("Welcome, {}.".format(user.account))
                return
        print("Cannt Login.")

    def buy(self) -> None:
        book = input("Please input the title of the book you want to buy : ")
        if book not in self.books:
            print("{} cannt find.".format(book))
            return
        if self.current_user is not None:
            self.current_user.buy(book)
        else:
            print("Please login.")

    def read(self) -> None:
        book = input("Please input the title of the book you want to read : ")
        if self.current_user is not None:
            self.current_user.read(book)
        else:
            print("Please login.")


if __name__ == "__main__":
    book_system = BookSystem()
    while True:
        op = input("What you want to do : ").lower()
        if op == "register":
            book_system.register()
        elif op == "login":
            book_system.login()
        elif op == "buy":
            book_system.buy()
        elif op == "read":
            book_system.read()
        elif op == "esc":
            break
