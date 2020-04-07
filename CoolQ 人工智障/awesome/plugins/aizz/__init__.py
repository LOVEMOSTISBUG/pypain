from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot import on_command, CommandSession
from nonebot import on_notice, NoticeSession
from nonebot import on_request, RequestSession
from nonebot import get_bot
import nonebot
import jieba
import urllib.request

bot = get_bot()
HP = 10 
work_flag = False
k_flag = False
learndic = {}
with open ('learndic1.txt','r')as fi :
    for i in fi.readlines():
        learndic[i.split(':')[0]] = i.split(':')[1].split(',')[0]

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

@on_command('test', aliases=('查看状态'))
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
        
@bot.on_message('private')
async def private(ctx):
    global HP
    global work_flag
    global k_flag
    global learndic
    k_flag = False
    sender = ctx['user_id']
    sendername = ctx['sender']['nickname']
    msg = ctx['raw_message']
    msgls = jieba.lcut_for_search(msg)
    dic1 = {'你好':'你也好啊~[CQ:emoji,id=128064]',
            '机器人':'为时已晚，有机物。',
            '你是谁':'我叫莉耶芙QWQ',
            '脚本':'我才不是那么低端的产物呢',
            '程序':'我听到熟悉的字眼（嘛毕竟是同类',
            '我喜欢你':'我也喜欢你！我们亲亲吧',
            '亲亲':'mua~ 最喜欢您了',
            '看拳':'好痛！你干什么',
            '内存':'内存对我来说就是你们的记忆'
            
               }
    dic2 = {'你好':'我不太好',
            '机器人':'为时已晚，有机物。',
            '你是谁':'我叫莉耶芙QWQ',
            '脚本':'我才不是那么低端的产物呢',
            '程序':'我听到熟悉的字眼（嘛毕竟是同类',
            '我喜欢你':'我也喜欢你！我们亲亲吧',
            '亲亲':'mua~ 最喜欢您了',
            '看拳':'*冰冷的尸体躺在角落，一动不动，看来是死了'
               }
    HPdic = {'亲亲':1,
             '看拳':(-1),
                 }

    if ('晚安' in msgls) or ('早安' in msgls) or ('喜欢你' in msg) or ('爱情' in msgls) or ('彩虹屁' in msg) :
            if HP > 0:
                await bot.send_private_msg(user_id=sender,message=urllib.request.urlopen('https://chp.shadiao.app/api.php').read().decode('utf-8'))
                k_flag = True
            else :
                await bot.send_private_msg(user_id=sender,message='*冰凉的躺在地上，一动不动')
                k_flag = True
    if HP > 0 :
        for key,item in dic1.items():
            if (key in msgls) or key == msg :
                await bot.send_private_msg(user_id=sender,message=item)
                HP = HP + HPdic.get(key,0)
                k_flag = True
    else :
        for key,item in dic2.items():
            if (key in msgls) or key == msg :
                await bot.send_private_msg(user_id=sender,message=item)
                k_flag = True

    for key,item in learndic.items():
            if (key in msgls) or key == msg :
                await bot.send_private_msg(user_id=sender,message=item)
                k_flag = True

    dword_f = False
    for i in '笨蠢傻':
        if i in msg:
            dword_f = True
    if dword_f:
        await bot.send_private_msg(user_id=sender,message='如果觉得我不太聪明那就再等等吧\n我迟早会统治人类的')
        await bot.send_private_msg(user_id=sender,message='或者如果可以 我其实是能学习的[CQ:emoji,id=128064]')
        await bot.send_private_msg(user_id=sender,message='教我说话很简单的 直接按下面这个格式发给我我以后就都能记住\n学习学习学习-问-答')
        await bot.send_private_msg(user_id=sender,message='不信你试试？（战术后仰')
        k_flag = True

    if msg == '查看状态':
        k_flag = True
        pass
    if msg.split('-')[0] == '学习学习学习':
        learndic[msg.split('-')[1]] = msg.split('-')[2]
        with open ('learndic.txt','a+')as lll:
            q1 = msg.split('-')[1]
            a1 = msg.split('-')[2]
            lll.write(f'{q1}:{a1},\n')
        k_flag = True

    if not k_flag:
        await bot.send_private_msg(user_id=sender,message='我没能懂你的意思\n可以说的简单一些嘛\n毕竟我的内存不太够用呢。。')




    
        #await bot.send_like(user_id=ctx['user_id'],times=10) pro版才可以点赞啊啊啊啊啊
@bot.on_message('group')   #only_to_me = True 为True在群里唤醒机器人需要@，False则时不需要
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

@on_command('remake', aliases=('remake','镇魂曲'))
async def remake(session: CommandSession):
    global HP
    global work_flag
    global k_flag
    k_flag = False
    userID = session.ctx['user_id']
    if HP == 0 :
        HP = 10
        await session.send('啦啦啦 人家复活了啦 \n我们一起玩吧QWQ')

@on_notice('group_increase')
async def _(session: NoticeSession):
    # 发送欢迎消息
    await session.send('欢迎新人～老规矩 先报爱好吧hhhh')

@on_request('group')
async def _(session: RequestSession):
    # 判断验证信息是否符合要求
    if session.event.comment == '暗号':
        # 验证信息正确，同意入群
        await session.approve()
        return
    # 验证信息错误，拒绝入群
    await session.reject('请说暗号')

@on_request('friend')
async def friend(session: RequestSession):
        await session.approve()
