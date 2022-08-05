import re

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#import nltk
#nltk.download('punkt')
#nltk.download('stopwords')

def topic_2_tokens(topic):
    # Only use 1st sentence
    sent = sent_tokenize(topic)[0]
    
    # 00-year-old -> 00 year old
    tokens = word_tokenize(sent.replace('-',' '))
    
    # stopwords contain "m", so remove this
    stop_words = set(stopwords.words('english'))
    stop_words.remove('m')
    stopped_tokens = []
    
    for w in tokens:
        w = w.lower()
        if w not in stop_words: 
            stopped_tokens.append(w)
            
    return stopped_tokens
    

def get_genders(topics):
    
    gender_query = []
    
    for t in topics:
        tokens = topic_2_tokens(t)
        
        male_likes = ['man','male','m','gentleman','boy']
        female_likes = ['woman','female','f','girl']

        for g in tokens:
            if g in male_likes:
                gender = 'Male'
                break
            elif g in female_likes:
                gender = 'Female'
                break
            else:
                m_rxp = re.findall(r'[0-9]+m',g)
                w_rxp = re.findall(r'[0-9]+w',g)
                if m_rxp:
                    gender = 'Male'
                    break
                elif w_rxp:
                    gender = 'Female'
                    break 
                gender = 'N/A'
                
        gender_query.append(gender)
    
    return gender_query

def get_years(topics):
    
    year_query = []
    
    for t in topics:
        tokens = topic_2_tokens(t)
        
        year = 'N/A'
        # Find the first numeric string, so it reversed
        for w in reversed(tokens):
            y = re.sub(r'[^0-9]+', '', w)
            if y != '':
                year = y
        
        if ('months' in tokens[0:7] and 'old' in tokens[0:7]):
            month = year
            year = int(month)//12
        
        if ('day' in tokens[0:7] and 'old' in tokens[0:7]):
            day = year
            year = 0
                
        year_query.append(year)
    
    return year_query