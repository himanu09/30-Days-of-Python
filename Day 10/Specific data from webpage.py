from turtle import title
import requests
from bs4 import BeautifulSoup
url="https://www.horoscope.com//us//index.aspx"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,"html.parser")
# print(soup.prettify)
title=soup.title
print(title.text)
aries=soup.find(id='src-hp-aries')
for item in aries.stripped_strings:
    print(item)
Gemini=soup.find(id='src-hp-gem')
for item in Gemini.stripped_strings:
    print(item)
Cancer=soup.find(id='src-hp-canc')
for item in Cancer.stripped_strings:
    print(item)
Leo=soup.find(id='src-hp-leo')
for item in Leo.stripped_strings:
    print(item)
Virgo=soup.find(id='src-hp-virgo')
for item in Virgo.stripped_strings:
    print(item)
Libra=soup.find(id='src-hp-lib')
for item in Libra.stripped_strings:
    print(item)
Scorpio=soup.find(id='src-hp-scpo')
for item in Scorpio.stripped_strings:
    print(item)