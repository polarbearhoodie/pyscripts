import requests

INFLUX_URL="http://192.168.0.40:9330/api/v2/write?org=8b158fa2ed34133c&bucket=test0"
INFLUX_AUTH="n8tSCT8bQclvPKgSU1c4UGEAd7mJFt-DAu45A6KaDGV69277LPJVc1WQssKubADJX6p3quj0VYAk-wc5ed0VYg=="


# , 'Content-Type': 'text/plain'

head = {'Authorization': 'Token {}'.format(INFLUX_AUTH)}

a = 0.64
b = 0.70

payload = "weather,sensor=pico thermistor={},photocell={}".format(a, b)
print(payload)

response = requests.post(INFLUX_URL, headers=head, data=payload)

print(response.status_code)
print(response.text)
