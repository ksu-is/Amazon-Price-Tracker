import requests
from bs4 import BeautifulSoup
import smtplib
import time
import html5lib

URL = input("Enter Amazon URL")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

offerprice = float(input("Enter Wanted Price: "))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('trackeramzn@gmail.com', 'Shared83617'))

def check_price(URL,Price):
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html5lib")

    soup2 = BeautifulSoup(soup1.prettify(), "html5lib")

    title = soup2.find(id="productTitle").get_text().strip()

    price = soup2.find('span', class_='a-offscreen').get_text().strip()
    priceWithoutSign = price.split("$")[1]
    floatprice = float(priceWithoutSign)
    if floatprice <= Price:
        send_mail(server)
    print(title)
    print(floatprice)  
    
def send_mail(server):
    subject = 'Price has dropped!'
    body = 'Check the amazon link below to see your deal!', URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('TrackerAMZN@gmail.com',input("Enter your email: "),msg)
    print('MESSAGE HAS BEEN SENT')
try:    
    while(True):    
        check_price(URL, offerprice)
        time.sleep(15)
except KeyboardInterrupt:
    server.quit()


