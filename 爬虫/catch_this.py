import urllib.request

url = input('把url交出来\n')

response = urllib.request.urlopen(url)

fo = input('要保存为什么名字？（ssln.jpg)\n')
catch = response.read()

with open ( fo,'wb') as file:
    file.write(catch)

