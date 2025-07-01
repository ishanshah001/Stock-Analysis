# Automated Stock Analysis and News Emailer

## Overview
This Python script automates the process of analyzing a chosen stock's recent market data, fetching related news articles, and sending a consolidated summary via email. It leverages public APIs for stock data and news, web scraping techniques, and SMTP for email delivery.

## Features
- Fetches daily stock price data using Alpha Vantage API.
- Calculates day-over-day differences for open, high, low, close prices, and volume.
- Computes percentage changes to give insight into stock performance.
- Retrieves the latest news headlines related to the company from NewsAPI.
- Sends an automated email with the stock analysis and top news articles.

## Technologies Used
- Python 3
- `requests` for API calls
- `datetime` for date handling
- `smtplib` for sending emails via SMTP
- Public APIs:
  - [Alpha Vantage](https://www.alphavantage.co/) for stock data
  - [NewsAPI](https://newsapi.org/) for news articles

## Setup Instructions

1. **Clone the repository or copy the script**

2. **Install dependencies** (if not already installed):

3. **Configure the script**

- Replace ```YOUR_API_KEY``` with your Alpha Vantage API key.
- Replace ```YOUR_NEWS_API_KEY``` with your NewsAPI key.
- Set your email credentials (```my_email``` and ```password```) in the script.
- Update ```to_email``` list with recipient email addresses.
- Modify ```STOCK_NAME```, ```COMPANY_NAME```, and ```SYMBOL``` to your stock of interest.

4. **Run the script**
```
python your_script_name.py
```

## How It Works
- The script fetches the daily stock data for the selected symbol.
- It compares yesterday's data with the day before yesterday's data (skipping weekends) and calculates the differences in open, high, low, close, and volume.
- It fetches up to 3 recent news articles related to the company.
- It combines the stock data summary and news into an email body.
- Sends the email to all listed recipients.

## Note
- The script currently supports sending emails via Gmail's SMTP server. If you use Gmail, you might need to enable "App Passwords" or allow "Less Secure Apps" (not recommended) for the login to work.
- The stock market is closed on weekends, so the script accounts for that in its logic.
- The news section picks random articles from the most recent new
