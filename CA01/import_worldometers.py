import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.worldometers.info',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'fsbotchecked=true; _ga=GA1.2.2130102090.1583759140; _fsuid=fec19354-3298-4c7f-9087-31194509f045; __beaconTrackerID=gqgupcm8z; __qca=P0-770848749-1583759142013; __gads=ID=8dc8fb1cf54bb6b6:T=1583759142:S=ALNI_MYJG68DHk_wjjHwF4MAx-XWAs4_6Q; cookieconsent_status=dismiss; __atssc=reddit^%^3B3; _fsloc=?i=IE^&c=Cork; __cfduid=d52a0fcc4f30047636dc108f4ad7342761584114420; _gid=GA1.2.464114386.1584890967; _fssid=4418d2a3-38e8-4577-8d3a-15b06505dc49; fssts=false; __atuvc=31^%^7C11^%^2C19^%^7C12^%^2C15^%^7C13; __atuvs=5e78fdeec0e3a842000',
    'if-none-match': '^\\^8180999-1584987587;br^\\^',
}

response = requests.get('https://www.worldometers.info/coronavirus/', headers=headers, verify=False)
 
soup = BeautifulSoup(response.content, features="html.parser")
# print(soup.prettify())

cells = soup.find_all('td')
# print(len(cells))
for cell in cells:
    print(cell.string)