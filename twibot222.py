import tweepy
import time
import schedule
from datetime import datetime
from flask import Flask
from threading import Thread
import os
import datetime

def hourly_check():
    now = datetime.datetime.utcnow()
    print(f"[LOG] 現在時刻(UTC): {now.strftime('%Y-%m-%d %H:%M:%S')}")
    if now.hour == 19 and now.minute == 0:
        print("[LOG] 19:00に一致！投稿開始します")
        post_video()


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
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    try:
        print(f"[LOG] [{now}] 投稿処理を開始します")
        if os.path.exists("kaikaikai.mp4"):
            print(f"[LOG] [{now}] 動画ファイルが存在しました。アップロードを開始します")
            media = api.media_upload("kaikaikai.mp4")
            print(f"[LOG] [{now}] メディアアップロード成功、ツイートを送信します")
            client.create_tweet(text="", media_ids=[media.media_id])
            print(f"[LOG] [{now}] ✅ ツイート完了！")
        else:
            print(f"[LOG] [{now}] ❌ 動画ファイルが見つかりませんでした")
    except Exception as e:
        print(f"[LOG] [{now}] ❌ 投稿中にエラー発生: {e}")

# スケジュール登録
schedule.every().minute.do(hourly_check)

print("スケジュールを開始します...")

#post_video()

while True:
    schedule.run_pending()
    time.sleep(1)


