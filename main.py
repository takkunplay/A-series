import os
import pprint
import time,asyncio
import urllib.error
import urllib.request, requests
import discord,random,sys
from server import keep_alive
from replit import db
from discord.ext import tasks
import xml.etree.ElementTree as ET
TOKEN = os.environ['token']
btid = [""]
# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)
# parameters
STM="=help|あゆさんまじ神"
#imgutil.mkdir(path)
mutes=[159985870458322944,894191491277258752,411916947773587456]
#page_limit = 3 # 検索ページ数
#startIndex = 1
response = []
img_list = []
#db["kaso"]=311
sex="丗糶背瀬畝競施世攻責勢谷扠設政生性製成説選聖"
@client.event
async def on_ready():
  # 起動したらターミナルにログイン通知が表示される
  print("loguined")
  game = discord.Game(STM)
  await client.change_presence(status=discord.Status.online, activity=game)
  channel=client.get_channel(906399117692010576)
  user=await client.fetch_user(713400700813705256)
  dm=await user.create_dm()
  #await channel.send("=help g")
  channel=client.get_channel(912536602071420969)
  await channel.connect()
  guild=client.get_guild(876782808847220786)
  
  while 1==1:
    if 1640962789==int(time.time()):
      break
    await asyncio.sleep(0.5)
  channel=client.get_channel(906399117692010576)

  await channel.send("日本年腰10秒前！")
  await asyncio.sleep(1)
  guild.voice_client.play(discord.FFmpegPCMAudio("10sec.wav"))
  await asyncio.sleep(10)
  await channel.send("https://cdn.discordapp.com/attachments/906399117692010576/926365032919465994/superup.mov")
  guild.voice_client.play(discord.FFmpegPCMAudio("superup.mp3"))
  await asyncio.sleep(7)
  guild.voice_client.play(discord.FFmpegPCMAudio("goodsad.mp3"))
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
  if message.content=="=shop":
    await message.channel.send("準備中")
  #ギャンブル
    #半分倍
  if message.content=="=g bh":
    ido=str(message.author.id)
    money=db["money"][ido]
    kake=int(money/2)
    if money==1:
      kake=1
    if kake==0:
      await message.reply("これ、かけるお金がﾅｲ！")
      return
    if random.randint(1,2)==1:
      db["money"][ido]=money+(kake*2)
      dme=await message.reply(str(kake)+"Aかけて*成功して*"+str(kake)+"A増えました("+str(money+(kake*2))+"A)")
    else:
      db["money"][ido]=money-kake
      dme=await message.reply(str(kake)+"Aかけましたが*失敗して*"+str(kake)+"A減りました("+str(money-kake)+"A)")
    await asyncio.sleep(30)
    await dme.delete()
    #全財産ぶちまけイベント
  if message.content=="=g ba":
    ido=str(message.author.id)
    money=db["money"][ido]
    if money==0:
      await message.reply("これ、かけるお金がﾅｲ！")
      return
    if random.randint(1,2)==1:
      db["money"][ido]=money*2
      dme=await message.reply(str(money)+"Aかけて*成功して*"+str(money)+"A増えました("+str(money*2)+"A)")
    else:
      db["money"][ido]=0
      dme=await message.reply(str(money)+"Aかけましたが*失敗して*"+str(money)+"A減りました(0A)")
    await asyncio.sleep(30)
    await dme.delete()
  #pinpon
  if message.content=="=ping":
    raw_ping = client.latency
    # ミリ秒に変換して丸める
    ping = round(raw_ping * 1000)
    # 送信する
    await message.reply(f"Pong!\n"+str(ping)+"ms")
  if message.content=="=help":
    await message.reply("""
=kaso:過疎を防止します。
=money:所持金を表示します
=hey <〇〇>:誰かを呼びます(help heyで詳細)
=g:ギャンブルします(help gで詳細)
https://onl.tw/EnNEE4u :ステータスを表示します""")
  if message.content=="=help hey":
    await message.reply("""
=hey 2 1:2 1さんを呼びます
=hey ayu:あゆさんを呼びます
=hey rami:ラミエルさんを呼びます)""")
  if message.content=="=help g":
    await message.reply("""
=g bh:全財産の半分を倍にします
=g ba:全財産を倍にします""")
  if message.content=="=kaso":
    rnd=random.randint(0,5)
    if rnd==0:
      await message.channel.send("https://cdn.discordapp.com/attachments/906399117692010576/925178035668402186/kasokin.mp4")
    elif rnd==1:
      await message.channel.send("https://cdn.discordapp.com/attachments/906399117692010576/926750544683487242/kasokin.mov")
    else:
      await message.channel.send("https://cdn.discordapp.com/attachments/906399117692010576/914472044970795028/kasokin.mov")
  if (message.content=="=kaso") or (message.content=="/kaso") or (message.content=="/kaso_n") or (message.content=="/kaso_i"):
    db["kaso"]=db["kaso"]+1
    await message.channel.send("今までに"+str(db["kaso"])+"回過疎りました")
  if message.content=="=kaos":
    await message.reply("もしかして:=kaso")
  if (random.randint(0,500)==1) or (message.content[:2]=="設ｘ"):
    await message.channel.send(sex[random.randint(0,len(sex)-1)]+"ｘしたい")
  #hey
  if message.content=="=hey 2 1":
    await message.channel.send("Hey! <@!347556496231366656>!")
  if message.content=="=hey ayu":
    await message.channel.send("Hey! <@!876782491783024641>!")
  if message.content=="=hey rami":
    await message.channel.send("Hey! <@!890178063210545182>!")
  if message.content=="=urs":
    try:
      message.guild.Voice_Client.stop()
    except:
      pass
    message.guild.voice_client.play(discord.FFmpegPCMAudio("うるさいわボケー.mp3"))
  if message.content=="=ynk":
    me=await message.guild.fetch_member(441098719803211788)
    try:
      message.guild.Voice_Client.stop()
    except:
      pass
    #guild=client.get_guild(876782808847220786)
    for mute in mutes:
      user=await message.guild.fetch_member(mute)
      if (user.voice==None) or (user.voice.channel.id!=me.voice.channel.id):
        continue
      await user.edit(mute=True)
    message.guild.voice_client.play(discord.FFmpegPCMAudio("yanki.mp3"))
    await asyncio.sleep(18)
    for mute in mutes:
      user=await message.guild.fetch_member(mute)
      if (user.voice==None) or (user.voice.channel.id!=me.voice.channel.id):
        continue
      await user.edit(mute=False)
  if message.content=="=10":
    try:
      message.guild.Voice_Client.stop()
    except:
      pass
    message.guild.voice_client.play(discord.FFmpegPCMAudio("10sec.wav"))
  if message.content=="=ns":
    role = message.guild.get_role(919543222450159636)
    if None==discord.utils.get(message.author.roles, name='にんじんしりしり'):
      await message.author.add_roles(role)
    else:
      await message.author.remove_roles(role)
  if message.content=="=egg":
    role = message.guild.get_role(919544905196511252)
    if None==discord.utils.get(message.author.roles, id=919544905196511252):
      await message.author.add_roles(role)
    else:
      await message.author.remove_roles(role)
  #bot管理者以外立入禁止
  if (message.author.id!=425948316334030848) and (message.author.id!=441098719803211788):
    return
  if message.content[:4]=="=del":
    db["money"][message.content[5:]]=0
    await message.reply("<@!"+message.content[5:]+">の財産\nhttps://cdn.discordapp.com/attachments/906399117692010576/925892604950880256/kieuseta.mov")
  if message.content[:4]=="=say":
    if message.reference==None:
      await message.delete()
      await message.channel.send(message.content[5:])
    else:
      await message.delete()
      rm=await message.channel.fetch_message(message.reference.message_id)
      await rm.reply(message.content[5:])
  
keep_alive()
client.run(TOKEN)
