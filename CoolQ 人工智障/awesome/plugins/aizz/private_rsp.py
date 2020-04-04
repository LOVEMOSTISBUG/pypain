import jieba

def private_rsp(msg):
    msgls = jieba.lcut(msg)
    return 'nmsl'

if __name__ == '__main__':
    pass


