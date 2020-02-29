import urllib.request
import urllib.parse
import random
import os 
import re
import ipipip #本目录下用来处理代理ip事项

def url_open(url):
    '''访问并返回html，设置代理ip，修改headers'''
    #读取更新的代理IP
    iplist =list(set(open('ip.txt','r').read().split('\n')))
    #随机ip地址
    proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
    opener = urllib.request.build_opener(proxy_support)
    #修改headers里的user-Agent 可以继续补充
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')]
    urllib.request.install_opener(opener)
    #可以补充data在这里
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def download(url_list):
    '''下载一个列表中的所有文件并命名'''
    for each in url_list:
        response = urllib.request.urlopen(each)
        catch = response.read()
        fo = each.split('/')[-1]
        with open ( fo,'wb') as file:
            file.write(catch)

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

def gkdgkd(left,total,*tip):
    '''输入剩下的str长度和总str长度显示目前进度  tip字符串用来提示当前是在干什么'''
    print('{1} 目前进度：{0:%}'.format(1-left/total,tip[0]))

#ip更新
#ipipip.update_ip() 

url = 'https://www.bilibili.com/'
jpg = re.compile(r'http:(?:.).*?\.jpg')

html = url_open(url).decode('utf-8')

jp = re.findall(jpg,html)
for i in jp:
    print(i)
print('***********************************************************')
print('***********************************************************')
print('***********************************************************')


jp2 = find_aim(url,jpg)
for i in jp2:
    print(i)


