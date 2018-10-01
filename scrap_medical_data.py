import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
url = 'https://epss.ahrq.gov/ePSS/GetResults.do?method=search&new=true'

opts = Options()
#opts.add_argument('--no-sandbox')
#opts.add_argument('headless')
browser = Chrome(chrome_options=opts)
browser.get(url)
time.sleep(10)
browser.find_element_by_id('age').send_keys('50')
sexbtn=browser.find_element_by_xpath('//*[@value="Female"]')
sexbtn.click()
sexbtn1=browser.find_element_by_xpath('//*[@name="pregnant"]')
sexbtn1.click()
#pregnantbtn=browser.find_element_by_id("pregnant").get_attribute("value") ="yes"
#pregnantbtn.click()
#tobacobtn=browser.find_element_by_id("tobacco").get_attribute("value") ="yes"
#tobacobtn.click()
#sexualyact=browser.find_element_by_id("sexuallyActive").get_attribute("value") ="yes"
#sexualyact.click()
#browser.find_element_by_id('tobacco').send_keys('')
#browser.find_element_by_id('sexuallyActive').send_keys('')
'''btn=browser.find_element_by_xpath('//*[@id="sex"]')
if btn.is_selected():
    btn.click()
btn1=browser.find_element_by_xpath('//*[@id="pregnant"]')
if btn1.is_selected():
    btn1.click()
btn2=browser.find_element_by_xpath('//*[@id="sexuallyActive"]')
if btn2.is_selected():
	btn2.click()'''
#browser.click("")
#browser.close()
#y_id('sgnBt').click()
browser.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(20)
browser.close()
#maincontent > html\:errors:nth-child(1) > form:nth-child(1) > button:nth-child(24)
#browser.find_element_by_css_selector("#maincontent > html\:errors:nth-child(1) > form:nth-child(1) > button:nth-child(24)").click()
