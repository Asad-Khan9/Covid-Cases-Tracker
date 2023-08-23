from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
#from win10toast import ToastNotifier
import time 
try:

    header = {"User-Agent":"chrome"}
    link = "https://www.worldometers.info/coronavirus/country/"
    print("="*100)
    print("="*100)
    print("WELCOME TO COVID DAILY!!")
    country = input("Enter the country:")
    new_link = link + country + '/'
    req = Request(new_link, headers = header) 
    html = urlopen(req)
    time.sleep(7)
    obj = bs(html, "html.parser") #html.parser

    new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]
    death = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

    print("Number of new cases today in", country,":", new_cases)
    print("Number of new deaths today in", country,":", death)
    print("="*100)
    print("="*100)

except:
    print("Enter a valid country!")
    print("="*100)
    print("="*100)

notifier = ToastNotifier()
message  = "New Cases - "+ new_cases+"\nDeath - "+death
message 
notifier.show_toast(title="COVID-19 Update for" + country, msg=message, duration=10)


