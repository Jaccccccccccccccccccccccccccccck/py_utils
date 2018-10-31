import hashlib,os

def str_md5(str_temp):
    m = hashlib.md5()
    m.update(str_temp.encode('utf8'))
    old_bundlekey = m.hexdigest()
    print(old_bundlekey)
path = '/'.join(['us', 'nyse', '2018', 'q0', 'i', 'yi'])
print(path)
str_md5(path)
str_md5('https://www.sec.gov/Archives/edgar/data/1742518/000121390018014224/ff12018_mmtecinc.htm')
# cn/hk/2018/q0/8/01758

#44cb95e31c9c7f71fa992155e0f21de4

