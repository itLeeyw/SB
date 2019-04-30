# 引入酷Q的包
# 引入pprint 跟print差不多 叫更好看的打印
# from pprint import  pprint
import re

import requests
from cqhttp import CQHttp

import random
import shlex
import tuling

# 设置酷Q的root-API 在哪里 并实例化给bot对象
bot = CQHttp(api_root='http://127.0.0.1:5700')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
}
commands = {}


def command(name):  # 命令装饰器
    def decorator(func):
        #注册命令到commands中
        commands[name] = func
        return func

    return decorator


@command('命令大全')
def cmdAll(ctx, arg):
    return {'reply': "command + space 使用命令" + "\n" \
                                              "命令大全\n" \
                                              "你好\n" \
                                              "计算\n" \
                                              "知乎日报\n" \
                                              "算法菜单(暂未开发)\n" \
                                              "h5菜单(暂未开发)\n" \
                                              "翻译(暂未开发)\n" \
                                              "专研\n"\
                                              "掷骰子\n" \
                                              "a\n\n" \
                                              "/*\n*a为沙雕bot在线聊天,后续功能正在开发\n*Gakki是李伟豪老婆\n*/"
            }


@command('你好')
def hello(ctx, arg):
    return {'reply': "哦"}


@command('专研')
def _(ctx,arg):
    argv = shlex.split(arg)
    if not argv:
        bot.send("谁是那个被选召的孩子")
    print(argv)
    bot.send(ctx,random.choice(argv) + "!")




@command('掷骰子')
def ztz(ctx, arg):
    return {'reply': " " + str(random.randint(1, 6)) + " 点"}


@command('计算')
def calculate(ctx, arg):
    try:
        c = re.compile(r'amp;')
        formula = re.sub(c, '', arg.strip())
        print(formula)
        # 逆波兰表示法(后缀表示法)
        return {'reply': "答案:" + str(eval(formula))}
    except:
        return {'reply': "亲亲这边见你您输入正常的表达式呢"}


@command('知乎日报')
def zhrb(ctx, arg):
    url = 'https://news-at.zhihu.com/api/4/news/latest'
    STORY_URL = 'http://daily.zhihu.com/story/{}'
    r = requests.get(url=url, headers=headers)
    data = r.json()
    stories = data.get('stories')
    if not stories:
        bot.send(ctx, "服务器爆炸了，你等哈子再专研")
        return
    else:
        rep = ''
        for story in stories:
            surl = STORY_URL.format(story['id'])
            title = story.get('title', "冒得内容")
            rep += f'\n{title}\n{surl}\n'
        bot.send(ctx, "今日知乎日报一览\n"+rep)


@command('算法菜单')
def algorithmList(ctx, arg):
    pass


@command('h5菜单')
def html5List(ctx, arg):
    pass


@command('翻译')
def Fanyi(ctx, arg):
    pass


# @bot.on_message('private')告诉bot说，这一个函数(handle_msg)是处理私聊消息的
@bot.on_message('group')
def handle_msg(ctx):
    # pprint(ctx)
    # ctx是一个字典序，获取到的是当前聊天操作的所有信息
    msg: str = ctx['message']
    sp = msg.split(maxsplit=1)
    if not msg:
        return
    cmd, *args = sp
    arg = ''.join(args)

    handle = commands.get(cmd)  # 通过cmd获取对应函数， get为获取字典的安全操作，不报错

    if not handle:
        if msg.startswith("a") or msg.startswith("lt"):
            replies = tuling.get_reply(msg[len("a"):])
            if replies:
                bot.send(ctx, replies[0])
    else:
        return handle(ctx, arg)


# 粗理解为网站后端在哪里127.0.0.1:8080（(QQ)客户端实际请求的地方）
bot.run('127.0.0.1', 8080)
