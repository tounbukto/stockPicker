# Total Equity (Book Value of Equity): Found in the balance sheet under shareholders' equity.
# Net Income (Earnings): Found in the income statement.

class Revenue:
    def __init__(self, q1, q2, q3, q4):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
    
    def total(self):
        return self.q1 + self.q2 + self.q3 + self.q4

class Company:
    def __init__(self, name, stock_price, number_of_shares, assets, equity, cash, debt, revenue: Revenue, last_revenu: Revenue, EBITDA, net_income: Revenue, last_net_income: Revenue):
        self.name = name
        self.stock_price = stock_price
        self.number_of_shares = number_of_shares
        self.assets = assets
        self.equity = equity
        self.cash = cash
        self.debt = debt
        self.revenue = revenue
        self.last_revenu = last_revenu
        self.EBITDA = EBITDA
        self.net_income = net_income
        self.last_net_income = last_net_income
        

    def market_cap(self) -> float:
        return self.stock_price * self.number_of_shares

    def entreprise_value(self) -> float:
        return self.market_cap() - self.cash + self.debt