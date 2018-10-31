import json

json_file = open('C:/temp/ir_earning.json')

ir_earnings = json.load(json_file)
stocks = set()
for ir_earning in ir_earnings:
    stocks.add(ir_earning['stock_code'])

print(f'stock_count:{len(stocks)}')
print(str(stocks))