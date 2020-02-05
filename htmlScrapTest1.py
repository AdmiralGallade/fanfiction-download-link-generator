#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

#%matplotlib inline
import os
from os import path
from urllib.request import urlopen

#from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

#url = "http://www.fanfiction.net/u/1634629/Crukix" //Issue with custom font, will search for ways around
=======
#url = "http://www.fanfiction.net/u/1634629/Crukix"
url="https://www.fanfiction.net/u/8877203/KyKyuKai"
html = urlopen(url)




#url="https://www.fanfiction.net/u/2293605/Little-Miss-Firebright"
#html = urlopen(url)
soup = BeautifulSoup(html,"lxml")
type(soup)
#print(soup.prettify()) //test to see if the program is error free
title = soup.title
print(title) #prints the name of the webpage i.e the author name


rows = soup.find_all('tr')

all_links = soup.find_all("a",class_="stitle")
i=0

if str(path.isfile("stories.txt"))=="false":
    print("Everything ok")
else:
    if os.path.exists("stories.txt"):     
        print("Oh no")
        os.remove("stories.txt")
        print("Nvm, problem solved :D")

#for rows in  rows:
 #   text= soup.find_all(class_="z-list favstories")[1].get_text()
 #   print(text)
  
  
#if str(path.isfile("stories.txt"))=="true":
 #   print("duplicate found")


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
  
  
