from twython import Twython
import csv

CONSUMER_KEY = 'ZrzxuMQNKKHTKGWgPWQYnVAK1'
CONSUMER_SECRET = 'zKBHnHgtQKR13BoyyW99sCtuod6LaaQHrngr6WUSFeIYxa44kl'
ACCESS_TOKEN = '722880563636412416-f3s7lR4tA5h6pC8oTTDgsrHReQLc7Yl'
ACCESS_TOKEN_SECRET = '9ObrwG6GbBj8b3xhd1iSBRTrxW6OP2Vr1KsVKQtqMhh2W'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='danielle', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)

#Open the CSV file. 'data.csv' can be renamed to whatever you would like. This is the filename it will save under.

    a.writerow(('Search Term', 'Tweet Text', 'URL'))

#At the top of the CSV file, we want to add in a row with columns labeled 'Search Term' and 'Tweet Text'.

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['danielle', result['text'].encode('utf-8'), url]]
        a.writerows((text))