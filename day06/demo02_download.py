import urllib.request, urllib.response

url = "https://img2.baidu.com/it/u=2102736929,2417598652&fm=26&fmt=auto&gp=0.jpg"

response = urllib.request.urlopen(url)

with open("baidu.jpg", "wb") as file:
    file.write(response.read())
    pass



