import urllib.request
import urllib.parse
import json

class GetWeatherData:

    def getfile(file):
        f = open(file)
        rawContent = f.readlines()
        strContent = ''
        for i in range(len(rawContent)):
            strContent += rawContent[i]
        return strContent

    def geturl(url):
        req = urllib.request.Request(url)
        page = urllib.request.urlopen(req)
        html = page.read()
        return html

    def getData(url,city):
        values = {'q' : city}
        data = urllib.parse.urlencode(values)
        data = bytes(data, encoding = "utf8")
        req = urllib.request.Request(url, data)
        page = urllib.request.urlopen(req)
        html = page.read()
        return html

    def getWeatherData(self):
        rawData = GetWeatherData.getData('http://api.openweathermap.org/data/2.5/weather?APPID=06dc04f1d54e930bdc3d4372d7291dd1', 'Chicago')
        strData = str(rawData, encoding='utf-8')
        weatherData = json.loads(strData)
        return weatherData

