import re

re_stock_code = re.compile(r"(.*)首次.*")

title = '天风证券次公开发行股票招股意向书附录'

if re_stock_code.match(title):
    company_name = re_stock_code.search(title).group(1).strip()
    print(company_name)