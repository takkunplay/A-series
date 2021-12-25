import os
import pprint
import time
import urllib.error
import urllib.request, requests
import discord,random
from server import keep_alive
from replit import db
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
  channel=client.get_channel(922424600107831327)
@client.event
async def on_message(message):
  if message.content[:6]=="=money":
    moneys=db["money"]
    ido=str(message.author.id)
    re=ido in moneys
    if re==False:
      money=0
    else:
      money=moneys[ido]
    await message.reply(message.author.mention+":"+str(money)+"A")
  if random.randint(0,9)==0:
    ido=str(message.author.id)
    moneys=db["money"]
    re=ido in moneys
    if re==False:
      money=0
    else:
      money=moneys[ido]
    db["money"][ido]=money+1

    
  #ここから先bot立入禁止
  if message.author.bot:
    return
  if message.content=="=help":
    await message.reply("""
=kaso:過疎を防止します。
=money:所持金を表示します""")
  if message.content=="=kaso":
    await message.channel.send("https://cdn.discordapp.com/attachments/906399117692010576/914472044970795028/kasokin.mov")
keep_alive()
client.run(TOKEN)
