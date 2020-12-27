import requests

url = 'https://www.wanandroid.com/user/login'
payload = {'username': 'gaobaojian', 'password': '123qwe.@'}
s = requests.session()
# 登录
s.post(url=url, data=payload)
# 查看收藏
r2 = s.get('https://www.wanandroid.com/lg/collect/list/0/json')
print(r2.json())
