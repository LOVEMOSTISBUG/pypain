import urllib.request
import urllib.parse
import random
import os 
import re

def url_open(url):
    '''访问并返回html，设置代理ip，修改headers'''
    #手动代理ip没排面  
    #iplist =['101.132.118.170:8080','121.237.148.198:3000','121.237.148.62:3000']
    iplist =[]
    for line in open ('ip.txt','r'):
        iplist.append(line.strip('\n'))
    iplist = list(set(iplist))
    #随机ip地址
    proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
    opener = urllib.request.build_opener(proxy_support)
    #修改user-Agent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')]
    urllib.request.install_opener(opener)
    #可以补充data和headers在这里
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def download(url_list):
    '''下载一个列表中的所有文件并命名为url最后15个字符'''
    for each in url_list:
        response = urllib.request.urlopen(each)
        catch = response.read()
        fo = each[-15:]
        with open ( fo,'wb') as file:
            file.write(catch)

def find_aim(url,k,iplist):
    '''输入url和正则表达式k得到目标列表'''
    html = url_open(url,iplist).decode('utf-8')
    aim_list = []
    ohtml = html
    total = len(ohtml)
    while re.search(k,html) != None:
        a,b = re.search(k,html).span()
        aim_list.append(html[a:b])
        left = len(html.split(html[a:b])[1])
        gkdgkd(left,total,'扫描网页')
        html = html.split(html[a:b])[1]
        if re.search(k,html) != None:
            (a,b) = re.search(k,html).span()
        else:
            break
    
    return aim_list  

def gkdgkd(left,total,*tip):
    '''输入剩下的str长度和总str长度显示目前进度  tip字符串用来提示当前是在干什么'''
    print('{1} 目前进度：{0:%}'.format(1-left/total,tip[0]))

def get_ip(url):
    '''爬取代理IP'''
    k = r'((2[0-4]\d|25[0-5]|[0-1]{0,1}\d{0,1}\d)\.){3}(2[0-4]\d|25[0-5]|[0-1]{0,1}\d{0,1}\d)'
    html = url_open(url).decode('utf-8')
    aim_list = []
    ohtml = html
    total = len(ohtml)
    while re.search(k,html) != None:
        aim = []
        a,b = re.search(k,html).span()
        aim.append(html[a:b])
        c = b - a
        duankou = html[a+31-15+c:b+25].split('<')[0]
        aim.append(duankou)
        left = len(html.split(html[a:b])[1])
        gkdgkd(left,total,'扫描网页')
        html = html.split(html[a:b])[1]
        
        a,b = re.search(r'<td>HTTPS</td>|<td>HTTP</td>',html).span()
        aim.append(html[a+4:b-5])
     
        aim_list.append(aim)
        if re.search(k,html) != None:
            continue
        else:
            break
    iplist = []
    for each in aim_list:
        iplist.append(each[0] +':' + each[1])
    return iplist
def update_ip():
    '''更新目录下ip.txt'''
    for each in get_ip('https://www.xicidaili.com/nn/1'):
        with open ('ip.txt','a+')as ipfile:
            ipfile.write(each+'\n')

update_ip()





