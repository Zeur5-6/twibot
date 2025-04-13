import tweepy
import time
import schedule
from datetime import datetime

consumer_key = "D5RPxaTdAj54IrtzpOe9LsqPF"
consumer_secret = "9lKRKJ1M2gLiPS2NNWxNXKqPK6BCfaKRJUKP3A88QYzcZ1Ab30"
access_token = "1902322099974500352-3DTHpCj1qshsCd5tLlhUROzbviDPas"
access_token_secret = "wrm2j4lPQ3FlCslhXDSmDa24gYZ5fcj0iSnPiFd8hn2VT"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Tweepy Client（v2 API 用）を使用
client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAOcn0AEAAAAAQGr%2BiLLok5bFleoPWKUpdYjdIkQ%3DLeIai7gc7rBfIie0gho7BFaGLupXvmBWYpnQvIrOTTzU5TnEiK",
    consumer_key="D5RPxaTdAj54IrtzpOe9LsqPF",
    consumer_secret="9lKRKJ1M2gLiPS2NNWxNXKqPK6BCfaKRJUKP3A88QYzcZ1Ab30",
    access_token="1902322099974500352-3DTHpCj1qshsCd5tLlhUROzbviDPas",
    access_token_secret="wrm2j4lPQ3FlCslhXDSmDa24gYZ5fcj0iSnPiFd8hn2VT"
)

def post_video():
    media = api.media_upload("C:\\Users\\user\\Documents\\キャルちゃんbot用かいかいかい.mp4")
    client.create_tweet(text="", media_ids=[media.media_id])
    print("ツイート完了")

schedule.every().day.at("04:00").do(post_video)

print("スケジュールを開始します...")
while True:
    schedule.run_pending()
    time.sleep(1)