from company import Company, Revenue
from company_loaders import load_companies
from reporter import Growth, Profitability, Report, Valuation, generate_company_report
import json



companies = load_companies()
amazon = companies[0]


global_report = generate_company_report(amazon)


def json_serializable(obj):
    if isinstance(obj, Report) or isinstance(obj, Company) or isinstance(obj, Growth) or isinstance(obj, Valuation) or isinstance(obj, Profitability) or isinstance(obj, Revenue):
        return obj.__dict__


file = open("result.json", "w")
json.dump(global_report,file, default=json_serializable, indent=4)
file.close()