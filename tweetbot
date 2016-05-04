from twython import Twython, TwythonError

CONSUMER_KEY = 'ZrzxuMQNKKHTKGWgPWQYnVAK1'
CONSUMER_SECRET = 'zKBHnHgtQKR13BoyyW99sCtuod6LaaQHrngr6WUSFeIYxa44kl'
ACCESS_TOKEN = '722880563636412416-f3s7lR4tA5h6pC8oTTDgsrHReQLc7Yl'
ACCESS_TOKEN_SECRET = '9ObrwG6GbBj8b3xhd1iSBRTrxW6OP2Vr1KsVKQtqMhh2W'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print e
    
    # read from csv