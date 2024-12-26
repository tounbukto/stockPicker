from company import Company 

# P/B
def book_value_per_share(company: Company) -> float:
    return company.equity / company.number_of_shares

def price_to_book(company: Company) -> float:
    return company.stock_price / book_value_per_share(company)


# P/E
def earning_per_share(company: Company) -> float:
    return company.net_income.total() / company.number_of_shares

def price_to_earn(company: Company) -> float:
    return company.stock_price / earning_per_share(company)

# P/S
def revenue_per_share(company: Company) -> float:
    return company.revenue.total() / company.number_of_shares

def price_to_sales(company: Company) -> float:
    return company.stock_price / revenue_per_share(company)

# EV/EBITDA
def ev_to_ebitda(company: Company) -> float:
    return company.entreprise_value() / company.EBITDA