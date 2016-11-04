#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import smtplib
import random
import os

from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from GetWeatherData import GetWeatherData
from GetDotaData import GetDotaData
from GetPicture import GetPicture


class GoodMorning:

    def __init__(self):
        self.weatherData = {} # dictionary
        self.dotaAccount = [201956451, 247810685, 132130668]
        self.dotaHero = []
        self.dotaWin = []
        self.dotaLost = []
        self.mail_host="smtp.gmail.com"  #设置服务器
        self.mail_user="tlmorphing@gmail.com"    #用户名
        self.mail_pass="morphing"   #口令
        self.sender = 'tlmorphing@gmail.conm'
        self.receivers = ['tlmorphing@gmail.com', 'yzhou108@hawk.iit.edu', 'qsong4@hawk.iit.edu', 'byang24@hawk.iit.edu']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        # self.receivers = ['tlmorphing@gmail.com', 'tanglonglevy@outlook.com', '452479893@qq.com', 'tllevybright@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.word = []      # 变冷了还是变暖
        self.temMin = []    # 最低气温
        self.temMax = []    # 最高气温
        self.weather = []   # 气候
        self.sw = {
            'Rain': '雨',
            'Clouds': '多云',
            'Snow': '雪',
            'Clear': '晴',
            'Fog': '雾'
        } # 对应的中文

    def temCompare(self):
        tem = round(self.weatherData['main']['temp']-273.15,1)
        historyFile = './history'
        with open(historyFile, 'r') as f:
            hisTep = f.read()

        if float(hisTep)<tem:
            self.word = '今天好像暖和点了'
        else:
            self.word = '今天又变冷了'
        with open(historyFile, 'w') as f:
            f.write(str(tem))

        self.temMin = round(self.weatherData['main']['temp_min']-273.15,1)
        self.temMax = round(self.weatherData['main']['temp_max']-273.15,1)
        self.weather = self.weatherData['weather'][0]['main']

    def sendEmail(self, number):
        msgRoot = None
        msgRoot = MIMEMultipart('related')
        if number != 3:
            if self.dotaHero != []:
                heroStr = ''
                self.dotaHero = list(set(self.dotaHero))
                length = len(self.dotaHero)
                if length == 1:
                    heroStr = self.dotaHero[0]
                else:
                    for j in range(length):
                        if j == 0:
                            heroStr += self.dotaHero[j]
                        elif j == length-1:
                            heroStr += '和' + self.dotaHero[j]
                        else:
                            heroStr += ', ' + self.dotaHero[j]

                # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
                msgText = MIMEText('早上好, 芝加哥的朋友\n' +'今天天气: ' + self.sw[self.weather] + '\n最低气温 : ' + str(self.temMin) + '°C' + '\t最高气温 : ' + str(self.temMax) + '°C\t' + self.word + '\n您昨天司职' +
                                   heroStr + ', 获得了' + str(self.dotaWin) + '胜' + str(self.dotaLost) +
                                   '负的某改战绩\n' + '祝您生活愉快\n', 'plain', 'utf-8')
            else:
                msgText = MIMEText('早上好, 芝加哥的朋友\n'+'今天天气: ' + self.sw[self.weather] + '\n最低气温 : ' + str(self.temMin) + '°C' + '\t最高气温 : ' + str(self.temMax) + '°C\t' + self.word +
                                   '\n您昨天一把未战\t何不邀请朋友来开黑呢\n' + '祝您生活愉快\n', 'plain', 'utf-8')
        else:
            msgText = MIMEText('早上好, 芝加哥的朋友\n'+'今天天气: ' + self.sw[self.weather] + '\n最低气温 : ' + str(self.temMin) + '°C' + '\t最高气温 : ' + str(self.temMax) + '°C\n' + self.word + '\t祝您生活愉快\n', 'plain', 'utf-8')
        msgRoot['From'] = Header("力量的花生", 'utf-8')
        to_nickName = Header("渺小的凡人", 'utf-8')
        to_nickName.append('<' + self.receivers[i]  + '>', 'ascii')
        msgRoot['To'] = to_nickName
        msgRoot.attach(msgText)

        # index = random.randint(1,5)
        # fp = open('./images/' + self.weather.lower() + str(index) + '.jpg', 'rb')
        # msgImage = MIMEImage(fp.read())
        # fp.close()

        fp = open('0.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        os.remove('0.jpg')

        msgRoot.attach(msgImage)

        subject = '又是新的一天'
        msgRoot['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, [self.receivers[i]], msgRoot.as_string())
            smtpObj.quit()
            print("Successful")
        except smtplib.SMTPException:
            print("Error")

    def start(self, number):
        self.weatherData = GetWeatherData.getWeatherData(self) # get weather data
        GetPicture.start(self)                                 # get the picture
        self.temCompare()
        if number != 3:
            self.dotaHero, self.dotaWin, self.dotaLost = GetDotaData.get(self.dotaAccount[number])
        self.sendEmail(number)

if __name__ == '__main__':
    goodMorning = GoodMorning()
    for i in range(4):
        goodMorning.start(i)


def swap(a, b):
    tem = a
    a = b
    b = tem