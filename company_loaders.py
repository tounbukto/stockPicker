from company import Company
from company import Revenue

# dummy data
def load_company() -> Company:
    amazon_revenue = Revenue(q1=157.72e9, q2=177.90e9, q3=188.47e9, q4=199.12e9)  # Values in billions of USD
    amazon_last_revenue = Revenue(q1=147.44e9, q2=157.30e9, q3=167.20e9, q4=178.00e9)  # Last year's quarters

    amazon_net_income = Revenue(q1=6.31e9, q2=8.72e9, q3=12.47e9, q4=16.54e9)  # Values in billions of USD
    amazon_last_net_income = Revenue(q1=5.61e9, q2=6.89e9, q3=8.15e9, q4=10.79e9)  # Last year's quarters



    amazon = Company(
        name="amazon", 
        stock_price=229.05,  # Example stock price in USD
        number_of_shares=10.42e9,  # Outstanding shares in billions
        assets=620.1e9,  # Total assets in billions of USD
        equity=49.8e9,  # Shareholders' equity in billions of USD
        cash=32.2e9,  # Cash and cash equivalents in billions of USD
        debt=154.7e9,  # Total debt in billions of USD
        revenue=amazon_revenue,
        last_revenu=amazon_last_revenue,
        EBITDA=111.56e9,  # EBITDA in billions of USD
        current_net_income=amazon_net_income,
        last_net_income=amazon_last_net_income
    )
    return amazon

def load_companies() -> list[Company]:
    return [load_company()]

