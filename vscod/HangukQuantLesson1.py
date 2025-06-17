from bs4 import BeautifulSoup
import pandas as pd
import requests
def get_sp_500_ticker():
    res = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    #making the content readable
    soup = BeautifulSoup(res.content, 'lxml')
    #finds the first table
    table = soup.find_all('table')[0]
    #now we read it and put it into a pandas df... i think
    df = pd.read_html(str(table))
    #takes the df and only outputs symbol, if the table on Wiki used some other word(ticker), we would write ticker here.
    tickers_list = list(df[0].Symbol)
    return tickers_list
    #print(df[0].to_json(orient='records'))
ticker = get_sp_500_ticker()
print(ticker)