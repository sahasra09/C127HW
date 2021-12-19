from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser=webdriver.Chrome('chromedriver')
browser.get(START_URL)
time.sleep(10)
page=requests.get(START_URL,verify=False)
def scrape():
    headers=['V Mag. (mV)','Proper name','Bayer designation','Distance (ly)','Spectral class','Mass (M☉)','Radius (R☉)','Luminosity (L☉)']
    planets_data=[]
    for i in range(0,1):
        soup=BeautifulSoup(browser.page_source,'html.parser')
        for table_tag in soup.find('table'):
            tr_tags=table_tag.find('tr')
            temp_list=[]
            for index,tr_tag in tr_tags:
                if index==0:
                    temp_list.append(tr_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append('')
            planets_data.append(temp_list)
        
    with open('scrappers.csv','w') as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planets_data)
scrape()