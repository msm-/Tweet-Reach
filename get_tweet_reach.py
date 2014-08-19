import tweedle


api = tweedle.Api(consumer_key= <string>,,
consumer_secret= <string>, 
access_token_key= <string>,, 
access_token_secret= <string>,'

#tweet_id = '433357143966642176'

def find_reach(tweet_id):

    retweeters = api.GetRetweeters(tweet_id) #returns a list of retweeters
    
    
    list_of_number_of_followers_of_the_retweeters = []
    
    for user in retweeters:
        list_of_number_of_followers_of_the_retweeters.append( api.GetUser(user).AsDict()['followers_count']) #sums up the number of followers of the retweeters
    
    total_exposure = sum(list_of_number_of_followers_of_the_retweeters) + api.GetStatus(tweet_id).GetUser().AsDict()['followers_count'] #adds the sum of the followers of all the retweeters to the number of followers of the original tweeter
    
    return total_exposure

print find_reach('433357143966642176')

