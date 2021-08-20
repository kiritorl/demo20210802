import requests

# requests 采集数据
url = "http://www.baidu.com"
response = requests.get(url)
if response.status_code == 200:
    # print(response.raw)
    # print(response.text)
    pass

# 爬虫 requests bs4 scrapy
url = "http://httpbin.org/post"
data = {"name": "zhangsan",
        "age": 10}
response = requests.post(url, data=data)
if response.status_code == 200:
    # print(response.text)
    pass

headers = {
    "host": "httpbin.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
}
response = requests.post(url, data=data, headers=headers)
if response.status_code == 200:
    # print(response.text)
    pass

url = "https://ip.taobao.com/outGetIpInfo"
response = requests.get(url, params={"ip": "222.222.222.222", "accessKey": "alibaba-inc"})
print(response.text)

