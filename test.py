# encoding=utf8 
import sys

reload(sys) 
sys.setdefaultencoding('utf8')


# #获取好友列表

# memberList = itchat.get_friends()
# fopen = open('namelist.txt', 'w')
# for item in memberList:
#     # import pdb; pdb.set_trace()
#     username = item['UserName']
#     itchat.get_head_img(userName=username,picDir='/Users/chenliang/Coding/mysite/resource/%s.png'%item['Alias'])
#     fopen.write('=============')
#     fopen.write('\n')
#     fopen.write("City:%s"%item['City'])
#     fopen.write('\n')
#     fopen.write('Province:%s'%item['Province'])
#     fopen.write('\n')
#     fopen.write(u'微信号:%s'%item['Alias'])
#     fopen.write('\n')
#     fopen.write('NickName:%s'%item['NickName'])
#     fopen.write('\n')
#     fopen.write('HeadImgUrl:%s'%item['HeadImgUrl'])
#     fopen.write('\n')
#     fopen.write('Sex:%s'%item['Sex'])
#     fopen.write('\n')
# fopen.close()



#coding=utf8
import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    import pdb; pdb.set_trace()
    msg['Text']('/Users/chenliang/Coding/mysite/resource/%s'%msg['FileName'])
    return '@%s@/Users/chenliang/Coding/mysite/resource/%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print msg['isAt']
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

itchat.auto_login(True)
itchat.auto_login(hotReload=True)
itchat.run()
# username = memberList[0]['UserName']
# print username
# itchat.get_head_img(userName=username,picDir='/Users/chenliang/Coding/mysite/resource/1.png')

itchat.send('Hello world!')