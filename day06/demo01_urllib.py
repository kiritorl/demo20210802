import urllib.request, urllib.response

url = "http://www.baidu.com"

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getcode())
# if response.getcode() == 200:
#     print(response.read().decode("utf-8"))
#     pass

response = urllib.request.urlopen("http://www.baidu.com")
print(response.getcode())
if response.getcode() == 200:
    with open("baidu.html", "w+", encoding="utf-8") as file:
        file.write(response.read().decode("utf-8"))
    pass

import pickle

# url = "https://cn.bing.com/search"
# data = {"q": "python"}
# data = pickle.dumps(data)
# response = urllib.request.urlopen(url, data=data)
# print(response.read().decode("utf-8"))


url = "http://httpbin.org/post"
headers = {
    "host": "httpbin.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
}

request = urllib.request.Request(url, headers=headers, method="POST")
response = urllib.request.urlopen(request)
if response.getcode() == 200:
    print(response.read().decode("utf-8"))
    pass
