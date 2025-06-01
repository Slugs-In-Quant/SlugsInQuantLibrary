import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
#Take an input from user, and normalize it to uppercase, not sure if this matters.
#"Give me a ticker!" will be shown to the user.
input = input("Give me a ticker! ").upper()
#Now, instead of giving a ticker the user will give us a ticker, represented by input variable.
user_data = yf.download(input,start="2001-01-01",end="2025-05-20")
user_data = user_data.loc[:,"Close"].copy()

#the below comments will plot what we have thus far.
#user_data.plot(fontsize=12)
#plt.show()

#We now are finding all the returns of AAPL from this period.
ret = user_data.pct_change().dropna()
#the below comments will plot what we have thus far.
#ret.plot(kind="hist",figsize=(12,8),bins = 100)
#plt.show()

#mean_ret finds the mean of daily returns using the .mean() function
mean_ret = ret.mean()
#var_daily finds the daily mean variance of the ticker
var_daily = ret.var()
#std_ret finds the daily stddev of returns of the ticker
std_ret = ret.std()
#this will give us annual mean variance of the ticker, which we can use for stddev, 252 for trading days
annual_var_return = var_daily.mul(252)
#annualized stddev will give us.. annualized stddev
annual_stddev = np.sqrt(annual_var_return)
#Ok, so since I wanted the print statement to be all pretty I had to do all this, but its not necessary to be readable
#First I had to take out the float value of the stddev dataframe, so it could be printed nicely
#Now, to make it into a percentage value, I multiplied by 100
#Then I wanted to round off the 4th digit, any place can do, 2 may be nicer.
#Then It had to be converted to a string to be nice for the print statement
stddev_dig = float(annual_stddev.iloc[0]) 
stddev_dig = stddev_dig * 100
stddev_dig = round(stddev_dig,4)
stddev_dig = str(stddev_dig)
#my beautiful print statement
print("Annualized Standard Deviation of " + input + " is roughly " + stddev_dig + "%")
