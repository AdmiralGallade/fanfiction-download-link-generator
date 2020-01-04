
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

#%matplotlib inline

#from urllib.request import urlopen

#from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

#url = "http://www.fanfiction.net/u/1634629/Crukix"
url="https://www.fanfiction.net/u/12219229/MissBraixen"
html = urlopen(url)



soup = BeautifulSoup(html,"lxml")




type(soup)
#print(soup.prettify())
title = soup.title
print(title)


rows = soup.find_all('tr')

all_links = soup.find_all("a",class_="stitle")
i=0


f = open('stories.txt','w')


for link in all_links:
    f.write("https://www.fanfiction.net"+link.get("href"))
    print("https://www.fanfiction.net"+link.get("href"))  
    f.write("\n")
    i+=1
print(i)
f.close()

rows = soup.find_all(class_="z-list favstories")


#print(rows[:10])
#for rows in  rows:
 # text= soup.find_all(class_="z-list mystories")[1].get_text()
  #print(text)
  
  