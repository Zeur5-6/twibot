import tweepy
import time
import schedule
from datetime import datetime
from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# スレッドでFlask起動
Thread(target=run_flask).start()

# Twitter API認証
consumer_key = "D5RPxaTdAj54IrtzpOe9LsqPF"
consumer_secret = "9lKRKJ1M2gLiPS2NNWxNXKqPK6BCfaKRJUKP3A88QYzcZ1Ab30"
access_token = "1902322099974500352-3DTHpCj1qshsCd5tLlhUROzbviDPas"
access_token_secret = "wrm2j4lPQ3FlCslhXDSmDa24gYZ5fcj0iSnPiFd8hn2VT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAOcn0AEAAAAAQGr%2BiLLok5bFleoPWKUpdYjdIkQ%3DLeIai7gc7rBfIie0gho7BFaGLupXvmBWYpnQvIrOTTzU5TnEiK",
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def post_video():
    if os.path.exists("kaikaikai.mp4"):
        media = api.media_upload("kaikaikai.mp4")
        client.create_tweet(text="", media_ids=[media.media_id])
        print("ツイート完了")
    else:
        print("動画ファイルが見つかりませんでした")

# スケジュール登録
schedule.every().day.at("19:00").do(post_video)

print("スケジュールを開始します...")

post_video()

while True:
    schedule.run_pending()
    time.sleep(1)


