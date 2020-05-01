import requests
import re
import time
import smtplib
from bs4 import BeautifulSoup
URL = 'https://www.amazon.in/Samsung-Galaxy-Ocean-Blue-Storage/dp/B07HGJKDQL/ref=sr_1_1_sspa?dchild=1&keywords=smartphone&qid=1584605846&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQUtSV0w0T0czU01VJmVuY3J5cHRlZElkPUEwNTM4NjY3MzBXQzBIUE44U0FLQSZlbmNyeXB0ZWRBZElkPUEwODE2NDk4M0I0QjJTTzQzN1A0NCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_dealprice').get_text()
    alter_price = price[2:8]
    listt=re.findall(r'\d',alter_price)
    str=""
    for ele in listt:
        str+=ele

    converted_price=int(str)
    
    print(converted_price)
    print(title.strip())

    if converted_price >= 14000:
        send_mail()
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('jaididwania@gmail.com','nbjcsmvsrremqwbp')

    subject = "Price Fell Down!!!"
    body = 'Check The Link Now! https://www.amazon.in/Samsung-Galaxy-Ocean-Blue-Storage/dp/B07HGJKDQL/ref=sr_1_1_sspa?dchild=1&keywords=smartphone&qid=1584605846&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQUtSV0w0T0czU01VJmVuY3J5cHRlZElkPUEwNTM4NjY3MzBXQzBIUE44U0FLQSZlbmNyeXB0ZWRBZElkPUEwODE2NDk4M0I0QjJTTzQzN1A0NCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'jaididwania@gmail.com',
        'jaididwania0909@gmail.com',
        msg
    )

    print('MESSAGE HAS BEEN SENT!!!')
    server.quit()

while(True):
    check_price()
    time.sleep(60*60*24)