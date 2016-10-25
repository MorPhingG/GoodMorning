import re
import urllib.request

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
        x = 0
        urllib.request.urlretrieve(imglist[0],'%s.jpg' % x)

    def start(self):
        html = GetPicture.getHtml("http://www.meizitu.com/")
        GetPicture.getImg(html)