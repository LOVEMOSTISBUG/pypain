def rushrushrush() :
    print ('well,here we do this\n')
    keepon=True
    while keepon :
        new_key=input('What is new key ?\n')
        new_value=input('What is new value?\n')
        file = 'dic.txt'
        with open (file,'a') as file_object:
            file_object.write("'"+new_key+"'"+":"+"'"+new_value+"',\n")
        repeat=input('keep on ? (type no to quit)\n')
        if repeat == 'no':
            keepon= False
    print ('******make is over******\n')
        
def view():
    file = 'dic.txt'
    for line in open(file):
        print(line)
    print ('******above is all******\n')

import pickle
print ('No more word ,let us work.\nMake a dict or view existing dict ?\nExit is just exit.\nm or v')
switch = True                                           
while switch:    
    answer = input()
    if ('m' in answer) or ('M' in answer) :
        rushrushrush()
    elif ('v' in answer) or ('V' in answer) :
        view()
    elif ('e' in answer) or ('E' in answer) :
        switch = False
    
