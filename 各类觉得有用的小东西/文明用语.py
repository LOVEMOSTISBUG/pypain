talk = input('say something\n')
output = ''
talk1 = talk
dirty = ['你妈','他妈的','傻逼','脑瘫','神经病']

for i in dirty:
    talk1 = talk1.replace(i,'*')
if talk != talk1:
    print('请文明发言，傻逼')

print (talk1)

