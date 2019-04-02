import urllib, json
import pandas 
import csv
url = "https://epssdata.ahrq.gov/?key=6c2efa05afbe47af3fcd802f45c1b258"
response = urllib.urlopen(url)
data = json.loads(response.read())
df=pandas.read_json(data)
data.to_csv('tools.csv')
tools=[]
tools.append(data['tools'])
#print tools
#for tool in tools:
	#print("*************")
	#print tool