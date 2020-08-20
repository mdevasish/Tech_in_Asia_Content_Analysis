# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:22:08 2020

@author: mdevasish
"""

import pandas as pd
import spacy

nlp = spacy.load('en_core_web_sm')

def ner_spacy(nlp,file_name):
    '''
    Function to extract Named entities from the articles
    
    Parameters:
        nlp : Pretrained model from Spacy
        file_name : Name of the file containing the articles
    
    Returns a dataframe with named entities
    '''
    posts_df = pd.read_csv(file_name,usecols = ['id','content'])
    posts = list(posts_df['content'])
    ids = list(posts_df['id'])
    
    org = []
    loc = []
    for each in posts:
        doc = nlp(each)
        locs = []
        orgs = []
        for ent in doc.ents:
            if ent.text.isalpha():                
                if ent.label_ in ['GPE','LOC']:
                    locs.append(ent.text.strip(''))
                    locs = list(set(locs))
                elif ent.label_ == 'ORG':
                    orgs.append(ent.text.strip(''))
                    orgs = list(set(orgs))
        org.append(orgs)
        loc.append(locs)
    return pd.DataFrame(list(zip(ids,org,loc)),columns = ['id','Organisations','Locations'])


if __name__ == '__main__':
   
    ner = ner_spacy(nlp,'./Data/posts.csv')
    ner.to_csv('./Results/NER.csv',index = False)
    posts = pd.read_csv('./Models/BOW/BOW_Topic_Modelling.csv',usecols = ['id','title','content','author.display_name','comments_count','read_time','tokens','Topic_Mixture'])
    posts = posts.merge(ner, on = 'id', how = 'inner')
    posts = posts[['id','title','content','author.display_name','comments_count','read_time','Topic_Mixture','Organisations','Locations']]
    posts.to_csv('./Results/final.csv',index = False)
    
    
