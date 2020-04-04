from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot import on_command, CommandSession
from nonebot import on_notice, NoticeSession
from nonebot import get_bot
import nonebot
import jieba

bot = get_bot()

@on_command('test', aliases=('测试'),only_to_me=False)
async def test(session: CommandSession):
    selfID = session.self_id
    userID = session.ctx['user_id']
    sendtype = session.ctx['message_type']
    text = session.ctx['message'][0]['data']['text']
    response = f'{selfID}\n{userID}\n{sendtype}\n{text}'
    if userID == 2212029828:
        await session.send('主人大人，您来啦')
    await session.send(response)
        
@on_command('rbq', aliases=('爬', '速爬'),only_to_me=False)
async def rbq(session: CommandSession):
    userID = session.ctx['user_id']
    if userID == 2212029828:
        await session.send('主人大人,我这就爬')
    username = session.ctx['sender']['nickname']
    await session.send('人家这就爬')
    #sextext = f'{username}君 咕噜咕噜'
    #await session.send(sextext)

@bot.on_message('private')
async def private(ctx):
    sender = ctx['user_id']
    msg = ctx['raw_message']

    #检测是否有暗示词汇 并反应
    msgls = jieba.lcut(msg)
    for i in  msgls:
        if i == '色图'  :
            await bot.send_private_msg(user_id=sender,message='hentai!')
        if i == '笑话':
            await bot.send_private_msg(user_id=sender,message='从前有个人叫王七，生了个儿子叫王八')

    #检测是否有侮辱性词汇 并反应
    dword_f = False
    for i in '笨蠢傻':
        if i in msg:
            dword_f = True
    if dword_f:
        await bot.send_private_msg(user_id=sender,message='人家只是一个小笨蛋而已啦\n就饶了人家吧QWQ')



@bot.on_message('group')
async def group(ctx):
    groupID = ctx['group_id']
    if groupID == 796528952:
        pass
