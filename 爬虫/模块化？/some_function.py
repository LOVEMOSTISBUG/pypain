import urllib.request
import urllib.parse
import random
import re

def url_open(url):
    '''访问并返回html，设置代理ip，修改headers'''
    my_headers = list(set(open('user_agent.txt','r').read().split('\n')))
    iplist = list(set(open('ip.txt','r').read().split('\n')))
    #读取更新的代理IP 随机ip地址
    my_ip = random.choice(iplist)
    my_head = random.choice(my_headers)
    print (my_ip+'\n'+my_head+'\n')
    iplist =list(set(open('ip.txt','r').read().split('\n')))
    proxy_support = urllib.request.ProxyHandler({'http':my_ip})
    opener = urllib.request.build_opener(proxy_support)
    #修改headers里的user-Agent 
    opener.addheaders = [('User-Agent',my_head)]
    urllib.request.install_opener(opener)
    #可以补充data在这里
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def gkdgkd(left,total,*tip):
    '''输入剩下的str长度和总str长度显示目前进度  tip字符串用来提示当前是在干什么'''
    print('{1} 目前进度：{0:%}'.format(1-left/total,tip[0]))

def get_ip(url):
    '''爬取目标url的代理IP'''
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
    for n in range(1,20):
        print("第"+str(n)+'次抓取ip\n')
        for each in get_ip('https://www.xicidaili.com/nn/'+str(n)):
            with open ('ip.txt','a+')as ipfile:
                ipfile.write(each+'\n')


def download(url_list):
    '''下载一个列表中的所有文件并命名'''
    for each in url_list:
        response = urllib.request.urlopen(each)
        catch = response.read()
        fo = each.split('/')[-1]
        with open ( fo,'wb') as file:
            file.write(catch)
            

if __name__ == '__main__':
    update_ip()


