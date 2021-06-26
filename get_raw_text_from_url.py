import requests
import time

url = requests.get('https://pastebin.com/raw/ugVB27TE')
url_text = url.text
print(url_text)
time.sleep(10)
