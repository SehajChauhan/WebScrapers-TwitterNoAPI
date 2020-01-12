from twitterscraper import query_tweets
import datetime as dt
import pandas as pd


start_date = dt.date(2020,1,7)
stop_date = dt.date(2020,1,12)

TweetLimit = 2000
language = 'english'
query = input("Enter query: ")

tweets = query_tweets(query, begindate = start_date, enddate = stop_date, limit = TweetLimit, lang = language)

df = pd.DataFrame(t.__dict__ for t in tweets)
df = df[['text', 'hashtags', 'likes', 'retweets', 'replies']]
df.to_csv('tweets.csv', index=False)
