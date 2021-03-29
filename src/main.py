from ScheduledTweetGetter import ScheduledTweetGetter
from discord.ext import commands
import json

client = commands.Bot('#')

tweetGetter = ScheduledTweetGetter()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    client.loop.create_task(sendTweets())

def getChannels():
    return [channel for guild in client.guilds 
                        for channel in guild.channels 
                            if channel.name == '😂memes']
                            
async def sendTweets():
    while True:
        tweetsToSend = await tweetGetter.getTweets()
        for tweet in tweetsToSend:
            for channel in getChannels():
                await channel.send(tweet)

if __name__ == "__main__":
    with open('../data/botToken.json', 'r') as jsonFile:
        client.run(json.load(jsonFile)['token'])