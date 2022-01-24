from flask import Flask, redirect, request
from flask import json as json_flask
from threading import Thread
import requests
import json
import configparser
import os
from replit import db
app = Flask("")
from markupsafe import escape
BASE_URL = 'https://discordapp.com/api/'
scope="identify"
authorize_params = {
            'response_type': 'code',
            'scope': scope,
            'client_id': "441098719803211788",
            'redirect_uri': "https://A-series.obktvjobk-dtv.repl.co/callback"
        }
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
@app.route("/help")
def msg():
    with open("help.htm") as f:
      s = f.read()
      return s
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
@app.route('/mm')
def minsay():
    return str(db["mm"])
def exchange_code(code):
    data = {
        'client_id': "441098719803211788",
        'client_secret': os.environ['cliant_secret'],
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': "https://A-series.obktvjobk-dtv.repl.co/callback",
        'scope': '%20'.join(scope)
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('https://discordapp.com/api/oauth2/token', data=data, headers=headers)
    print(data)
    r.raise_for_status()
    return r.json()

@app.route('/login')
def login():
    res_authorize = requests.get(BASE_URL + 'oauth2/authorize', params=authorize_params)
    return redirect(res_authorize.url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    res_token = exchange_code(code)
    token = res_token['access_token']
    print('token:', res_token['access_token'])
    print('expires_in:', res_token['expires_in'])
    return redirect(f'/me?token={token}')

@app.route('/me')
def me():
    token = request.args.get('token')
    res_me = requests.get(BASE_URL + 'users/@me', headers={ 'Authorization': f'Bearer {token}' })
    return res_me.content
def keep_alive():
    t = Thread(target=run)
    t.start()
