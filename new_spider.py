import requests
from lxml import etree

def get_url():
    url = 'https://news.sina.com.cn/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    res = requests.get(url=url,headers=headers,verify=False)
    res.encoding='utf-8'
    text = res.text
    # print(text)
    html = etree.HTML(text)
    links = html.xpath('//*[@id="blk_gjxw_011"]/li')
    for link in links:
        new_url=link.xpath('./a/@href')[0]
        print(new_url)
        print(1111)
        res1 = requests.get(url=new_url,headers=headers,verify=False)
        res1.encoding='utf-8'
        text1=res1.text
        # print(text1)
        # input()
        html1=etree.HTML(text1)
        title= html1.xpath('.//title')[0]
        title=title.text
        print(title)

        time=html1.xpath('//*[@id="top_bar"]/div/div[2]/span')[0]
        time=time.text
        print(time)
        source = html1.xpath('//*[@id="top_bar"]/div/div[2]/a')[0]
        source=source.text
        print(source)
        texts=html1.xpath('//*[@id="article"]/p')
        for text1 in texts:
            text= text1.text
            print(text)

        input()


get_url()

