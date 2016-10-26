import re
import urllib.request
import random

class GetPicture:

    def getHtml(url):
        req = urllib.request.Request(url)
        page = urllib.request.urlopen(req)
        html = page.read()
        return html

    def getImg(html):
        html = html.decode("gbk")
        reg = r'src="(http.+?\.jpg)"'
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        print(imglist)
        x = random.randint(0,29)
        urllib.request.urlretrieve(imglist[x],'%s.jpg' % 0)

    def start(self):
        html = GetPicture.getHtml("http://www.meizitu.com/")
        GetPicture.getImg(html)
