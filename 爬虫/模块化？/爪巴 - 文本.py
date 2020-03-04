import urllib.request
import urllib.parse
import random
import os 
import re
import some_function as sf

#ip更新
sf.update_ip() 

url = 'https://www.vodtw.com/Html/Book/64/64777/'

k_contents = re.compile(r'href="((?:.).*?\.html)(?:.).*?">(第(?:.).*?)</a>')
k_txt = re.compile(r'nbsp;&nbsp;((?:.).*?)<br>')

html = sf.url_open(url).decode('gbk')
contents = re.findall(k_contents,html)

for i in contents:
    txt_url = url+i[0]
    txt_html = sf.url_open(txt_url).decode('gbk')
    with open('小说.txt','a+')as fo:
        fo.write(i[1]+'\n')
        print(i[1]+'\n')
        for n in re.findall(k_txt,txt_html):
            fo.write(n)
            fo.write('\n')

