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
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        x = random.randint(0,29)
        urllib.request.urlretrieve(imglist[x],'%s.jpg' % 0)

    def start(self):
        html = GetPicture.getHtml("http://www.meizitu.com/")
        GetPicture.getImg(html)
