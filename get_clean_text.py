# -*- coding: utf-8 -*-
'''
Read text 
Clean text
Order/Prepare text
'''
import os
import re
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup

def get_text(): 
    text_file_name = os.listdir(Path('E:\\1_Py_Work\Qanda_Tweets\Transscript'))[1]
    
    transcript = Path('E:\\1_Py_Work\Qanda_Tweets\Transscript\\' + text_file_name)
    
    raw_transcript = transcript.read_text()
    
    soup_text = BeautifulSoup(raw_transcript, 'lxml')
       
    # Extracting all p attributes and writing to file 
    f = open("trial_text_0.txt", "w")
    for paragraph in soup_text.find_all('p'):
        text = paragraph.text
        print(text)
        print()
        f.writelines(text + '\n')
    f.close()
    
    # In the next block of scripts file will be:
    # Openned 
    # Cleaned
    # Writen to Data Frame 
    # Saved to .json
    
    f = open("trial_text_0.txt", "r")
    
    # Splits file into List
    split_transcript = re.split('\n', f.read())
    
    # Cleans List from all occurances of \xa0
    for i in split_transcript:
        try:
            split_transcript.remove('\xa0')
        except:
            break # ignors error at the end
    
    qa_data = {'NAME':'TONY','QandA':'speakers comment'}
    df = pd.DataFrame(qa_data, index=[1])
    
    # Count used for keeping track of multiple paragraphs per speaker, reset when new speaker is introduced 
    paragraph_count = 0               
    index = 0 
    
    # Text will be divided up into dataFrame of two columns:
    # NAME - Speakers Name
    # QandA - Speakers Question/Answer
    
    for text in split_transcript:
        # Each new NAME speaker will also create an empty tuple in QandA column
        if re.match('[A-Z]+[\s][A-Z]+',text):
            df = df.append({'NAME':text,'QandA':' '}, ignore_index=True)
            paragraph_count = 0
            index = index + 1

        # QandA text, checks all bgining attributes in speakers text 
        if re.match('[A-Z][a-z]+|[(]',text):
            df.iloc[index,1] = df.iloc[index,1] + ' ' + text
            paragraph_count = paragraph_count + 1
        
        if re.match('[A-Z]{1}[ ]|[A-Z]+[u"\u2019"]',text):
            df.iloc[index,1] = df.iloc[index,1] + ' ' + text
            paragraph_count = paragraph_count + 1
        
        if re.match('[OK]|[\.\.\.]',text):
            df.iloc[index,1] = df.iloc[index,1] + ' ' + text
            paragraph_count = paragraph_count + 1

    new_fileName = text_file_name.replace('.txt','')
    # Saving to '.json' file 
    df.to_json(r'E:\1_Py_Work\Qanda_Tweets\BeutifulSoup\df_%s.json' %new_fileName)
    
get_text()

read_df = pd.read_json('df_2019-02-11qanda.json')