from replit import db
import os,pprint,time,asyncio,datetime,pyttsx3
import urllib.error
import urllib.request, requests
import discord,random,sys
from server import keep_alive
from replit import db
from discord.ext import tasks, commands
import xml.etree.ElementTree as ET
TOKEN = os.environ['token']
btid = [""]
mt=False
bot = commands.Bot(command_prefix='=')
# 接続に必要なオブジェクトを生成
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)
tz_jst = datetime.timezone(datetime.timedelta(hours=9))
#engine = pyttsx3.init()
# parameters
sjp=0
STM="=help|あゆさんまじ神"
#imgutil.mkdir(path)
mutes=[533698325203910668,159985870458322944,894191491277258752,411916947773587456,282859044593598464]
jug=["吐き気を催す　-3点",":-1: -2点","良くはない -1点","普通 0点","悪くはない　1点",":+1: 2点","んふーんっっっｆ 3点"]
#page_limit = 3 # 検索ページ数
#startIndex = 1
response = []
img_list = []
mml=[]
sm=0
mm=0
ksk=0
ksc=906399117692010576
#db["kaso"]=311
@tasks.loop(seconds=1)
async def restc():
  global sm,mm,ksk
  now=datetime.datetime.now(tz_jst).strftime("%H:%M:%S")
  mml.append(sm)
  mm+=sm
  sm=0
  db["mm"]=mm
  if len(mml)==61:
    mm-=mml[0]
    del mml[0]
  if now=="00:00:00":
    channel=client.get_channel(906399117692010576)
    await channel.send("今日は"+str(db["cc"])+"回発言できました！")
    print("reset")
    db["cc"]=0
@tasks.loop(seconds=10)
async def showjp():
  global mm,mml
  mm=0
  for i in mml:
    mm+=i
  game = discord.Game("=help|JP:"+str(db["jp"]/10)+"|"+str(mm)+"発言/m")
  await client.change_presence(status=discord.Status.online, activity=game)
sex="丗糶背瀬畝競施世攻責勢谷扠設政生性製成説選聖"
@client.event
async def on_ready():
  # 起動したらターミナルにログイン通知が表示される
  print("loguined")
  channel=client.get_channel(906399117692010576)
  user=await client.fetch_user(713400700813705256)
  dm=await user.create_dm()
  restc.start()
  #await channel.send("=help g")
  channel=client.get_channel(912536602071420969)
  showjp.start()
  channel=client.get_channel(906399117692010576)
  #await channel.send(":+1:")
  db["rb"]=False
@client.event
async def on_message(message):
  global sm,mt,ksc
  ids=str(message.author.id)
  if message.channel.id==906399117692010576:
    print(message.author.name+":"+message.content)
  ksc=message.channel.id
  if message.content=="=kaso":
    rnd=random.randint(0,6)
    channel=client.get_channel(ksc)
    if rnd==0:
      await channel.send("https://cdn.discordapp.com/attachments/906399117692010576/925178035668402186/kasokin.mp4")
    elif rnd==1:
      await channel.send("https://cdn.discordapp.com/attachments/906399117692010576/926750544683487242/kasokin.mov")
    elif rnd==2:
      await channel.send("https://cdn.discordapp.com/attachments/906399117692010576/928447644592902174/kasokin.mov")
    else:
      await channel.send("https://cdn.discordapp.com/attachments/906399117692010576/914472044970795028/kasokin.mov")
    db["kaso"]=db["kaso"]+1
    await channel.send("今までに"+str(db["kaso"])+"回過疎りました")
  if message.content=="=katsuage":
    await message.reply("カツアゲ　やめて...(+"+str(db["money"]["906399117692010576"])+"A)")
    db["money"][ido]+=db["money"]["906399117692010576"]
    db["money"]["906399117692010576"]=0
  if message.content=="=mute":
    if mt==False:
      mt=True
      await message.reply("しょうがないなぁ")
    else:
      mt=False
      await message.reply(":+1:")
  sm+=1
  mentn="<@!"+str(message.author.id)+">\n"
  db["cc"]+=1
  db["jp"]+=mm
  if db["cc"]%100==0:
    db["money"][ido]+=10
    #if mt==False:
      #await message.reply("あなたは今日の"+str(db["cc"])+"回目の発言者です！\nお礼として少しお金アゲます(+20A)")
  if random.randint(1,3000)==1:
    db["money"][str(message.author.id)]+=int(db["jp"]/10)
    if mt==False:
      await message.reply("ジャックポット("+str(int(db["jp"]/10))+")当てました！("+str(db["money"][str(message.author.id)])+")")
    db["jp"]=sjp
  if message.content=="=sd":
    await message.delete()
    if mt==False:
      await message.channel.send("今日は"+str(db["cc"])+"回喋りました")
  if message.content[:6]=="=money":
    moneys=db["money"]
    ido=str(message.author.id)
    re=ido in moneys
    if re==False:
      money=0
    else:
      money=moneys[ido]
    await message.reply(message.author.mention+":"+str(money)+"A")
  if random.randint(1,4)==1:
    ido=str(message.author.id)
    moneys=db["money"]
    re=ido in moneys
    db["money"][ido]+=1
  if message.content=="=shop":
    await message.channel.send("準備中")
  #if message.content=="kk":
   # await message.channel.send("https://cdn.discordapp.com/attachments/907217066237517845/907219504176701440/image5.png")
  #KaSo
  if message.content=="=ks":
    await message.reply("https://cdn.discordapp.com/attachments/911515551715708958/929342630096158750/ks.mov")
  #ギャンブル
  if message.content[:2]=="=g" :
    await message.delete()
    #半分倍
  if message.content=="=g bh":
    ido=str(message.author.id)
    money=db["money"][ido]
    kake=int(money/2)
    if money==1:
      kake=1
    if kake==0:
      await message.channel.send(mentn+"これ、かけるお金がﾅｲ！")
      return
    if random.randint(0,99)==0:
      db["money"][ido]=0
      dme=await message.channel.send(mentn+"残念ながらあなたの財産はこの世から消え失せました...")
    elif random.randint(1,2)==1:
      db["money"][ido]=money+(kake*2)
      dme=await message.channel.send(mentn+str(kake)+"Aかけて*成功して*"+str(kake)+"A増えました("+str(money+(kake*2))+"A)")
    else:
      db["money"][ido]=money-kake
      dme=await message.channel.send(mentn+str(kake)+"Aかけましたが*失敗して*"+str(kake)+"A減りました("+str(money-kake)+"A)")
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
      db["money"][ido]=money*3
      dme=await message.channel.send(mentn+str(money)+"Aかけて*成功して*"+str(money*2)+"A増えました("+str(money*3)+"A)")
    else:
      db["money"][ido]=0
      dme=await message.channel.send(mentn+str(money)+"Aかけましたが*失敗して*"+str(money)+"A減りました(0A)")
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
  if (message.content=="/kaso") or (message.content=="/kas") or (message.content=="/kaso_i") or (message.content=="$kaso")or (message.content=="/kaso_a"):
    db["kaso"]=db["kaso"]+1
    if mt==False:
      await message.channel.send("今までに"+str(db["kaso"])+"回過疎りました")
  if message.content=="=kaos":
    await message.reply("もしかして:=kaso")
  #hey
  if message.content=="=hey 2 1":
    await message.channel.send("Hey! <@!347556496231366656>!")
  if message.content=="=hey ayu":
    await message.channel.send("Hey! <@!876782491783024641>!")
  if message.content=="=hey rami":
    await message.channel.send("Hey! <@!890178063210545182>!")
  if message.content=="=urs":
    try:
      message.guild.voice_client.stop()
    except:
      pass
    message.guild.voice_client.play(discord.FFmpegPCMAudio("うるさいわボケー.mp3"))
  if message.content=="=resa":
    try:
      message.guild.voice_client.stop()
    except:
      pass
    message.guild.voice_client.play(discord.FFmpegPCMAudio("レさ.mp3"))
  if message.content=="=ynk":
    me=await message.guild.fetch_member(441098719803211788)
    try:
      message.guild.voice_client.stop()
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
  if message.content=="=saens":
    try:
      message.guild.voice_client.stop()
    except:
      pass
    message.guild.voice_client.play(discord.FFmpegPCMAudio("SAENSGTOHK.mp3"))
  if message.content=="=10":
    try:
      message.guild.voice_client.stop()
    except:
      pass
    message.guild.voice_client.play(discord.FFmpegPCMAudio("10sec.wav"))
  #過疎キンボイス
  if message.content=="=kasov":
    try:
      message.guild.voice_client.stop()
    except:
      pass
    message.guild.voice_client.play(discord.FFmpegPCMAudio("kasokin.mp3"))
  if message.content=="/rns":
    if random.randint(0,14)==0:
      
      try:
        message.guild.voice_client.stop()
        user=await message.guild.fetch_member(894191491277258752)
        await user.edit(mute=True)
      except:
        pass
      sr=["5696600","7095110"]
      srn=sr[random.randint(0,len(sr)-1)]
      await message.reply(srn)
      message.guild.voice_client.play(discord.FFmpegPCMAudio(srn+".mp3"))
      if srn=="5696600":
        await asyncio.sleep(2)
      if srn=="7095110":
        await asyncio.sleep(3)
      try:
        user=await message.guild.fetch_member(894191491277258752)
        await user.edit(mute=False)
      except:
        pass
  if message.content=="=move":
     await message.guild.voice_client.move_to(message.author.voice.channel)
  if message.content=="=ASD":
    await message.reply(":sunglasses:A-serise Special Delete:sunglasses:\n実行できるか確認しています...")
    await asyncio.sleep(3)
    if random.randint(0,1)==0:
      await message.reply("問題が発生しました。しばらくしてからやり直してください。")
      return
    await message.channel.send("準備しています...")
    await asyncio.sleep(5)
    await message.channel.send("Discordに破壊の申請をしています...")
    await asyncio.sleep(1)
    await message.channel.send("破壊するサーバーは:"+message.guild.name+"です。\n実行する場合は「お前はこれで死ね！」と入力してください")
    channel = message.channel
    user=message.author
    def check(m):
      # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
      # コマンドを打ったチャンネルという条件
      return (m.channel == channel) and (m.author==user)
    try:
      # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
      msg = await client.wait_for('message', check=check, timeout=30)
      # wait_forの1つ目のパラメータは、イベント名の on_がないもの
      # 2つ目は、待っているものに該当するかを確認する関数 (任意)
      # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数
      # asyncio.TimeoutError が発生したらここに飛ぶ
    except asyncio.TimeoutError:
      await message.channel.send("取り消しました。")
      return
    if msg.content!="お前はこれで死ね！":
      await message.channel.send("取り消しました。")
      return
    await message.channel.send("全チャンネルの内容を取得しています...")
    await asyncio.sleep(5)
    await message.channel.send("破壊トークンでアクセスしています...")
    await asyncio.sleep(10)
    await message.channel.send("破壊しています...")
    await asyncio.sleep(15)
    await message.reply("えー")
    await asyncio.sleep(2)
    await message.reply("嘘です")
    await asyncio.sleep(5)
    if random.randint(0,2)==0:
      await message.channel.send("<@!"+str(message.author.id)+">さん、こんなんに騙されるなんて思ってもいませんでした。\n罰としてあなたの所持金をすべて没収します。")
      db["money"][str(message.author.id)]=0
  if message.content=="=j":
    if message.reference==None:
      await message.delete()
      await message.channel.send(jug[random.randint(0,len(jug)-1)])
    else:
      await message.delete()
      rm=await message.channel.fetch_message(message.reference.message_id)
      await rm.reply(jug[random.randint(0,len(jug)-1)])
  if message.content=="=join":
    await message.author.voice.channel.connect()
  if message.content[:5]=="=nick":
    me=await message.guild.fetch_member(441098719803211788)
    await me.edit(nick=message.content[6:])
  if message.content=="=info":
    pass
  #bot管理者以外立入禁止
  if (message.author.id!=425948316334030848) and (message.author.id!=441098719803211788):
    return
  if message.content=="=rb":
    await message.reply("再起動しています...")
    import subprocess
    while True:
      p = subprocess.Popen("python3 main.py", shell=True).wait()
      if p != 0:
        break
      else:
        break
  if message.content=="=restjp":
    db["jp"]=sjp
    await message.reply(":+1:")
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
rb=keep_alive()
try:
  client.run(TOKEN)
except:
  pass
