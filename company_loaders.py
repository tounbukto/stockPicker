from company import Company
from company import Revenue

# dummy data
def load_company() -> Company:
    amazon_revenue = Revenue(q1=127.36e9, q2=134.38e9, q3=143.08e9, q4=149.20e9)  # Values in billions of USD
    amazon_last_revenue = Revenue(q1=116.44e9, q2=121.23e9, q3=127.10e9, q4=137.41e9)  # Last year's quarters

    amazon_net_income = Revenue(q1=3.17e9, q2=6.75e9, q3=9.88e9, q4=14.14e9)  # Values in billions of USD
    amazon_last_net_income = Revenue(q1=8.11e9, q2=7.78e9, q3=2.87e9, q4=14.32e9)


    amazon = Company(
        name="amazon", 
        stock_price=140.0,  # Example stock price in USD
        number_of_shares=10.23e9,  # Outstanding shares in billions
        assets=468.4e9,  # Total assets in billions of USD
        equity=118.1e9,  # Shareholders' equity in billions of USD
        cash=64.4e9,  # Cash and cash equivalents in billions of USD
        debt=164.7e9,  # Total debt in billions of USD
        revenue=amazon_revenue,
        last_revenu=amazon_last_revenue,
        EBITDA=58.56e9,  # EBITDA in billions of USD
        net_income=amazon_net_income,
        last_net_income=amazon_last_net_income
    )
    return amazon

def load_companies() -> list[Company]:
    return [load_company()]

