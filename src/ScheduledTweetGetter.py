from JsonDatabase import JsonDatabase
from TwitterAPI import TwitterAPI
import datetime
import asyncio

class ScheduledTweetGetter:
    def __init__(self) -> None:
        self.__jsonDb = JsonDatabase()
        self.__authKeys = self.__jsonDb.readAuthJsonFile()
        self.__twitter = self.__initTwitterApi(self.__authKeys)

    async def getTweets(self):
        while True:
            accounts = self.__jsonDb.readTwitterAccountsFile()
            listOfNewTweets = self.__getNewTweets(accounts)
            if len(listOfNewTweets) != 0:
                return listOfNewTweets
            await asyncio.sleep(120)

    def __getNewTweets(self, accounts: list):
        newTweets = []
        for i, account in enumerate(accounts):
            currentLastTweet = self.__getLatestTweet(account['username'])
            if account['lastTweet'] != currentLastTweet:
                if currentLastTweet == None:
                    continue
                if not self.__tweetIsValid(currentLastTweet):
                    continue
                print(f'New tweet from {account["username"]}\n{currentLastTweet}')
                accounts[i]['lastTweet'] = currentLastTweet
                newTweets.append(currentLastTweet)
        self.__updateTwitterAccounts(accounts)
        return newTweets

    def __getLatestTweet(self, username):
        print(f"\nGetting latest tweet from user {username}", datetime.datetime.now())
        return self.__twitter.getLatestTweet(username)

    def __initTwitterApi(self, authKeys: dict):
        return TwitterAPI(authKeys['API-KEY'], authKeys['API-SECRET-KEY'],
                          authKeys['ACCESS-TOKEN'], authKeys['ACCESS-TOKEN-SECRET'])

    def __updateTwitterAccounts(self, accounts: list):
        self.__jsonDb.writeToTwitterAccountsFile({"accounts": accounts})

    def __tweetIsValid(self, url: str):
        return ('mp4' in url) and (url != None)
