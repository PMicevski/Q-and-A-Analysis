# -*- coding: utf-8 -*-
"""
Scraping tweets 
"""

from datetime import date, timedelta
from twitterscraper import query_tweets
import pandas as pd


# date used by twitter scrapper in query_tweets 
start_date = date(2019, 5, 6) 

# qanda_shows static number of shows variable 
qanda_shows = 41 

tweet_limit = 10000

for i in range(qanda_shows):
    
    # timedelta used to increase date range for end date in query tweets
    end_date = start_date + timedelta(days=1)
    
    # tweet extraction 
    tweets = query_tweets("#QANDA", begindate = start_date, enddate = end_date, limit = tweet_limit)
    
    # extracted tweets transformed to data frame 
    df = pd.DataFrame(t.__dict__ for t in tweets)
    
    # str_date formats date to string to be used in file name 
    date_file_name = '{0}'.format(start_date)                          
    
    # writing data frame to json file 
    df.to_json(r'E:\Py_Work\Qanda_Tweets\%sqanda.json' %date_file_name)
    
    # timedelta used to increment date to following week 
    start_date = start_date + timedelta(days=7)

