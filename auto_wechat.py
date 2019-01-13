from wxpy import *
import requests
from threading import Timer
import datetime as dt
import time

def get_msg():
    url = 'http://open.iciba.com/dsapi'
    wb_data = requests.get(url)
    cn_content = wb_data.json()['content']
    en_content = wb_data.json()['note']
    return cn_content,en_content

def send_msg(content):
    # bot = Bot(cache_path=True)
    try:
        my_friend = bot.friends().search('XXX')[0]# 对方的昵称名，对方自己起的昵称
        my_friend.send(content)
        # t = Timer(86400,send_msg)
        # t.start()
    except:
        bot.self.send('消息发送失败')

if __name__ == '__main__':
    while True:
        if dt.datetime.now().minute == 39 and dt.datetime.now().second == 0:
            time.sleep(3)
            content = '现在是{}年{}月{}日{}时{}分'.format(dt.datetime.now().year,dt.datetime.now().month,dt.datetime.now().day,dt.datetime.now().hour,dt.datetime.now().minute)
            cn_content, en_content = get_msg()
            content = '\n'.join([content,cn_content, en_content, '-- 来自自动发送的问候'])
            send_msg(content)