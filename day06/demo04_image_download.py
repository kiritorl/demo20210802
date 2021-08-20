import urllib.request
import urllib.response
import threading
import sys

class Downloader(threading.Thread):
    def __init__(self, url, path, fileName):
        super().__init__()
        self.__url = url
        self.__path = path
        self.__fileName = fileName
        pass

    def run(self):
        urllib.request.urlretrieve(self.__url)
        urllib.request.urlretrieve(self.__url, self.__path, self.callback)
        pass

    def callback(self, block, blocksize, contentLength):
        per = block*blocksize / contentLength * 100
        if per > 100:
            per = 100
            pass
        sys.stdout.write("%d" % per)
        sys.stdout.flush()
        pass
    pass


url = "https://img2.baidu.com/it/u=2102736929,2417598652&fm=26&fmt=auto&gp=0.jpg"
path = "a.png"
dd = Downloader(url, path, 'a.png')
dd.start()
