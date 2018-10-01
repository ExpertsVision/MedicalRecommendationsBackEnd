from bs4 import BeautifulSoup
import requests
import urllib
from urlparse import urljoin
from urlparse import urlparse
import re
import time
import logging
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
logger = logging.getLogger(__name__)
import pandas as pd
import csv
#my_url="https://www.aldoshoes.com/us/en_US/women/outlet/footwear/sandals/Croreni-Natural/p/56839067-35"
#my_url="https://www.uspreventiveservicestaskforce.org/Page/Document/UpdateSummaryFinal/bladder-cancer-in-adults-screening#recommendations"
#my_url="https://www.aldoshoes.com/us/en_US/Brandli-Pink%2FPurple/p/50857387-56"

#my_url="https://www.aldoshoes.com/us/en_US/men/bags-%26-accessories/watches/Colles-Brown/p/53634330-20"
df=pd.read_csv("general_recommendation.csv")
urls=df["otherUrl"]
i=0
for row in urls:
	print row
	try:
		options=Options()
		options.add_argument('--user-agent= Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')
		browser = Chrome(chrome_options=options)
		browser.get(row)
		time.sleep(10)
		#soup1=BeautifulSoup(browser.page_source, 'lxml')
		title=browser.title
		print(title)
		#recom_url=urljoin("https://www.uspreventiveservicestaskforce.org/",soup1.find("div",{"class":"recButtonInnards"}).find("a")["href"])
		#print recom_url
		#browser.get(recom_url)
		#print browser.title.text
		try:
			discussin_list=[]
			browser.find_element_by_xpath('//*[@id="centerContent"]/div[1]/div[4]/div[1]/div/div/a').click()
			soup1=BeautifulSoup(browser.page_source, 'lxml')
			discussion=soup1.findAll("div",{"class":"col100"})
			#for p in discussion[7].findAll("p"):
			#print discussion
			discus=discussion[7].find("div",{"class":"podBody"})
			discussin_list.append(str(discus.encode(encoding='UTF-8')).strip())
			df["otherUrl"][i]=discussin_list
			print(discus)
			print(df['id'][i])
		except:
			discussin_list=[]
			soup1=BeautifulSoup(browser.page_source, 'lxml')
			discussion=soup1.findAll("div",{"class":"col100"})
			#for p in discussion[7].findAll("p"):
			#print discussion
			discus=discussion[7].find("div",{"class":"podBody"})
			discussin_list.append(str(discus.encode(encoding='UTF-8')).strip())
			df["otherUrl"][i]=discussin_list
			print(discus)
			print(df['id'][i])
			#print(p.find("h3").text)
			#print (p.text)
	except:
		pass
	i+=1
	print i
df.to_csv("discussion_with_htmltags_data.csv")
#print("new data")
browser.close()