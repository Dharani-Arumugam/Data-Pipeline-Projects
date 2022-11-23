# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import tweepy
import s3fs
import json
def etl_twitter_run():
    consumer_key           = "7AcJFL7y4p8IF7yCzk0CdYU70"
    consumer_secret        = "cWOdKyi0z4um248xpcEzD0F3BkUeJ9foubjyz585XAqqkpO9X5"
    access_token           = "1381642000001286151-MSQ0eUHtBsfnnNdcXpucpPZiJoi4Hm"
    access_token_secret    = "ZtRpLs1YbIDlVNCjcZFPPQ0XfvjaOMy77UZrkGZrWrtaI"

    #Twitter authentication
    auth = tweepy.OAuth1UserHandler(consumer_key,
                                    consumer_secret,
                                    access_token,
                                    access_token_secret)
    api  = tweepy.API(auth)

    tweets = api.user_timeline(screen_name= '@elonmusk',
                               count = 200,
                               include_rts = False,
                               tweet_mode = 'extended')

    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]
        refined_tweet = {"user": tweet.user.screen_name,
                         'text' : text,
                         'favorite_count' : tweet.favorite_count,
                         'retweet_count' : tweet.retweet_count,
                         'created_at' : tweet.created_at}
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv('s3://twitter-dag-bucket/refined_tweets_s3.csv')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    etl_twitter_run()

