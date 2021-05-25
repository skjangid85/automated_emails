# Api Key: 890603a55bfa47048e4490069ebee18c
import requests
from pprint import pprint


class NewsFeed:
    """Represents the data required for newsfeed from the newsapi.com"""
    base_url = 'https://newsapi.org/v2/everything?'
    api_key = '890603a55bfa47048e4490069ebee18c'

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              f'apiKey={self.api_key}'
        r = requests.get(url)
        data = r.json()
        articles = data['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

if __name__ == '__main__':
    news_feed = NewsFeed('meditation', '2021-05-21', '2021-05-20', 'en')
    print(news_feed.get())