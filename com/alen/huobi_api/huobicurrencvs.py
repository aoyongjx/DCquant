import requests

BASEURL = 'https://api.huobi.pro'

# 获取所有币种
currencys = '/v1/common/currencys'

currencys_url = BASEURL + currencys
print(currencys_url)


resp = requests.get(currencys_url)
print(resp)
print(resp.status_code)
print(resp.json())
r_json = resp.json()
data = r_json['data']
# print(data)
# print()
for d in data:
    print(d)