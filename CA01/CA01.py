'''
Student Name:   Thomas Higgins
Student Number: 10544739
Course title:   Programming for Big Data         
Course ID:      B8IT105
Assignment:     CA01

Created:        2020-03-23
Editted:        2020-04-11
'''
DEBUG = True

import requests
from bs4 import BeautifulSoup

def getcoronar():
    headers = {
    'authority': 'www.worldometers.info',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'fsbotchecked=true; _ga=GA1.2.612961837.1584225072; _gid=GA1.2.1728409109.1584225072; _fsloc=?i=IE&c=Ennis; _fsuid=e847d8c5-a53e-43b2-a655-b1164a6d9031; __beaconTrackerID=lbaj4msm7; cookieconsent_status=dismiss; __cfduid=d1dd1fa78409d4f21607a427504d29ed91584354800; mobile_detect=desktop; __atuvc=2%7C11%2C54%7C12',
    'if-none-match': '"591748-1584735688;br"',
    }
    return requests.get('https://www.worldometers.info/coronavirus/', headers=headers)

def parse(data):
    return BeautifulSoup(data.content, features="html.parser")

def getdata(soup)
    #print(soup.prettify())
    data = []
    cells = soup.find_all('td')
    print(len(cells))
    print(cells[3])
    for cell in cells:
        for content in cell.contents:
            value = str(content).strip().replace('\n', '')
            # print(len(value))
            # value = removeHTML(value)
            # print(len(value))
            if len(value) == 0:
                # item = ('"0"'+',')
                item = ('0'+',')
                data.append(item)
            elif value[0].lower() in 'abcdefghijklmnopqrstuvwxyz<':
                item = ('\n' + value+',')
                data.append(item)
            else:
                #item = ('"' + value + '"' + ',')
                item = (value + ',')
                data.append(item)
    return data




# def removeHTML2(data):
#     result = []
#     for line in data:
#         index = 0
#         clean = []
#         while index <= len(line):
#             # if start of HTML brackets, find 
#             if line[index] == '<':
#                 a = line[index+1]
#                 if line[a] == '>':
#                     index=a
#                 else:
#                     if DEBUG:
#                         print('skip'+str(index))
#                     a+=1
#             else:
#                 clean.append(line[index])
#         result.append(clean)
#     return result

# def removeHTML(data):
#     result = []
#     index = 0
#     while index < len(data):
#         if data[index] == '<':
#             a = index+1
#             if data[a] == '>':
#                 index=a
#             else:
#                 a += 1
#                 if DEBUG:
#                     print(index)
#         else:
#             result.append(data[index])
#             index += 1
#     return result


# Export data to CSV
def writecsv(filename, headers, data):
    csv_file = open(filename,'w')
    csv_file.write(headers,'\n')
    for line in data:
        csv_file.write(str(line))
    csv_file.close()


#####################################################

data = getcoronadata()
# print(data)
data2 = data.strip()
print(data2)
