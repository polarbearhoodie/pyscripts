import requests

INFLUX_URL="http://YOUR_INFLUX_URL"
INFLUX_AUTH="YOUR_KEY"


# 'Content-Type': 'text/plain'

head = {'Authorization': 'Token {}'.format(INFLUX_AUTH)}

a = 0.64
b = 0.70

payload = "weather,sensor=pico thermistor={},photocell={}".format(a, b)
print(payload)

response = requests.post(INFLUX_URL, headers=head, data=payload)

print(response.status_code)
print(response.text)
