#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import getData

import json

rawData = getData.getData('http://api.openweathermap.org/data/2.5/weather?APPID=06dc04f1d54e930bdc3d4372d7291dd1','Chicago')
strData = str(rawData, encoding='utf-8')
dictData = json.loads(strData)

mail_host="smtp.gmail.com"  #设置服务器
mail_user="tlmorphing@gmail.com"    #用户名
mail_pass="morphing"   #口令

sender = 'tlmorphing@gmail.com'
receivers = ['tlmorphing@gmail.com', 'yzhou108@hawk.iit.edu']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# body = getData.getfile('content.html')
temMin = round(dictData['main']['temp_min']-273.15,1)
temMax = round(dictData['main']['temp_max']-273.15,1)
# body = '<h1>早上好,芝加哥的朋友<h1>'


# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('早上好,芝加哥的朋友\n'+'今天最低气温 : ' + str(temMin) + '°C' + ' 最高气温 : ' + str(temMax) + '°C\n' + '好冷啊', 'plain', 'utf-8')
message['From'] = Header("力量的花生", 'utf-8')
message['To'] = Header("渺小的凡人", 'utf-8')

subject = '又是新的一天'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("Successful")
except smtplib.SMTPException:
    print("Error")

