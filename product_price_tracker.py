from twilio.rest import Client
from bs4 import BeautifulSoup
import requests
import os

URL = 'https://bit.ly/2mQLe4b'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

def send_sms(price):
    client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])

    message = client.messages \
                    .create(
                         body=f"Hey,\nThe price has dropped and it is now ₹{price}. Check out before stocks run out {URL}. HURRY !!!",
                         from_= os.environ['TWILIO_NO'],
                         to= os.environ['MY_NUMBER']
                     )
    print(f"Message has been sent!")

while True:
    title = soup.find("span", attrs = {"class":"_35KyD6"}).get_text()
    price = soup.find("div", attrs = {"class":"_1vC4OE _3qQ9m1"}).get_text()
    updated_price = price.replace(',', '')
    int_price = int(updated_price[1:5])

    print(f"{title} is now available for {int_price}")

    if int_price < 1500:
        send_sms(int_price)
        break
    else:
        pass