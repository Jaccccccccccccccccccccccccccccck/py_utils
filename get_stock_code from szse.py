import random,demjson,requests


def get_stock_code_from_szse_website(name):
    # http://www.szse.cn/szseWeb/FrontController.szse?randnum=0.3467027121503963
    randnum = str(random.random())
    url = 'http://www.szse.cn/szseWeb/FrontController.szse?randnum=%s' % randnum
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    form_data = {
        'ACTIONID': '51',
        'datatype': '[zqjsb]',
        'matchmode': '',
        'resultcount': '15',
        'TYPE_AHEAD_TXTVALUE': name,
        'TYPE_AHEAD_MATCHANYWHERE': 'true'
        # ACTIONID=51&datatype=[zqjsb]&matchmode=&resultcount=15&TYPE_AHEAD_TXTVALUE=富奥&TYPE_AHEAD_MATCHANYWHERE=true
    }
    return prase_stock_name(requests.post(url=url, headers=headers, data=form_data))


def prase_stock_name(response):
    resp_content = response.text
    print((resp_content))
    code_list = demjson.decode(resp_content).get('items')
    print(len(code_list))
    if 1 == len(code_list):
        stock_code = code_list[0].get('code')
        stock_id = stock_code + '.SZ'
        stock_name = code_list[0].get('name')


    return None



print(get_stock_code_from_szse_website('富奥'))