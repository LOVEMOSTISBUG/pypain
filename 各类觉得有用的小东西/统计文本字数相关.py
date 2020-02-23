import jieba

#打开文件提取全文并关闭
with open ('命运.txt','r') as file:
    txt = file.read()
#去除符号
for n in '，。：；‘’\n"~`!?？！*,.、《》' :
    txt = txt.replace(n,'')

d = {}
wordd = {}
danls = []
#全文字符单字转换为单字列表
for dan in txt:
    danls.append(dan)
#单字列表去除重复元素 
danls2 = list(set(danls))
#用已去除重复元素列表和单字列表统计成一个 字 —— 数量 字典
for dan in danls2:
    d[dan] = danls.count(dan)
#字典转换二维列表
danls3 = list(d.items())
#二维列表排序
danls3.sort(key = lambda x:x[1],reverse = True)

for dange in danls3:
    print (f'{dange[0]:*^10}:{dange[1]}')
    if danls3.index(dange) == 30 :
        break
#切割文章为词句列表
wordls = jieba.lcut(txt)

#字典统计词句数量并转化字典为二维数组排序
for word in wordls:
    wordd[word] = wordd.get(word,0) + 1
word_ls = list(wordd.items())
word_ls.sort(key = lambda x:x[1] ,reverse = True)

for Word in word_ls:
    print('{}:{}'.format(Word[0],Word[1]))
    if word_ls.index(Word) == 29 :
        break

    
  #  position = file2.tell()
  #  print(str(position))
   # print(type(position))                消除最后的逗号啥的
  #  file2.seek(position - 1)
  #  file2.write(' ')
