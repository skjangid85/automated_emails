import yagmail
import pandas
from news import NewsFeed
import datetime
import time

df = pandas.read_excel('people.xlsx')

while True:
    if datetime.datetime.now().hour == 20 and datetime.datetime.now().minute == 4:
        for index, row in df.iterrows():
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m_%d')
            news_feed = NewsFeed(row['interest'], from_date=yesterday, to_date=today)

            email = yagmail.SMTP(user='learningpythonjangid@gmail.com', password='15698023y')
            email.send(to=row['email'],
                       subject=f'Todays news about {row["interest"]}',
                       contents=f'Hi {row["name"]} see whats on about {row["interest"]} \n {news_feed.get()} \n Sohan',
                       )

    time.sleep(60)
