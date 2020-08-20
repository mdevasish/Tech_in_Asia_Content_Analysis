# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:26:14 2020

@author: mdevasish
"""
import pandas as pd
import requests
import time
from pandas import json_normalize
from datetime import datetime
import re

def clean_content(text):
    '''
    Function to clean the html tags from the content columns
    
    Parameters :
        
        text : Content to be cleaned
    
    Returns text free from html tags
    '''
    
    cleaner = re.compile('<.*?>')
    return re.sub(cleaner, ' ',text)

def replace_illegal_chars(text):
    '''
    Function to replace illegal characters
    
    Parameters :
        
        text : Content to be cleaned
    
    Returns text free from illegal characters
    '''
    return text.replace("â€™","'")

def extract_from_posts(url,headers,nap = 30,total_pages = 30):
    '''
    Function to extract the data and store it in a pandas data frame with the below parameters.
    
    Parameters:
        
        url : API of the required data
        headers : Configuration settings of the Browser to extract the data
        nap : Amount of time for the function to remain inactive. Used here to control the agressiveness of the API calls. Default value is 30 seconds.
    
    Writes a dataframe to the disk and returns a boolean
    '''
    
    # Create an empty data frame to hold the extracted data.
    posts_frame = pd.DataFrame(columns = ['id','title','content','excerpt','comments_count','read_time','author.display_name'])
    
    # Making the first request to get the number of total pages and remain inactive for 30 seconds.
    print(datetime.now(),'-->First hit')
    
    # Loop over the total_pages, extract the required data 
    for i in range(total_pages):
        r = requests.get(url+str(i+1),headers=headers)
        if r.status_code == 400:
            print(datetime.now(),'-->Iteration in error: ',i)
            time.sleep(nap)
            
        elif r.status_code == 200:
            print(datetime.now(),'-->Iteration in success: ',i)
            html = r.json()['posts']
            frame = json_normalize(html)
            frame = frame[['id','title','content','excerpt','comments_count','read_time','author.display_name']]
            posts_frame = pd.concat([posts_frame,frame],ignore_index = True,axis = 'index')
                
    print('Data shape is ',posts_frame.shape)
    posts_frame.drop_duplicates(inplace = True)
    print('Data shape after dropping duplicates is ',posts_frame.shape)
    
    # Clean the content column of the posts_frame and store the data in the required dataframe    
    posts_frame['content'] = posts_frame['content'].apply(lambda x: clean_content(x))
    posts_frame['content'] = posts_frame['content'].apply(lambda x: replace_illegal_chars(x))
    posts_frame['title'] = posts_frame['title'].apply(lambda x: replace_illegal_chars(x))
    posts_frame['excerpt'] = posts_frame['excerpt'].apply(lambda x: replace_illegal_chars(x))
    
    posts_frame.to_csv('./Data/posts.csv',index = False)
    print('Posts writing completed successfully')
    return True

def extract_comments(url,file,headers,nap=30):
    '''
        Function to extract the comments of the posts and store it in a pandas data frame with the below parameters.
        
        Parameters:
            
            url : API of the required data
            file : Location of the posts.csv
            headers : Configuration settings of the Browser to extract the data
            nap : Amount of time for the function to remain inactive. Used here to control the agressiveness of the API calls. Default value is 30 seconds.
        
        Extracts comments into a dataframe and saves it to the disk
    '''
    print('Extracting Comments start')
    comments_frame = pd.DataFrame(columns = ['id','excerpt'])
    df = pd.read_csv(file,usecols = ['id','comments_count'])
    df = df[df['comments_count']>0]
    idx = list(set(df['id']))
        
    for i,each in enumerate(idx):
        
        r = requests.get(comments_url.format(id = str(each)),headers = headers)
        if r.status_code == 400:
            print(datetime.now(),'-->Iteration in error: ',i,' ,id = ',each)
            time.sleep(nap)
                    
        elif r.status_code == 200:
            print(datetime.now(),'-->Iteration in success: ',i,' ,id = ',each)
            comments = json_normalize(r.json()['comments'])
            comments = comments[['id','excerpt']]
            comments_frame = pd.concat([comments_frame,comments],ignore_index = True,axis = 'index')
        
    print('Data shape is ',comments_frame.shape)
    comments_frame.drop_duplicates(inplace = True)
    print('Data shape after dropping duplicates is ',comments_frame.shape)
    comments_frame.to_csv('./Data/comments.csv',index = False)
    print('Comments writing completed successfully')
    return True

if __name__ == '__main__':
    posts_url = 'https://www.techinasia.com/wp-json/techinasia/2.0/posts?page='
    comments_url = 'https://www.techinasia.com/wp-json/techinasia/2.0/posts/{id}/comments'
    jobs_url = 'https://www.techinasia.com/api/2.0/job-postings'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    file = './Data/posts.csv'
    
    if extract_from_posts(posts_url,headers):
        print('Posts extracted and job exited successfully')
    else:
        print('Please debug the code')
    
    if extract_comments(comments_url,file,headers):
        print('Comments extracted and job exited successfully')
    else:
        print('Please debug the code')
