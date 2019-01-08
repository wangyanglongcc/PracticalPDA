# -*- coding: UTF-8 -*-
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
import datetime as dt
import mimetypes
import os
from getConfig import getConfig
config = getConfig # 实例化
smtpserver = getConfig.getsmtpserver(config.smtpserver)
port = getConfig.getport(config.port)
usermail = getConfig.getusermail(config.usermail)
password = getConfig.getpassword(config.password)
username = getConfig.getusername(config.username)
receivers = getConfig.getreceivers(config.receivers).split(',')
cc_list = getConfig.getreceivers(config.cc_list).split(',')


def mail_connect(smtpserver,port,usermail,username,password,receivers):
    smtp = smtplib.SMTP(smtpserver,int(port))
    smtp.login(usermail, password)
    msg = EmailMessage()
    msg['From'] = Address(username)
    msg['To'] = receivers
    msg['cc'] = cc_list
    print(set(cc_list) | set(receivers))
    return smtp,msg
def mail_content(subject,content,attachments = None):
    try:
        smtp,msg = mail_connect(smtpserver,port,usermail,username,password,receivers)
        print('connect successful!')
    except Exception as e:
        print('connect failed!')
        print(e)
    try:
        msg['Subject'] = subject
        msg.add_alternative(content, subtype='html')
        if attachments is None:
            smtp.send_message(msg, usermail, receivers)
            smtp.quit()
            print('The mail was sent without attachment!')
        else:
            for filename in attachments:
                ctype,encoding = mimetypes.guess_type(filename)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype,subtype = ctype.split('/',1)
                with open(filename,'rb') as f:
                    msg.add_attachment(f.read(),maintype=maintype,subtype=subtype,filename=filename.split('/')[-1])
            smtp.send_message(msg,usermail,receivers)
            smtp.quit()
            print('The mail was sent with attachment!')
    except Exception as e:
        print('The mail could not send,Please take a chect!')
        print(e)
if __name__ == '__main__':
    subject = '{}年{}月{}日 - 日报'.format(dt.datetime.today().year, dt.datetime.today().month, dt.datetime.today().day)
    file = os.path.join(os.getcwd(),'content.html')
    f = open(file, 'r+', encoding='utf-8')
    content = f.readlines()
    content = ''.join(content)
    content = content.replace('以下是2018年11月19日的日报情况，请查收。','以下是{}年{}月{}日的日报情况，请查收。'.format(dt.datetime.today().year, dt.datetime.today().month, dt.datetime.today().day))
    f.close()
    mail_content(subject,content,attachments=None)
