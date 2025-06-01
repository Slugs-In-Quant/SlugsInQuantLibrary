import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#call a ticker using this method, initial calls a ticker, and using start and end you specify a time period.
ES = yf.download("ES=F",start="2001-01-01",end="2025-05-05")
#I've now turned it into a collection of its closing datas using the .loc function,
#one may presume you can call Open data as well, I would presume you are correct.
realES = ES.loc[:,"Close"].copy()
#not sure this was necessary, but it decides upon a matplot graph style decidedly
plt.style.use('seaborn-v0_8')
#here we are building the plot, fontsize variable changes type size on BOTH X AND Y AXES
#and I have no clue what figsize does, changing the variables doesn't seem to do anything...
realES.plot(figsize=(60,50),fontsize = 12)
#changes fontsize in the legend. duh.
plt.legend(fontsize='12')
#shows the plot
plt.show()


