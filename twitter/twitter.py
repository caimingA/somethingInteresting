import tweepy
import json
import csv

# 可能需要用到的
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# API 信息 
access_token = "1115282187895443456-oj1eKANIg85Nl889yRmlx0pQ8bpqpi"
access_token_secret = "gF1gC4rAYBf445YhB1sR9omRpoeYweSUwYMFmBeiaInSE"
consumer_key = "zfXLnAxvay7YB9TEcCqvZVg16"
consumer_secret = "N5trquk7H0lCvL8ScB5WY8p5n98FU5Z8JwqEVOfdKyuRmI6ZRf"


def on_status(status):
    if hasattr(status, "retweeted_status"):  # Check if Retweet
        try:
            print(status.retweeted_status.full_text)
            file.write(str(tweet.created_at) + " @@@ " + status.retweeted_status.full_text)
            file.write('\n')
        except AttributeError:
            print(status.retweeted_status.text)
            file.write(str(tweet.created_at) + " @@@ " + status.retweeted_status.text)
            file.write('\n')
    else:
        try:
            print(status.full_text)
            file.write(str(tweet.created_at) + " @@@ " + status.full_text)
            file.write('\n')
        except AttributeError:
            print(status.text)
            file.write(str(tweet.created_at) + " @@@ " + status.text)
            file.write('\n')


if __name__ == '__main__':
    
    # 验证你的身份
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # 获取句柄，链接API
    api = tweepy.API(auth, wait_on_rate_limit=True) # 输入认证

    
    query = "earthquake evacuation"
    tweets = api.search(query, lang="en", count=30, since="2021-07-01", tweet_mode="extended")

    # 打开一个txt文件
    file = open(query+".txt", 'w')

    i = 1
    for tweet in tweets:
        print("==================")
        print(i)
        i +=1
        on_status(tweet)
    
    file.close()