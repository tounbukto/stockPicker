from company import Company

def net_profit_margin(company: Company) -> float:
    return 100 * company.current_net_income.total() / company.revenue.total()

def return_on_assets(company: Company) -> float:
    return 100 * company.current_net_income.total() / company.assets

def return_on_equity(company: Company) -> float:
    return 100 * company.current_net_income.total() / company.equity # stake holder equity ???

def operating_margin(company: Company) -> float:
    return 100 * company.current_net_income.total() / company.revenue.total() # not net income but the operating income