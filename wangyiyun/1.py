import requests


url = 'http://45.113.201.36/'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Host': '45.113.201.36',
    'Proxy-Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'session=eyJ1aWQiOiI0ODA0MjkxNjgifQ.X5OkGg.yGVvAMm_SrENaeJvPTCGHfoyCXM',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) bilibili Security Browser/70.0.3538.67 Safari/537.36',
}

r = requests.get(url, headers=headers)

print(r.text)