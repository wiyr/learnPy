import re
import requests
import sys
reload(sys)

url = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=' \
      'r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=145846' \
      '1209860_R&pv=&ic=0&nc=1&z=&se=1&showtab=0' \
      '&fb=0&width=&height=&face=0&istype=2&i' \
      'e=utf-8&word=%E9%BB%91%E5%AD%90%E7%9A%84%E7%AF%AE%E7%90%83'


header={'''User-Agent:Mozilla/5.0
(Windows NT 6.1) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'''}
html = requests.get(url)

picUrl = re.findall('objURL":"(.*?)", ', html.text, re.S)
i = 0
for each in picUrl:
    print 'downloading:' + each
    pic = requests.get(each)
    fp = open('pic\\' + str(i) + '.' + each.split('.')[-1], 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1
