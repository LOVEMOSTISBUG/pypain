import urllib.request
import urllib.parse
import random
import os 
import re

def url_open(url):
    '''访问并返回html，设置代理ip，修改headers'''
    #手动代理ip没排面  啊对这里的几个ip有可能已经挂了
    iplist = ['121.237.149.146:3000','119.41.236.180:8010','59.110.26.1:8080']
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

def find_aim(url,k):
    '''输入url和正则表达式k得到目标url列表'''
    html = url_open(url).decode('utf-8')
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
    
url = 'http://www.budejie.com/pic/'
k = r'http://.+?.gif'
gif = find_aim(url,k)
for each in gif :
    each = each #是否需要加前缀https://啥的？
    print(each)
    
'''
os.mkdir('gaoxiao')
os.chdir('gaoxiao')
download_https(gif)
'''
''' tip 1
不用正则表达式的寻找方式
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    a = html.find('//image.hahamx')
    img_addrs = []
    while a != -1:
        b = html.find('.gif',a,a+255)
        if b != -1:
            img_addrs.append(html[a:b+4])
        else:
            b = a + 8
        a = html.find('//image.hahamx',b)
    return img_addrs
'''
'''tip2 
ip查询正则表达式        
k = r'((2[0-4]\d|25[0-5]|[0-1]{0,1}\d{0,1}\d)\.){3}(2[0-4]\d|25[0-5]|[0-1]{0,1}\d{0,1}\d)'
re.search(k,'121.237.149.146').span()  在字符串中查找出并返回下标
'''
