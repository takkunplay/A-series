from flask import Flask
from threading import Thread
from replit import db
app = Flask("")
from markupsafe import escape
@app.route("/")
def main():
  return "ヒカキンTVでケツの穴とか言ったことあんまないけど"
@app.route('/money/<user>')
def show_user_profile(user):
    # show the user profile for that user
    try:
      money=str(db["money"][user])
    except:
      return "情報がﾅｲ!"
    return str(money)
@app.route("/login")
@app.route("/kaso")
def kaso():
    with open("kaso.html") as f:
      s = f.read()
      return s
def run():
  try:
    app.run("0.0.0.0", port=8080)
  except:
    db["rb"]=True

def keep_alive():
  try:
    t = Thread(target=run)
    t.start()
    return False
  except:
    return True
