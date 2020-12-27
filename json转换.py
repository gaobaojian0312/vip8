import requests
import json
url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-UUCAO1609062696407.html'
headers = {'X-Requested-With': 'XMLHttpRequest', 'Host': 'www.kuaidi.com',
           'Cookie': r'lang=zh-cn; theme=default; sid=opmc263h24jdbhc70bfp117p90; UM_distinctid=176a39c1f7d4cd-0bf6e8ce81c645-c791039-1fa400-176a39c1f7e755; CNZZDATA1254194234=580963065-1609058756-%7C1609058756; __gads=ID=2845822829007c9b-22419b8f54c500f4:T=1609062682:RT=1609062682:S=ALNI_MZuIL-bFPML-8bojqYbrxkrq4AjbQ'}
r = requests.post(url=url, headers=headers)
data = r.json()
print(data['data'][0]['context'])
j = json.dumps(data)
print(j)
