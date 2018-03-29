# encoding=utf-8
__author__ = 'SR'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.MIMEBase import MIMEBase
from email import Encoders
import mimetypes
import email
import os


class MySendEmail(object):
    ''' 可以添加附件的邮件发送类 '''

    def __init__(self, smtpserver, sender, receiver, username, password, subject, main_body, attachmentList):
        self.smtpserver = smtpserver
        self.sender = sender
        self.receiver = receiver
        self.username = username
        self.password = password
        self.subject = subject
        self.main_body = main_body
        # 要发送附件的列表对象
        self.attachmentList = attachmentList

    # 使用mail.cofco.com服务器发送邮件（默认发邮件服务器）
    def sendEmail(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject  # 添加邮件主题
        msg['From'] = self.sender
        msg['To'] = ';'.join(self.receiver)

        # 设置邮件正文
        mainBody = MIMEText(self.main_body, 'plain', _charset='utf-8')
        # 将正文内容添加到邮件内容中
        msg.attach(mainBody)

        # 构造附件
        for idx, i in enumerate(self.attachmentList):
            att = MIMEText(open(i, 'rb').read(), 'base64', 'gbk')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"' % os.path.basename(i).encode("gbk")
            msg.attach(att)

        # 发送
        try:
            smtp = smtplib.SMTP_SSL()
            smtp.connect(self.smtpserver, 465)
            smtp.set_debuglevel(1)
            smtp.login(self.username, self.password)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
            smtp.quit()
        except Exception, e:
            print e
            return False
        else:
            return True


if __name__ == '__main__':
    sender = '835005338@qq.com'  # 发送者

    # 接受者，支持多人发送，以列表形式存储多人邮箱地址
    receiver = ['835005338@qq.com']
    smtpserver = 'smtp.qq.com'  # 发送邮件的服务器地址
    username = '835005338'  # 发送者用户名
    # password = 'zhang8355563!'  # 发送邮箱密码,QQ授权三方登录的授权码
    password = 'nzsrifdltvgkbbfc'
    subject = u"自动发送邮件"  # 邮件主题
    main_body = "这是一封邮件测试"  # 邮件正文内容
    attachmentList = [u"/Users/zhangbingwei/Downloads/ZZZ.txt",]

    my_send_email = MySendEmail(smtpserver, sender, receiver, username, password, subject, main_body, attachmentList)
    flag = my_send_email.sendEmail()
    if flag:
      print u"邮件发送成功"
