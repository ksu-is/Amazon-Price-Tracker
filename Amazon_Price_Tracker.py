from wsgiref.headers import Headers
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/GEARWRENCH-x-Core-Pinless-Universal-Extension/dp/B07QZCMBHG/?_encoding=UTF8&pd_rd_w=cO320&pf_rd_p=bbb6bbd8-d236-47cb-b42f-734cb0cacc1f&pf_rd_r=2N4KDKAFQKWM2SW9P15Q&pd_rd_r=0359d3d2-327d-4f91-a859-1275bbf36027&pd_rd_wg=uqnqv&ref_=pd_gw_ci_mcx_mi"
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

response=requests.get(url, headers = HEADER)
soup = BeautifulSoup(response.content,"lxml")
title = soup.find(id="productTitle")
price = soup.find('span', class_ = "a-offscreen")
print(title)
print(price)
