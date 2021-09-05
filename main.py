import random
import urllib.request as urllib2
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as BSHTML


let = '123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def makesoup(u):
    req = urllib2.Request(u, headers=hdr)
    page = urllib2.urlopen(req)
    soup = BSHTML(page,'lxml')
    images = soup.findAll('img')
    class1 = soup.findAll('input')
    for classe in class1:
        try:
            # print(classe["class"])
            if classe["class"] == ['uploader-chooser__input', 'js-file-upload-input']:
              #  print("False, Home page")
                return False
        except KeyError:
            pass
    for image in images:
        #print image source
        if image['src'] == "//st.prntscr.com/2021/04/08/1538/img/0_173a7b_211be8ff.png":
            # print("False,Screens hot was removed")
            return False
        else:
            return True
while True:
    def random_char(y):
        return (''.join(random.choice(let) for x in range(y)))
    url = "https://prnt.sc/" + str(random_char(6))
    url1 = makesoup(url)
    if url1 == True:
        print("Its true:",url)

