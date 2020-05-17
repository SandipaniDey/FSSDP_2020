from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup as BS
import requests

url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("C://Users/SAMD/chromedriver.exe")
browser.get(url)

html = browser.page_source
s = BS(html,"lxml")

right_table=browser.find_element_by_xpath('//*[@id="exTab2"]/div[1]/div[1]/div/div[1]/div/ul/li[1]/a')
sleep(10)


A=[]
B=[]
C=[] 
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]

for i in range(1,11):
    bid = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text.replace("\n"," ")
    A.append(bid)
    
    items = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text.replace("\n"," ")
    B.append(bid)
    
    Quan = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text.replace("\n"," ")
    C.append(bid)
    
    Dept = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text.replace("\n"," ")
    D.append(bid)
    
    Sdate = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[:10]
    E.append(bid)
    
    Stime = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[11:]
    F.append(bid)
    
    Edate = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[:10]
    G.append(bid)
    
    Etime = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[11:]
    H.append(bid)
    
    Pdfname = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    I.append(bid)
   
import pandas as pd
df = pd.DataFrame()
df["BID NO"]=A
df["items"]=B
df["Quantity Required"]=C
df["Department Name And Address"]=D
df["Start Date"]=E 
df["Start Time"]=F
df["End Date"]=G
df["End Time"]=H
df["PDF Name"]=I

df.to_csv("bid_plus.csv", index=False)




browser.quit()