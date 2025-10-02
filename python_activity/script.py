#import necessary libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from email.message import EmailMessage
import smtplib

#URL
URL="https://finance.yahoo.com/quote/AAPL/?p=AAPL"

#fetch the HTML content of the webpage
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/58.0.3029.110 Safari/537.3'
}
response=requests.get(URL,headers=headers)
print('response status code:',response.status_code)

#locate the element containing the stock price
soup = BeautifulSoup(response.content , 'html.parser')
price_element=soup.find('span',{'data-testid':'qsp-price'})

#convert  to a float value
if price_element:
    stock_price=price_element.text
    stock_price=float(stock_price.replace(',',''))

#Print the stock price
    print("Apple stock price:",stock_price)
else:
    print("Could not find the stock price element.")

#read the csv file
df=pd.read_csv('stock_data.csv')
print(df.head())

#filter apple price
apple_data=df[df['Company']=='AAPL']
print(apple_data)

#get the last price from the csv file
last_price=apple_data['Price'].iloc[-1]
print("Last recorded price from CSV:",last_price)

#price difference and percentage change
price_difference=stock_price - last_price
print(f"Price difference:{price_difference:.2f}")
percentage_change=(price_difference/last_price)*100
print(f"Percentage change:{percentage_change:.2f}%")

#email alert function
def send_alert(current_price,diff,pct_change):
    msg =EmailMessage()
    msg['Subject']="Apple Stock Price Alert"
    msg['From']="SENDERS'S EMAIL"
    msg['To']="RECEIVER'S EMAIL"
    msg.set_content(f"""
                    Apple stock price :{current_price}
                    change: {diff:.2f}
                    Percentage change: {pct_change:.2f}%
   """ )
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login("SENDERS'S EMAIL","APP_PASSWORD")
        server.send_message(msg)
        print("Email sent successfully.")   
#threshold for alert
threshold=1.0
if abs(percentage_change) > threshold:
    send_alert(stock_price,price_difference,percentage_change)
else:
    print("No significant change in stock price.")





                                
