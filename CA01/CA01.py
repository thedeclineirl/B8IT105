'''
Github:         thedeclineirl
Student Name:   Thomas Higgins
Student Number: 10544739

Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA01

Created:        2020-03-23
Editted:        2020-05-16
'''
DEBUG = False
import requests
from bs4 import BeautifulSoup

export_file = 'worldometer_corona.csv'

def get_soup():
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
    response = requests.get('https://www.worldometers.info/coronavirus/', headers=headers, verify=True)
    return BeautifulSoup(response.content, features="html.parser")

def wrangle_soup(soup):
    '''
    Wrangle soup file into lines, get rid of junk & duplicate data scraped in get_soup()
    '''
    cells = soup.find_all('td')
    if DEBUG:
        print(len(cells))
    continents = ['Africa','Asia','Australia/Oceania','Europe','North America','South America','World']
    wrangle = []
    line = []
    all_count = 0
    for cell in cells:
        if cell.string == None or cell.string == 'N/A':
            line.append('0')
        elif cell.string == 'Total:':
            return wrangle
        elif cell.string == 'All':
            if all_count==0:
                wrangle = []
                all_count +=1
        elif cell.string in continents:
            line.append(cell.string)
            wrangle.append(line)
            line = []
        elif len(line) > 13:
            wrangle.append(line)
            line = []
            txt = cell.string.replace(',','')
            line.append(txt)
        else:
            txt = cell.string.replace(',','')
            line.append(txt)
    return wrangle

def clean_soup(lines):
    '''
    Patch of a very specific bug  in wrangle_soup()-
    There was a bug with the first line every time I ran this code
    '''

    # remove first 2 lines
    line1 = lines.pop(0)
    line2 = lines.pop(0)
    # insert the last two items from line 1(Place & Country) at the beginning of line 2 
    line2.insert(0,line1[-1])
    line2.insert(0,line1[-2])
    #insert new first line back at the front of lines
    lines.insert(0,line2)
    return lines

def write_csv(filename,data):
    headers = 'Rank, Country/Ship, Total Cases, New Cases,Total Deaths, New Deaths, Total Recovered,Active Cases, Serious/Critical,Cases/1M,Deaths/1M,Total Tests,Test/1M,Continent'
    csv_file = open(filename,'w')
    csv_file.write(headers+'\n')
    for line in data:
        for cell in line:
            csv_file.write(str(cell)+', ')
        csv_file.write('\n')
    csv_file.close()
    print('Data scraped & exported to file: {0}'.format(filename))

def main():
    write_csv(export_file,clean_soup(wrangle_soup(get_soup())))

main()
