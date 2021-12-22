"""
@author: Ishan Shah

Automated chosen stock analysis, news and information sender on email using Python, APIs and web scraping.
"""

import requests
from datetime import datetime,timedelta
import random, smtplib, unicodedata

#-------------------Sample data--------------------------------------------

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "YOUR_API_KEY"
url="https://www.alphavantage.co/query"
news_api_key="YOUR_NEWS_API_KEY"
#news_url="https://newsapi.org/v2/everything?q=tesla&from=2021-04-24&sortBy=publishedAt&apiKey="+news_api_key
news_url="https://newsapi.org/v2/top-headlines"
mess=""
SYMBOL="TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


options=["1. open","2. high","3. low","4. close","5. volume"]


news_parameters={
    "q":"tesla",
    "from":str(datetime.today().date()-timedelta(days=7)),
    "sortBy":"publishedAt",
    "language":"en",
    "apiKey":news_api_key,
}


parameters={
    "function":"TIME_SERIES_DAILY",
    "apikey":API_KEY,
    "symbol":SYMBOL
}


#------------------------------Info about the stock------------------------------------------------
def stock():
    global mess
    response=requests.get(url=url,params=parameters)
    response.raise_for_status()
    data=response.json()
    daily_data=data["Time Series (Daily)"]
    #tdate = datetime(2021, 5, 22)
    tdate=datetime.today().date()
    day_of_week=datetime.today().strftime("%A")
    day_of_week = tdate.strftime("%A")
    if day_of_week=="Sunday" or day_of_week=="Monday":
        mess+="Stock market was close yesterday"
        print(mess)
    else:
        if day_of_week=="Tuesday":
            dbydate = str(tdate.date() - timedelta(days=4))
        else:
            dbydate = str(tdate.date() - timedelta(days=2))
        ydate=str(tdate.date()-timedelta(days=1))
        yesterday=daily_data[ydate]
        day_before=daily_data[dbydate]

        diff_open=float(yesterday[options[0]])-float(day_before[options[0]])
        diff_high=float(yesterday[options[1]])-float(day_before[options[1]])
        diff_low=float(yesterday[options[2]])-float(day_before[options[2]])
        diff_close=float(yesterday[options[3]])-float(day_before[options[3]])
        diff_volume=float(yesterday[options[4]])-float(day_before[options[4]])

        difference=[diff_open,diff_high,diff_low,diff_close,diff_volume]

        overall=float(yesterday[options[3]])-float(yesterday[options[0]])
        if overall>=0:
            mess+=COMPANY_NAME+": "+str(round(overall/float(yesterday[options[0]]),3))+"%"+"\n"
        else:
            mess += COMPANY_NAME+": " + str(round(abs(overall) / float(yesterday[options[0]]),3)) + "%"+" \n"
        mess+="Difference between "+ydate+" and "+ dbydate+" for "+ COMPANY_NAME+"("+SYMBOL+")"+" is:\n"
        for i in range(5):
            mess+=options[i]+": "+str(round(difference[i],3))+"\n"
        mess+="6. Percentage increase in "+ydate+" open and high: "+str(round(100*(float(yesterday[options[1]])-float(yesterday[options[0]]))/float(yesterday[options[0]]),3))+"%\n"
    news()

#-----------------------------------News finder-------------------------------
def news():
    global mess
    response=requests.get(url=news_url,params=news_parameters)
    response.raise_for_status()
    data=response.json()
    if data["totalResults"]<3:
        total=data["totalResults"]
    else:
        total=3
    articles=data["articles"]
    random.shuffle(articles)
    mess+="\n\nNews: "
    for i in range(total):
        mess+="\n"
        mess+="Source: "+articles[i]["source"]["name"]+"\n"
        mess+="Headline: "+articles[i]["title"]+"\n"+"Brief: "+articles[i]["description"]+"\n"+"For more: "+articles[i]["url"]


#-----------------------Email sender-----------------------------------------
def send_email():
    global mess
    mess="Subject: Tesla\n\n"
    stock()
    print(mess)
    mess.replace(u"\u2018", "'").replace(u"\u2019", "'")
    my_email = "your_email@gmail.com"
    password = ""
    to_email = ["","",""]
    connect = smtplib.SMTP("smtp.gmail.com")
    connect.starttls()
    connect.login(user=my_email, password=password)
    for i in to_email:
        connect.sendmail(from_addr=my_email, to_addrs=i, msg=mess)
    connect.close()

send_email()







