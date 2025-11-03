class Bank:

    def __init__(self, balance: List[int]):
        self.balances =  {}
        for i in range(len(balance)):
            self.balances[i] = balance[i]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1-1 not in self.balances or account2-1 not in self.balances:
            return False
        if self.balances[account1-1] < money:
            return False
        self.balances[account1-1] -= money
        self.balances[account2-1]+= money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account -1 not in self.balances:
            return False
        self.balances[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account-1 not in self.balances:
            return False
        if self.balances[account-1] < money:
            return False
        self.balances[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)