from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot import on_command, CommandSession
from nonebot import on_notice, NoticeSession
from nonebot import get_bot
import nonebot
import jieba
import urllib.request

bot = get_bot()
HP = 10 
work_flag = False
k_flag = True

@on_command('on', aliases=('开启群聊功能'),only_to_me=False)
async def on(session: CommandSession):
    global work_flag
    global k_flag
    k_flag = False
    work_flag = True 
    await session.send('我去找新朋友啦')
    
@on_command('off', aliases=('关闭群聊功能'),only_to_me=False)
async def off(session: CommandSession):
    global work_flag
    global k_flag
    k_flag = False
    work_flag = False
    await session.send('好吧 那我们就在这玩吧')

@on_command('test', aliases=('查看状态'),only_to_me=False)
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
    sender = ctx['user_id']
    sendername = ctx['sender']['nickname']
    msg = ctx['raw_message']
    k_flag = True
    msgls = jieba.lcut_for_search(msg)

    if ('晚安' in msgls) or ('早安' in msgls) or ('喜欢你' in msg) or ('爱情' in msgls) or ('彩虹屁' in msg) :
            if HP > 0:
                await bot.send_private_msg(user_id=sender,message=urllib.request.urlopen('https://chp.shadiao.app/api.php').read().decode('utf-8'))
                k_flag = False
            else :
                await bot.send_private_msg(user_id=sender,message='*冰凉的躺在地上，一动不动')
                k_flag = False
    if ('机器人' in msgls) or ('脚本' in msgls ):
        await bot.send_private_msg(user_id=sender,message='为时已晚，有机物。')
        k_flag = False

    if ('你是谁' in msgls) or ('你的名字' in msgls ):
        await bot.send_private_msg(user_id=sender,message='我叫莉耶芙QWQ')
        k_flag = False

    if ('我喜欢你'in msgls) or msg == '我喜欢你'  :
        if HP > 0:
            await bot.send_private_msg(user_id=sender,message=f'我也喜欢{sendername}君！我们亲亲吧~')
            k_flag = False
        else :
            await bot.send_private_msg(user_id=sender,message='*冰凉的尸体缩在角落，一言不发')
            k_flag = False

    if ('看拳'in msgls) or ('飞踹'in msgls)or ('欧拉'in msgls) or ('木大'in msgls):
        if HP > 0:
            HP = HP - 1
            await bot.send_private_msg(user_id=sender,message=f'好痛！{sendername}君你干什么 ')
            k_flag = False
        else :
            await bot.send_private_msg(user_id=sender,message='*在角落一动不动 看来是死了')
            k_flag = False

    if '亲亲'in msgls:
        if HP > 0:
            HP = HP + 1
            await bot.send_private_msg(user_id=sender,message=f'mua~ 最喜欢{sendername}酱了')
            k_flag = False
        else :
            await bot.send_private_msg(user_id=sender,message=f'*可惜我不是睡美人啊{sendername}君')
            k_flag = False

    dword_f = False
    for i in '笨蠢傻':
        if i in msg:
            dword_f = True
    if dword_f:
        await bot.send_private_msg(user_id=sender,message='如果觉得我不太聪明那就再等等吧\n我迟早会统治人类的')
        k_flag = False

    if msg == '查看状态':
        k_flag = False

    if  k_flag :
        await bot.send_private_msg(user_id=sender,message='我没能懂你的意思\n可以说的简单一些嘛\n毕竟我的内存不太够用呢。。')

@bot.on_message('group')
async def group(ctx):
    global HP
    global work_flag
    groupID = ctx['group_id']
    msg = ctx['raw_message']
    msgls = jieba.lcut_for_search(msg)
    if work_flag:
        if i == '亲亲':
            if HP > 0:
                HP = HP + 1
                await bot.send_group_msg(group_id=groupID,message='mua~ ')
            else :
                await bot.send_group_msg(group_id=groupID,message='*可惜我不是睡美人啊')

        dword_f = False
        for i in '笨蠢傻':
            if i in msg:
                dword_f = True
        if dword_f:
            await bot.send_group_msg(group_id=groupID,message='人家只是一个小笨蛋而已啦\n就饶了人家吧QWQ')



@on_command('remake', aliases=('remake','镇魂曲'),only_to_me=False)
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
