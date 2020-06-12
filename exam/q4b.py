import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'en.wikipedia.org',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en;q=0.9',
    'cookie': 'GeoIP=:::47.00:8.00:v4; forceHTTPS=true; enwikimwuser-sessionId=f0dabff1601beea9f1cf; WMF-Last-Access=02-Jun-2020; WMF-Last-Access-Global=02-Jun-2020; enwikiSession=cc7fm862kdf5jhi879d0io5k7756qhms',
    'if-modified-since': 'Tue, 02 Jun 2020 18:14:27 GMT',
}

response = requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_Republic_of_Ireland', headers=headers)
soup = BeautifulSoup(response.content, features="html.parser")
table_count = 0
for table in soup.find_all('table'):
    # print(table)
    # print(table.caption)
    table_count+=1

print(table_count)
