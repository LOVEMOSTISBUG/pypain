import urllib.request
import urllib.parse
import random
import os 
import re
import some_function as sf

def find_aim(url,k):
    '''输入url和正则表达式k得到目标一维列表'''
    html = url_open(url).decode('utf-8')
    aim_list = []
    ohtml = html
    total = len(ohtml)
    while re.search(k,html) != None:
        a,b = re.search(k,html).span()
        aim_list.append(html[a:b])
        left = len(html.split(html[a:b])[1])
        gkdgkd(left,total,'爬啊爬')
        html = html.split(html[a:b])[1]
        if re.search(k,html) != None:
            continue
        else:
            break
    
    return aim_list  

#ip更新
#sf.update_ip() 

url = ''
jpg = re.compile(r'http:(?:.).*?\.jpg')

html = sf.url_open(url).decode('utf-8')
print(html)
jp = re.findall(jpg,html)
print(jp)

