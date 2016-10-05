#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import random
import json

import getData
import dota

account = [201956451, 247810685, 132130668]

rawData = getData.getData('http://api.openweathermap.org/data/2.5/weather?APPID=06dc04f1d54e930bdc3d4372d7291dd1','Chicago')
strData = str(rawData, encoding='utf-8')
dictData = json.loads(strData)

mail_host="smtp.gmail.com"  #设置服务器
mail_user="tlmorphing@gmail.com"    #用户名
mail_pass="morphing"   #口令

sender = 'tlmorphing@gmail.com'
# receivers = ['tlmorphing@gmail.com', 'yzhou108@hawk.iit.edu', 'qsong4@hawk.iit.edu', 'byang24@hawk.iit.edu']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['tlmorphing@gmail.com', 'tanglonglevy@outlook.com', '452479893@qq.com', 'tllevybright@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


tem = round(dictData['main']['temp']-273.15,1)
historyFile = './history'
with open(historyFile, 'r') as f:
    hisTep = f.read()

if float(hisTep)<tem:
    word = '今天好像暖和点了'
else:
    word = '今天又变冷了'
with open(historyFile, 'w') as f:
    f.write(str(tem))

temMin = round(dictData['main']['temp_min']-273.15,1)
temMax = round(dictData['main']['temp_max']-273.15,1)
weather = dictData['weather'][0]['main']



sw = {
    'Rain': '雨',
    'Clouds': '多云',
    'Snow': '雪',
    'Clear': '晴'
}

for i in range(len(receivers)):
    msgRoot = None
    msgRoot = MIMEMultipart('related')
    if i != 3:
        hero, win, lost = dota.get(account[i])
        heroStr = ''
        hero = list(set(hero))
        length = len(hero)
        if length == 1:
            heroStr = hero[0]
        else:
            for j in range(length):
                if j == 0:
                    heroStr += hero[j]
                elif j == length-1:
                    heroStr += '和' + hero[j]
                else:
                    heroStr += ', ' + hero[j]

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        msgText = MIMEText('早上好, 芝加哥的朋友\n'+'今天天气: ' + sw[weather] + '\n最低气温 : ' + str(temMin) + '°C' + '\t最高气温 : ' + str(temMax) + '°C\t' + word + '\n您昨天司职' +
                           heroStr + ', 获得了' + str(win) + '胜' + str(lost) + '负的某改战绩\n' + '祝您生活愉快\n', 'plain', 'utf-8')
    else:
        msgText = MIMEText('早上好, 芝加哥的朋友\n'+'今天天气: ' + sw[weather] + '\n最低气温 : ' + str(temMin) + '°C' + '\t最高气温 : ' + str(temMax) + '°C\n' + word + '\t祝您生活愉快\n', 'plain', 'utf-8')
    msgRoot['From'] = Header("力量的花生", 'utf-8')
    to_nickName = Header("渺小的凡人", 'utf-8')
    to_nickName.append('<' + receivers[i]  + '>', 'ascii')
    msgRoot['To'] = to_nickName
    msgRoot.attach(msgText)

    index = random.randint(1,5)

    fp = open('./images/' + weather.lower() + str(index) + '.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgRoot.attach(msgImage)

    subject = '又是新的一天'
    msgRoot['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, [receivers[i]], msgRoot.as_string())
        smtpObj.quit()
        print("Successful")
    except smtplib.SMTPException:
        print("Error")

