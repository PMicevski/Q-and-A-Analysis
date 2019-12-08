# -*- coding: utf-8 -*-
"""
Url's are saved in txt file
Each url consits of a date, 
Date is exctracted and used as part of new file name for extracted data
"""

from requests import get
import re

url = open('qanda_transscript_https_addr.txt', 'r')

for line in url:
    
    # extracting date form url to use in file name
    extract_date = re.findall('[0-9]+[-][0-9]+[-][0-9]+', line)
    extract_date = re.sub('\'','',str(extract_date ))
    extract_date = re.sub('\[','', str(extract_date ))
    extract_date = re.sub('\]','', str(extract_date ))
    print(extract_date)
    
    # scraping text from web site and writing to file
    scraped_text = get(line)
    wf = open('%sqanda.txt' %extract_date, 'w')
    wf.write(scraped_text.text)
    wf.close()
    print(line)
    
url.close()

