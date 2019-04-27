# 引入酷Q的包
from cqhttp import CQHttp
#引入pprint 跟print差不多 叫更好看的打印
from pprint import  pprint

#设置酷Q的root-API 在哪里 并实例化给bot对象
bot = CQHttp(api_root='http://127.0.0.1:5700')


#@bot.on_message('private')告诉bot说，这一个函数(handle_msg)是处理私聊消息的
@bot.on_message('private')
def handle_msg(ctx):
    #ctx是一个字典序，获取到的是当前聊天操作的所有信息
    msg = ctx['message']
    echo_cmd = '你好'
    if msg.startswith(echo_cmd):
        bot.send(ctx, msg[len(echo_cmd):].lstrip())

#粗理解为网站后端在哪里127.0.0.1:8080（(QQ)客户端实际请求的地方）
bot.run('127.0.0.1',8080)