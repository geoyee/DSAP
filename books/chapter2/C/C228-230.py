"""
2.4.1节的PredatoryCreditCard类
增加一个功能，在本月内，一旦用户完成十次呼叫，就需要对其收取费用。每增加一个额外的呼叫，收取1美元的附加费。
增加一个功能，给用户分配一个每月最低付款额，作为账户的一部分，如果客户在下一个月周期之前没有连续地支付最低金额，则要评估延迟的费用。
修改CreditCard和PredatoryCreditCard，使子类无法直接访问数据成员_balance。
"""


class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def set_balance(self, balance, op="="):
        if op == "=":
            self._balance = balance
        elif op == "+":
            self._balance += balance
        elif op == "*":
            self._balance *= balance
        else:
            raise ValueError("op must be `=`/`+`/`*`, not {}.".format(op))

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._k = 0
        self._mini_paid = 10
        self._paid = 0
        self._delay_charge = 1.01

    def charge(self, price):
        self._k += 1
        success = super().charge(price)
        if not success:
            self.set_balance(5, "+")
        return success

    def make_payment(self, amount):
        self.set_balance(-amount, "+")
        self._paid += 0

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self.set_balance(monthly_factor, "+")
        if self._k > 10:
            self.set_balance((self._k - 10), "+")
        if self._paid < self._mini_paid:
            self.set_balance(self._delay_charge, "*")
        self._k = 0
        self._paid = 0


if __name__ == "__main__":
    wallet = PredatoryCreditCard(
        "John Bowman", "California Savings", "5391 0375 9387 5309", 2500, 0.001
    )
    print("Balance =", wallet.get_balance())
    for _ in range(8):
        wallet.charge(1)
    wallet.process_month()
    print("Balance =", wallet.get_balance())
    for _ in range(12):
        wallet.charge(1)
    wallet.process_month()
    print("Balance =", wallet.get_balance())
    for _ in range(20):
        wallet.charge(1)
    wallet.make_payment(10)
    print("Balance =", wallet.get_balance())
