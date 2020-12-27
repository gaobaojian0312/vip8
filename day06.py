import requests
import json

# url = 'https://www.blog.csdn.net/rainshine1190'
# resp = requests.get(url)
# # print(resp.text)
# # print(resp.content)
# print(resp.status_code)
# print(resp.headers)
# print(resp.cookies)

# url = 'http://httpbin.org/post'
# payload = {'qq群名': '123sdasdasda', 'qq群号': '12312312'}
# header = {'User-Agent':'abc'}
# # payload = json.dumps(payload)
# # r = requests.post(url=url,data=payload)
# # print(r.json())
#
# resp = requests.post(url=url, json=payload,headers=header)
# print(resp.text)
# print(resp.headers)

url = 'https://www.wanandroid.com/user/login'
payload = {'username': 'chaoge', 'password': '123456'}
r = requests.post(url=url, data=payload)
# data = r.json()
# data = json.loads(r.content)
data = r.json()
print(data['data']['username'])
if data['data']['username'] == payload['username']:
    print('登陆成功')
