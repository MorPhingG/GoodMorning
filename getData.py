import urllib.request
import urllib.parse

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
