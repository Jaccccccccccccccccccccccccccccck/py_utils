import requests
from bs4 import BeautifulSoup

res = requests.get(url = 'https://web.archive.org/web/*/www.iwencai.com')

bs = BeautifulSoup(res.text, 'lxml')

snapshots = bs.find_all

# months = bs.select('#month')
# for month in months:
#     month_name = month.select('#month-title')[0].text
#     for day in months.select('#month-body'):

