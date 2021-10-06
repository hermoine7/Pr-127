from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

lin="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome(r'C:Users\Dell\AppData\Local\Temp\Temp1_chromedriver_win32\to\chromedriver\chromedriver.exe')
browser.get(lin)
time.sleep(10)

def scrape():
    headers=["Name", "Distance", "Mass", "Radius"]
    starData=[]
    for i in range(0-428):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for s in soup.find_all("tr"):
            td=s.find_all("td")
            temli=[]
            for index,l in  enumerate(td):
                if(index == 0):
                    temli.append(l.find_all("a")[0].contents[0])
                else:
                    try:
                        temli.append(l.contents[0])
                    except:
                        temli.append("")
            starData.append(temli)

scrape()