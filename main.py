import tweepy
#import time
import random
#import csv
from datetime import datetime

# API KEY
CK = "6aAk891BBcmRCy91ncphVCDFf"
CS = "4c5uRz8fw79bjjMvhKiwMHdeAW2VomxTuioAibmSuYQui75oub"
AT = "1406435825244540928-0VJfWRmfpyFgzmPuNjyP8lYRx6SQgj"
AS = "S9GNwGkKol9k8BuAa5sIf5QV6LpndxoPeFcRS5TPUhG7q"
BT = "AAAAAAAAAAAAAAAAAAAAAI32WwEAAAAAPp9sDKXRP8R9bZ%2BMohWdL0qt3G4%3D70qhXKrWFeucTQ6wPSxWkk2qmFsROGEDwEDxGUMbVm4GOZQUi9"

#tweepyの設定
client = tweepy.Client(BT, CK, CS, AT, AS)


#２）あるキーワードで検索したユーザを指定の件数フォローする



# today = datetime.date.today()
# print(f'{today:%-m月%-d日}')

time_now = datetime.now()
month = time_now.strftime("%m").lstrip("0")
day = time_now.strftime("%d").lstrip("0")

date = "【" + month + "月" + day + "日" +"】"
date_num = month + "/" + day
animal = ["🐷", "🐮", "🐭", "🐻", "🐼", "🐔", "🐵", "🐶"]
aisatsu = "おはようございます" + random.choice(animal)

Start_weight = 59.6
todays_weight = 58 - 1 * random.random()
diference_weight = todays_weight - Start_weight
weight_text = "⭐体重" + str(round(todays_weight, 1)) + "kg"
bmi = round(todays_weight, 1) / (1.57*1.57)
bmi_text = "⭐BMI:"+ str(round(bmi, 1))
# print("✅体重" + str(round(weight, 1)) + "kg")
# print("✅BMI:"+ str(round(bmi, 1)))

# with open("weight_list", mode="r", encoding="utf-8") as f:
#     last_weight = f.readlines()[-1].split(",")

# count = int(last_weight[0]) + 1
# count_text = "🌷 ダイエット開始から" + str(count) + "日目🌷 "
# print(last_weight[1])

# difference = float(last_weight[1]) - round(weight,1)

# if difference > 0:
#     difference_text = "⭐昨日からの増減" +":" + "+" + str(round(difference, 1)) + "kg"

# else:
#     difference_text = "⭐昨日からの増減" +":" + str(round(difference, 1)) + "kg"

# with open("weight_list", mode="a", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow([count,round(weight, 1)])

start_day = datetime(year=2022, month=2, day=11)
count_days = time_now - start_day
count_text = "🌷ダイエット開始から" + str(count_days.days) + "日目🌷 "

difference_text = "⭐ダイエット開始時からの増減" +":"  + str(round(diference_weight, 1)) + "kg"

text = count_text + "\n" + aisatsu + "\n" + "\n" + date + "\n" + weight_text + "\n" + bmi_text + "\n" + difference_text + "\n" + "\n" + "#ダイエット垢さんと繋がりたい"
print(text)


# client.create_tweet(text=text)

# # 検索キーワード
# keyword = "#ダイエット垢さんと繋がりたい -is:retweet -is:reply"

# # フォロー数
# follow_cnt = 0

# # 現在のフォローリストを作成
# follow_list = client.get_users_following(id="1406435825244540928",max_results=400)
# follow_lists = []

# for follow in follow_list[0]:
#     follow_lists.append(follow.id)



# s_count = 50
# results = client.search_recent_tweets(query=keyword, max_results=s_count, user_fields = "name", expansions=["author_id","referenced_tweets.id"],)

# for result in results.data: 
#     print(result.author_id)
#     # print(result.referenced_tweets)


# for result in results.data: 
#     client.like(tweet_id=result.id)
# #フォローリストにこのツイート主がいなければフォローする。
#     if result.author_id not in follow_lists:
#         client.follow_user(result.author_id)
#         print(result.author_id)
# #61秒停止する
#         time.sleep(61)