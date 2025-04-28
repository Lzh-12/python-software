class Account:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    # 开户
    def get(self):
        print(f"账户名称：{self.name}, 余额：{self.money}")


if __name__ == '__main__':
    account = Account('小明', 100000)
    account.get()
