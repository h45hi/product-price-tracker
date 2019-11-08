# product-price-tracker
A fun script which saves you few clicks to check price for a product
## Description
This script was designed to save me from stress during flash sale. I have a bad habbit of checking my phone constantly during flash sale if price of the product has dropped or not. So it was time, to put web scrapping to work and let python monitor the price and notify if price drops below my mark.
## Pre-Requisites
As there are few f-strings in script, python version should be 3.6 or higher and some 3rd party libraries like twilio and Beautifulsoup which you can find in ```requirements.txt```
## Workflow
**Step-1**\
First create a virtual environment and install all dependencies from ```requirements.txt```. You can do so by running the following command
```pip install -r requirements.txt```\
**Step-2**\
Please make sure to change few details according your need
- URL: URL of the product you want to track
- TWILIO_ACCOUNT_SID & TWILIO_AUTH_TOKEN: It will be provided by [Twilio](https://www.twilio.com) upon signing up.
- body, from_, to: message body, twilio number and your number to which sms alert will be sent

Sensitive data like ```TWILIO_ACCOUNT_SID```, ```TWILIO_AUTH_TOKEN```, ```from_``` and ```to``` should be stored as environment variables.\
**Step-3**\
After installing all dependencies and setting up all variables you can run the script \
```python3.6 product_price_tracker.py```
