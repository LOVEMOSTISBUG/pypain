from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot import on_command, CommandSession
from nonebot import on_notice, NoticeSession
from nonebot import on_request, RequestSession
from nonebot import get_bot
import jieba
import urllib.request
import pickle
from awesome.plugins.aizz.class_question import question
import awesome.plugins.aizz.some_function as sf 
from random import choice
from pathlib import Path

bot = get_bot()
HP = 10 
path = Path('data\\learn_dic')
work_flag = False
k_flag = False
learn_dic_ls = []
learn_dic = {}

#获得学习记忆列表
learn_dic_ls,learn_dic = sf.memory()

#载入基础词库
alive_base_dic = sf.pklmemory('data\\alive_base_dic.pkl')
dead_base_dic = sf.pklmemory('data\\dead_base_dic.pkl')
HP_dic =sf.pklmemory('data\\HP_dic.pkl')

@bot.on_message('private')  #处理私聊消息
async def private(ctx):
    global HP
    global work_flag
    global k_flag
    global learn_dic
    global alive_base_dic
    global dead_base_dic
    global HP_dic
    k_flag = False
    sender = ctx['user_id']
    sendername = ctx['sender']['nickname']
    msg = ctx['raw_message']
    msgls = jieba.lcut_for_search(msg)
    #整点api
    if ('我的ip地址' == msg) :
            await bot.send_private_msg(user_id=sender,message=urllib.request.urlopen('http://whois.pconline.com.cn/ip.jsp').read().decode('gbk'))
            k_flag = True
    if ('晚安' in msgls) or ('早安' in msgls) or ('喜欢你' in msg) or ('爱情' in msgls) or ('彩虹屁' in msg) :
            if HP > 0:
                await bot.send_private_msg(user_id=sender,message=urllib.request.urlopen('https://chp.shadiao.app/api.php').read().decode('utf-8'))
                k_flag = True
            else :
                await bot.send_private_msg(user_id=sender,message='*冰凉的躺在地上，一动不动')
                k_flag = True
    #alive和dead两个记忆 一对一回答 
    if HP > 0 :
        for key,item in alive_base_dic.items():
            if (key in msgls) or key == msg :
                await bot.send_private_msg(user_id=sender,message=item)
                HP = HP + int(HP_dic.get(key,0))
                k_flag = True
    else :
        for key,item in dead_base_dic.items():
            if (key in msgls) or key == msg :
                await bot.send_private_msg(user_id=sender,message=item)
                k_flag = True
    #学习记忆 一对多回答 随机回答一个
    for key,item in learn_dic.items():
            if (key in msgls) or key == msg :
                await bot.send_private_msg(user_id=sender,message=choice(item.get_answer()))
                k_flag = True
    #提示教学
    dword_f = False
    for i in '笨蠢傻':
        if i in msg:
            dword_f = True
    if dword_f:
        await bot.send_private_msg(user_id=sender,message='如果觉得我不太聪明那就再等等吧\n我迟早会统治人类的')
        await bot.send_private_msg(user_id=sender,message='或者如果可以 我其实是能学习的[CQ:emoji,id=128064]')
        await bot.send_private_msg(user_id=sender,message='教我说话很简单的 直接按下面这个格式发给我我以后就都能记住\nL-问-答')
        await bot.send_private_msg(user_id=sender,message='不信你试试？（战术后仰')
        k_flag = True

    if (msg == '查看状态') or  (msg == '对话转文本浏览')or  (msg == '在线更新记忆')or  (msg == '开启群聊功能')or  (msg == '关闭群聊功能')or  (msg == '目前学习进度'):
        k_flag = True
        pass

    #灵魂
    if msg.split('-')[0] == 'L':
        for qn,qa in learn_dic.items():
            if qa.question == msg.split('-')[1]:
                qa.save_answer(msg.split('-')[2])
                break
        else:
            if msg.split('-')[1] == 'L':
                await bot.send_private_msg(user_id=sender,message='你很坏，不过我不会介意。')
            else:
                learn_dic[msg.split('-')[1]] = question(msg.split('-')[1])
                learn_dic[msg.split('-')[1]].save_answer(msg.split('-')[2])
        txtname = 'data\\learn_dic\\' + msg.split('-')[1] + '.txt'
        with open (txtname,'a+')as lll:
            aaa = msg.split('-')[2]
            lll.write(f'{aaa}\n')
        k_flag = True
    #如果始终弄不清五分之四概率发出抱歉
    if not k_flag:
        k_random =[2,3,4,1,0]
        if choice(k_random) > 0:
            await bot.send_private_msg(user_id=sender,message='我没能懂你的意思\n可以说的简单一些嘛\n毕竟我的内存不太够用呢。。')

@on_command('up_data', aliases=('在线更新记忆'))  #在线更新data\learn目录下的学习记忆
async def up_data(session: CommandSession):
    global k_flag
    global learn_dic
    global learn_dic_ls
    k_flag = False
    learn_dic_ls,learn_dic = sf.memory()
    await session.send('更新完毕')

@on_command('howisitgoing', aliases=('目前学习进度'))  #输出学习记忆关键词
async def howisitgoing(session: CommandSession):
    global k_flag
    global learn_dic_ls
    k_flag = False
    learn_dic_num = len(learn_dic_ls)
    learn_dic_view_s = ''
    for n in learn_dic_ls:
        learn_dic_view_s += (n+'\n')
    await session.send(f'目前学习词条共{learn_dic_num}条，分别如下\n{learn_dic_view_s}')

@on_command('dictotxt', aliases=('内置对话转文本浏览'))  #把内置pkl字典的内容输出到data文件夹
async def dictotxt(session: CommandSession):
    global k_flag
    global alive_base_dic
    global dead_base_dic
    global HP_dic
    k_flag = False
    userID = session.ctx['user_id']
    if userID == 2212029828: 
        await session.send('主人大人，请检查我的初始记忆')
        dic_ls = [alive_base_dic,dead_base_dic,HP_dic,learn_dic_ls] 
        for k,y in dic_ls[0].items():
            foname = 'data\\alive_base_dic.txt'
            with open (foname,'a+')as fo:
                fo.write(f'{k}:{y},\n')
                
        for k,y in dic_ls[1].items():
            foname = 'data\\dead_base_dic.txt'
            with open (foname,'a+')as fo:
                fo.write(f'{k}:{y},\n')
                
        for k,y in dic_ls[2].items():
            foname = 'data\\HP_dic.txt'
            with open (foname,'a+')as fo:
                fo.write(f'{k}:{y},\n')

        for n in dic_ls[3]:
            foname = 'data\\learn_dic.txt'
            with open (foname,'a+')as fo:
                fo.write(f'{n}\n')

        await session.send('主人大人，输出完毕')

@on_command('on', aliases=('开启群聊功能'))
async def on(session: CommandSession):
    global work_flag
    global k_flag
    k_flag = False
    work_flag = True 
    await session.send('我去找新朋友啦')
    
@on_command('off', aliases=('关闭群聊功能'))
async def off(session: CommandSession):
    global work_flag
    global k_flag
    k_flag = False
    work_flag = False
    await session.send('好吧 那我们就在这玩吧')

@bot.on_message('group')   #处理群聊消息   only_to_me = True 为True在群里唤醒机器人需要@，False则时不需要
async def group(ctx):
    global HP
    global work_flag
    global k_flag
    k_flag = False
    groupID = ctx['group_id']
    msg = ctx['raw_message']
    msgls = jieba.lcut_for_search(msg)
    if work_flag:
        dword_f = False
        for i in '笨蠢傻':
            if i in msg:
                dword_f = True
        if dword_f:
            await bot.send_group_msg(group_id=groupID,message='人家只是一个小笨蛋而已啦\n就饶了人家吧QWQ')

@on_request('group')  #处理进群的申请
async def _(session: RequestSession):
    # 判断验证信息是否符合要求
    if session.event.comment == '暗号':
        # 验证信息正确，同意入群
        await session.approve()
        return
    # 验证信息错误，拒绝入群
    await session.reject('请说暗号')
 
@on_notice('group_increase')  #欢迎新成员
async def _(session: NoticeSession):

    await session.send('欢迎新人～老规矩 先报爱好吧hhhh')
    
@on_command('test', aliases=('查看状态'))  #发送当前HP 或者各类杂项
async def test(session: CommandSession):
    global HP
    global work_flag
    global k_flag
    k_flag = False
    selfID = session.self_id
    userID = session.ctx['user_id']
    sendtype = session.ctx['message_type']
    text = session.ctx['message'][0]['data']['text']
    username = session.ctx['sender']['nickname']
    response = f'目前HP:{HP}\n要好好对人家哦'
    if userID == 2212029828:
        await session.send('主人大人，您来啦')
        await session.send(response)
    elif work_flag:
        await session.send(response)

@on_command('remake', aliases=('remake','镇魂曲'))  # 复活的函数
async def remake(session: CommandSession):
    global HP
    global work_flag
    global k_flag
    k_flag = False
    userID = session.ctx['user_id']
    if HP == 0 :
        HP = 10
        await session.send('啦啦啦 人家复活了啦 \n我们一起玩吧QWQ')

@on_request('friend')  #处理好友申请
async def friend(session: RequestSession):
        await session.approve()

#await bot.send_like(user_id=ctx['user_id'],times=10) pro版才可以点赞啊啊啊啊啊
