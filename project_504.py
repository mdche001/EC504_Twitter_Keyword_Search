# -*- coding: utf-8 -*-

import os
import csv
import random
import time
import matplotlib.pyplot as plt

def key_word_num_in_tweet(tweet,key_word_hashmap):
    res=0
    tweet_word_lis=tweet.split(' ')
    for word in tweet_word_lis:
        if word in key_word_hashmap:
            res+=1
    return res

def key_word_search(tweets,query,res_num=5):
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
    res=[(s.lower())[0:-1] for s in f.readlines()]
    f.close()
    return res

def read_csv_dataset(filename):
    csv_reader = csv.reader(open(filename,'r'))
    res=[]
    for row in csv_reader:
        res.append(': '.join(row[0:2]))
    return res[1:]
    
def print_tweets(tweets,tweet_num=5,with_semicol=True):
    if tweet_num<=len(tweets):
        for i in range(tweet_num):
            if with_semicol:
                print(i,":",tweets[i])
            else:
                print(tweets[i])
        print(" ")
    else:
        for i in range(len(tweets)):
            if with_semicol:
                print(i,":",tweets[i])
            else:
                print(tweets[i])
        print(" ")

def keyword_hashmap(q):
    word_lis=q.split(' ')
    res={}
    for word in word_lis:
        res[word]=1
    return res

def runtime_analysis(dataset):
    dataset_len_lis=list(range(100,500000,8000))
    runtime_lis=[]
    for dataset_len in dataset_len_lis:
        word_lis=[]
        while len(word_lis)<5:
            rand_tweet=random.choice(dataset)
            word_lis=rand_tweet.split(' ')
        
        rand_query=' '.join(random.sample(word_lis,5))
        part_dataset=random.sample(dataset,dataset_len)
        start_time=time.time()
        key_word_search(part_dataset,rand_query,res_num=10)
        end_time=time.time()
        runtime_lis.append(end_time-start_time)
    plt.figure()
    plt.plot(dataset_len_lis,runtime_lis)
    plt.xlabel("Dataset scale",fontsize = 25)
    plt.ylabel("Running time",fontsize = 25)
    plt.title("Key word searching",fontsize = 25)
    plt.show()
    
        
def main():
    print("Reading tweets in file...........\n")
    tweets=read_dataset('sample_win.txt')
    print_tweets(tweets);
    
    q='suffer'
    search_res=key_word_search(tweets,q)
    print("\nSearch results\n")
    print_tweets(search_res)
      
    csv_file_name = 'abcnews-date-text.csv'
    csv_dataset=read_csv_dataset(csv_file_name)
    print(len(csv_dataset))
        
    res_len=20
    
    q='vaile hopes for us free'
    print("Query: ",q)
    search_res1=key_word_search(csv_dataset,q,res_len)
    print("\nSearch results\n")
    print_tweets(search_res1,res_len,with_semicol=False)
    
    runtime_analysis(csv_dataset)

if __name__=="__main__":
    main()







