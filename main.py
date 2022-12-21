import tweepy
from time import sleep

api_key = "SB0RPKE4p5Jvndd7CeSDRZego"
api_secret = "Ocln8HBN1YSezEM43s0eA3OZFCEwvsQp8BJYpkLLyjUHtKUm44"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAGVBigEAAAAA8XojdvDs1%2FjSCRQefk31ddsI9k8%3Dt1Xhu3IQOMUF0r6G62VZmS5y3xtmtNj1VpmqrJOi0tw1IOVelb"
access_token = "1326897996794105857-qrAJlGE8KcJySax0KQ18snlmm9bksu"
access_token_secret = "9DfMxe09dHwd5AigXlf24Q2NuSsYBEM1D3upBiWMT5F9w"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search_tweets, q=('(#MAMAVOTE AND #mamamoo) OR (#MAMAVOTE AND #MAMAMOO) (-filter:retweets) (-filter:replies)')).items():
    try:
        print(tweet.text)
        tweet.retweet()

            # Twitter bot sleep time settings in seconds. Use large delays so that you account will not banned
        sleep(1)  # 300 seconds = 5 minutes

    except tweepy.TweepyException as e:
        print(e)
        #break

    except StopIteration:
        break

# # Bot searches for tweets containing certain keywords
# class MyStream(tweepy.StreamingClient):
#     # This function gets called when a tweet passes the stream
#     def on_tweet(self, tweet):
#         print(tweet.text)
#         try:
#             client.retweet(tweet.id)
#
#         except Exception as  error:
#             stream.disconnect()
#             print(error)
#
#
# stream = MyStream(bearer_token = bearer_token)
#
# rule = tweepy.StreamRule("((#MAMAVOTE AND #mamamoo) OR (#MAMAVOTE AND #MAMAMOO)) (-is:retweet) (-is:replies)")
#
# stream.add_rules(rule)
#
# stream.filter()


