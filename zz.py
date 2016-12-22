import requests
import re


s = requests.Session()

proxies = {
    'http': 'http://127.0.0.1:8087',
    'https': 'https://127.0.0.1:8087'
}

r = requests.get(
    'http://t66y.com/htm_data/7/1612/2174091.html', proxies=proxies)
print r.text.encode('utf-8')
