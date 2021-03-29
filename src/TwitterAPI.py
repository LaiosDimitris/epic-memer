import tweepy

class TwitterAPI:
    def __init__(self, API_KEY: str, API_SECRET_KEY: str, ACCESS_TOKEN: str, ACCESS_TOKEN_SECRET: str):
        self.__API = tweepy.API(self.__getAuthorization(
            API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
        ))
    
    def getLatestTweet(self, username: str):
        tweet = self.__getLastTweetFromUserTimeline(username)
        return tweet if tweet != None else None

    def __getLastTweetFromUserTimeline(self, username):
        try:
            tweet = self.__API.user_timeline(screen_name=username, count=1, include_rts = False, tweet_mode = 'extended')[0]
            return tweet.extended_entities['media'][0]['video_info']['variants'][0]['url']
        except Exception as TwitterApiError:
            print(f"Error while getting {username}'s last tweet\n{TwitterApiError}")
            return None

    def __getAuthorization(self, API_KEY: str, API_SECRET_KEY: str, ACCESS_TOKEN: str, ACCESS_TOKEN_SECRET: str):
        authorization = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        authorization.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return authorization
