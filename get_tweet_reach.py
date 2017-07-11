#!/usr/bin/env python3

from twitter import OAuth, Twitter
import argparse

# Keys from https://apps.twitter.com/app/<id>/keys
consumer_key = ''
consumer_secret = ''
token = ''
token_secret = ''

api = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

def find_reach(tweet_id):
    total_exposure = api.statuses.show(_id=tweet_id)['user']['followers_count']

    cursor = -1
    while (cursor != 0):
        retweeters = api.statuses.retweeters.ids(_id=tweet_id, cursor=cursor)
        for user in retweeters['ids']:
            total_exposure += api.users.show(user_id=user)['followers_count']
        cursor=retweeters['next_cursor']
    
    return total_exposure

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find the potential viewership of a tweet.')
    parser.add_argument('tweet_id', type=int, help='the tweet in question')
    args = parser.parse_args()

    print(find_reach(args.tweet_id))
