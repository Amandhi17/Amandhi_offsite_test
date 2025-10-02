

# Exercise 02: Web Scraping, Data Reconciliation, Email Sending, Scheduling (1 Day)

## 📌 Scenario
This exercise combines **web scraping, data reconciliation, and email sending** to automate stock price monitoring.

The goal is to track the stock price of **Apple Inc. (AAPL)** and send email alerts if the price goes above or below a certain threshold.

---

## ✅ Requirements
- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `smtplib` (built-in)
- An SMTP server (e.g., Gmail with less secure app access enabled)

---

## 🚀 Steps Implemented
1. **Web Scraping**
   - Target URL: [Yahoo Finance - AAPL](https://finance.yahoo.com/quote/AAPL?p=AAPL)  
   - Fetched HTML using `requests`  
   - Parsed content with `BeautifulSoup`  
   - Extracted stock price and converted it to a float  

2. **Data Reconciliation**
   - Read `stock_data.csv` using `pandas`  
   - Filtered prices for `AAPL` from `Company` column  
   - Compared scraped price with stored value  
   - Calculated price difference / percentage change  

3. **Email Alert**
   - Configured SMTP server with `smtplib`  
   - Defined sender, recipient, subject, and body  
   - Email included:
     - Current stock price  
     - Price difference  
     - Threshold checks  
   - Sent alert only if difference exceeded threshold  

4. **Scheduling**
   - Automated script execution using:
     - **Windows Task Scheduler** OR **cron job** (Linux/macOS)  
   - Script runs periodically (e.g., every hour)  

---

## ▶️ How to Run
1. Open a terminal in this folder  
2. Run the script:  

python script.py
ADD YOUR SENDER'S AND RECEIVER'S EMAIL ADDRESSES and APP PASSWORD  
