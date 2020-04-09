from pathlib import Path
from awesome.plugins.aizz.class_question import question
import pickle

def memory():
    '''返回记忆的关键词列表&储存以关键词为key 问题类为value的字典'''
    path = Path('data\\learn_dic')
    learn_dic_ls = []
    learn_dic = {}
    for n in path.glob('*.txt'):
        qtn = str(n).split('\\')[-1].replace('.txt','')
        learn_dic_ls.append(qtn)
        with open(str(n),'r')as fia :
            learn_dic[qtn] = question(qtn)
            for fiaa in fia.readlines():
                learn_dic[qtn].save_answer(fiaa)
    return learn_dic_ls,learn_dic

def pklmemory(pklpath):
    '''打开pkl文件仅此而已'''
    pklfo = pickle.load(open(pklpath,'rb'))
    return pklfo