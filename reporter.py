from company import Company
import valuation_ratios as val
import profitabilty_ratios as profit
import growth_metrics as grth


class Growth:
    def __init__(self, revenue_growth, revenu_growth_per_quarter, earning_growth_rate, earning_growth_rate_per_quarter):
        self.revenue_growth = revenue_growth
        self.revenu_growth_per_quarter = revenu_growth_per_quarter
        self.earning_growth_rate = earning_growth_rate
        self.earning_growth_rate_per_quarter = earning_growth_rate_per_quarter

class Profitability:
    def __init__(self, net_profit_margin, return_on_assets, return_on_equity, operating_margin):
        self.net_profit_margin = net_profit_margin
        self.return_on_assets = return_on_assets
        self.return_on_equity = return_on_equity
        self.operating_margin = operating_margin

class Valuation:
    def __init__(self, price_to_book, price_to_earn, price_to_sales, ev_to_ebitda):
        self.price_to_book = price_to_book
        self.price_to_earn = price_to_earn
        self.price_to_sales = price_to_sales
        self.ev_to_ebitda = ev_to_ebitda
    
class Report:
    def __init__(self, company_infos: Company, growth: Growth, valuation: Valuation, profitability: Profitability):
        self.company_infos = company_infos
        self.growth = growth
        self.valuation = valuation
        self.profitability = profitability




def generate_company_report(company: Company) -> Report:
    valuation = Valuation(val.price_to_book(company), val.price_to_earn(company), val.price_to_sales(company), val.ev_to_ebitda(company))
    profitability = Profitability(profit.net_profit_margin(company), profit.return_on_assets(company), profit.return_on_equity(company), profit.operating_margin(company))
    growth = Growth(grth.revenue_growth(company), grth.revenu_growth_per_quarter(company), grth.earning_growth_rate(company), grth.earning_growth_rate_per_quarter(company))

    return Report(company, growth, valuation, profitability)
