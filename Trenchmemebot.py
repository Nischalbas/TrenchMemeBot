import os
import discord 
from discord.ext import commands
import random
import aiohttp
import praw
from keep_alive import keep_alive


client = commands.Bot(command_prefix="!")

@client.event 
async def on_ready():
    print("Is ready")

reddit = praw.Reddit(client_id='f2XCh_q9gi0__Fy2m1H93w',
                     client_secret='ycpCstbC-R-rX8pVzNN-Nswc-T4yKQ',
                     user_agent='Hrisabbot')

@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()

    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

keep_alive()
client.run(os.getenv('token'))