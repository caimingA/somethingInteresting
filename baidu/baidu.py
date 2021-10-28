import urllib3
import re
from bs4 import BeautifulSoup
import time


if __name__ == "__main__":
    url = input("please input url of baidu wenku: ") 
    # url = "https://wenku.baidu.com/view/766985613c1ec5da50e2709e.html"
    header = {'User-agent': 'Googlebot'}
    http = urllib3.PoolManager()
    request = http.request('GET', url, headers=header)
    # print(request.data)
    target = request.data
    
    plist = list()
    soup = BeautifulSoup(target, "html.parser", from_encoding="utf-8")
    # print(soup)
    plist.append(soup.title.string)
    for div in soup.find_all('div', attrs={"class": "bd doc-reader"}):
        plist.extend(div.get_text().split('\n'))
    plist = [c.replace(' ', '') for c in plist]
    plist = [c.replace('\x0c', '') for c in plist]
    # print(plist)

    now = time.strftime("%Y%m%H%M%S", time.localtime())
    # print(now)
    title = plist[0] + now + ".txt";
    print(title)
    file = open(title, mode='w', encoding='utf-8')
    for str in plist:
        file.write(str + '\n')
    
    file.close()
    input("love wanglinqi")
