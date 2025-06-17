from bs4 import BeautifulSoup
import pandas as pd
import requests
import yfinance as yf
from datetime import datetime
import pytz
#read Lesson 1 for notes on this.
def get_sp_500_ticker():
    res = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))
    tickers_list = list(df[0].Symbol)
    return tickers_list
tickers = get_sp_500_ticker()
#we define a function get_history, using ticker, period_start, period_end and granularity which is the time interval
#df is now retrieving the history of a ticker from a certain period, and with a certain interval
#reset_index adds a new columns of integers
#.rename function lets us rename columns, why for most of them? I know not.
#df.empty, perhaps you think this is not useful! but what if the stock never had dividends(BRK.B)? the dataframe is empty throwing an error, so we need this
#We drop Dividends and Stock Splits because we care not.
#We set datetime as the index instead of integers 0,1,2,....,
def get_history(ticker,period_start,period_end, granularity = "1d"):
    df = yf.Ticker(ticker).history(
        start=period_start,
        end=period_end,
        interval = granularity,
        auto_adjust = True).reset_index()
    df = df.rename(columns={
        "Date":"datetime",
        "Open":"open",
        "High":"high",
        "Low":"low",
        "Close":"close",
        "Volume":"volume"
    })
    if df.empty:
        return pd.DataFrame()
    df = df.drop(columns=["Dividends","Stock Splits"])
    #df["datetime"]= df["datetime"].dt.tz_localize(pytz.utc)
    df = df.set_index("datetime",drop=True)
    return df
#defining the periods, this could be made as an input function
period_start = datetime(2010,1,1, tzinfo=pytz.utc)
period_end = datetime(2025,1,1, tzinfo=pytz.utc)
#iterates through each ticker(I THINK) in the list tickers(which is comprised of get_sp_500_ticker()) to give us OHLCV data
for ticker in tickers:
    df = get_history(ticker,period_start,period_end)
    print(ticker,df)