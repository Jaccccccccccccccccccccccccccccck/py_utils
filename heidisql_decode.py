# -*- coding: utf-8 -*-
"""
2017-1-21 3:42:54 codegay
"""
import re
settings = r"C:\Users\jack\Desktop\123.txt"

with open(settings,encoding="utf8") as f:
    lines = [r.strip() for r in f.readlines() if "\\Password<" in r]
passwords = [re.split("\<\|\|\|\>",r)[-1] for r in lines]

def heidipass(code):
    ascii = code[:-1]
    d = int(code [-1])
    decode = lambda x:chr(int(x,16) - d)
    password = ''.join(map(decode,re.findall("\w{2}",ascii)))
    return password

for r in passwords:
    print(heidipass(r))