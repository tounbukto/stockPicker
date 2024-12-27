from company import Company

def growth(current_value, last_value) -> float:
    return 100 * (current_value - last_value) / last_value

def earning_growth_rate(company: Company) -> float:
    return growth(company.current_net_income.total(), company.last_net_income.total())

def earning_growth_rate_per_quarter(company: Company) -> list[float]:
    return [
        growth(company.current_net_income.q1, company.last_net_income.q1),
        growth(company.current_net_income.q2, company.last_net_income.q2),
        growth(company.current_net_income.q3, company.last_net_income.q3),
        growth(company.current_net_income.q4, company.last_net_income.q4)
    ]

def revenue_growth(company: Company) -> float:
    return growth(company.revenue.total(), company.last_revenu.total())

def revenu_growth_per_quarter(company: Company) -> list[float]:
    return [
        growth(company.revenue.q1, company.last_revenu.q1),
        growth(company.revenue.q2, company.last_revenu.q2),
        growth(company.revenue.q3, company.last_revenu.q3),
        growth(company.revenue.q4, company.last_revenu.q4)
    ]