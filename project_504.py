# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:32:02 2019

@author: zephyrus
"""

import os

def key_word_num_in_tweet(tweet,key_word_hashmap):
    res=0
    tweet_word_lis=tweet.split(' ')
    for word in tweet_word_lis:
        if word in key_word_hashmap:
            res+=1
    return res

def key_word_search(query,res_num=5):
    # by default querie is a string
    key_word_lis=(query.lower()).split(' ')
    key_word_hash_map={}
    for word in key_word_lis:
        key_word_hash_map[word]=1
    tweet_key_word_freq_map={}
    for tweet in tweets:
        tweet_key_word_freq_map[tweet]=key_word_num_in_tweet(tweet,key_word_hash_map)
    sorted_map=sorted(tweet_key_word_freq_map.items(),key=lambda item:item[1],reverse=True)
    if res_num<=len(tweets):
        return [item[0] for item in sorted_map[0:res_num]]
    else:
        return [item[0] for item in sorted_map]
    
def read_dataset(file_name):
    file_path=os.getcwd()+os.sep+file_name
    f=open(file_path,'r')
    res=[s.lower() for s in f.readlines()]
    f.close()
    return res

def print_tweets(tweets,tweet_num=5):
    if tweet_num<=len(tweets):
        for i in range(tweet_num):
            print(i,":",tweets[i])
    else:
        for i in range(len(tweets)):
            print(i,':',tweets[i])

def keyword_hashmap(q):
    word_lis=q.split(' ')
    res={}
    for word in word_lis:
        res[word]=1
    return res

print("reading tweets in file")
tweets=read_dataset('sample_win.txt')
print("show partial tweets from dataset")
print_tweets(tweets);

q='suffer'
search_res=key_word_search(q)
print("search results")
print_tweets(search_res)

#print_tweets(tweets)
#q='app usage'
#key_word_map=keyword_hashmap(q)
#for t in tweets:
#    print(t,key_word_num_in_tweet(t,key_word_map))





































































