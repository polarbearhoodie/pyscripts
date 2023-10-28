import time
import requests
from timeit import default_timer as timer

from requests.auth import HTTPBasicAuth
wyze = HTTPBasicAuth('USER', 'PASSWORD')


while True:
    start = timer()
    image = requests.get("http://YOUR_URL_HERE", auth=wyze)

    if image.status_code == 200:
        t = time.localtime()
        utc_str = str(int(time.mktime(t)))
        filename = "photos/{}.jpg".format(utc_str)

        with open(filename, 'wb') as file:
            file.write(image.content)

    end = timer()
    elapse = end - start
    time.sleep(6 - elapse)
