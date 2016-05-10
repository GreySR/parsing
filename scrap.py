import urllib
import urllib.request
from bs4 import BeautifulSoup
file = open('file.txt','a')
theurl = "http://finance.yahoo.com/q/hp?s=GE&a=00&b=2&c=1962&d=03&e=25&f=2016&g=d"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")
for title in soup.findAll("th", {"class" : "yfnc_tablehead1"}):
    file.write(str(title.contents[0]).center(15, " "))
file.write('\n')
cnt = 0
for link in soup.findAll("td", {"class" : "yfnc_tabledata1"}):
    if cnt < 6:
        if len((link.contents[0])) > 12:
            file.write(str(link.contents[0]).center(15, " ")+'\n')
            cnt = 0
            continue
        file.write(str(link.contents[0]).center(15, " "))
        cnt = cnt + 1
    else:
        file.write(str(link.contents[0]).center(15, " ")+'\n')
        cnt = 0
file.close()
