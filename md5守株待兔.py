import requests
import time

init_url = "http://ctf5.shiyanbar.com/misc/keys/keys.php"
key_time = int(time.time())+10
url = "http://ctf5.shiyanbar.com/misc/keys/keys.php?key="+str(key_time)
while 1:
    res = requests.get(url)
    print(res.text)
    if "false" not in res.text:
        break
