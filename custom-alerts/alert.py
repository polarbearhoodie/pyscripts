import requests
from requests.auth import HTTPBasicAuth


# custom implementation of reading .env files due to PIP inconsistencies
def loadEnv():
    env_file = open(".env", "r")
    env_dict = {}

    for kv_pair in env_file:
        line = kv_pair.strip().split("=", 1)
        # no dangling spaces
        line = [x.strip() for x in line]
        env_dict[line[0]] = line[1]

    env_file.close()

    return env_dict


# static local, load .env only once
data = loadEnv()
server_url = data['SERVER_URL']
env_auth = HTTPBasicAuth(data['USER'], data['WORD'])


# a method of activating ntfy push notifications
def pushNotification(title, message, category):
    requests.post(server_url + category,
                  headers={"Title": title},
                  data=message,
                  auth=env_auth)

