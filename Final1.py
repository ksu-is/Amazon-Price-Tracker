from bs4 import BeautifulSoup
import requests
import smtplib
import time
import html5lib

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html5lib")

    soup2 = BeautifulSoup(soup1.prettify(), "html5lib")

    title = soup2.find(id="productTitle").get_text().strip()

    price = soup2.find('span', class_='a-offscreen').get_text().strip()
    priceWithoutSign = price.split("$")[1]
    floatprice = float(priceWithoutSign)
    offerprice = 17
    if floatprice <= offerprice:
        send_mail()
    print(title)
    print(floatprice)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('TrackerAMZN@gmail.com', 'Shared83617')
    subject = 'Price has dropped!'
    body = 'Check the amazon link below to see your deal!', URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('TrackerAMZN@gmail.com','TrackerAMZN@gmail.com',msg)
    print('MESSAGE HAS BEEN SENT')
    server.quit()
while(True):    
    check_price()
    time.sleep(15)