import httplib2, random
#import imgutil
from googleapiclient.discovery import build
import os
import pprint
import time
import urllib.error
import urllib.request, requests
import discord
from server import keep_alive

TOKEN = os.environ['token']
btid = [""]
# 接続に必要なオブジェクトを生成
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
# parameters

#imgutil.mkdir(path)

#page_limit = 3 # 検索ページ数
#startIndex = 1
response = []
img_list = []


@client.event
async def on_ready():
  # 起動したらターミナルにログイン通知が表示される
  print("logined")
  game = discord.Game("=help")
  await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
  if message.author.bot:
    return


keep_alive()
client.run(TOKEN)
