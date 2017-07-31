# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv
import arrow
import os,datetime
import time


f=open('dateDest.csv')

lines=f.readlines()

f.close()

Dest=[]
Start=[]
End=[]
for z in lines[1:]:
    Dest.append(z.split(",")[0])
    Start.append(z.split(",")[1])
    End.append(z.split(",")[2])

driver = webdriver.Firefox()

driver.maximize_window()

wait = WebDriverWait(driver, 1300)

####   Logging to Web-API   ####

driver.get("http://electratours.orangecay.com:9001/user/login.html")

driver.find_element(By.ID,'login-form-login').send_keys("webco")

driver.find_element(By.ID,'login-form-password').send_keys("v@s1l1s")

driver.find_element(By.CSS_SELECTOR,'.btn').click()

time.sleep(7)

driver.get("http://electratours.orangecay.com:9001/destination/index.html")

time.sleep(2)



table_rows=len(driver.find_elements_by_css_selector(".kv-grid-table > tbody:nth-child(2) > tr"))

for i in xrange(0,table_rows) :

    try :
        ### Find if airport is SKG and ignore it ###

        if driver.find_element_by_css_selector(".kv-grid-table > tbody:nth-child(2) > tr:nth-child("+str(i+1)+") >td:nth-child(12)").text=="SKG":
            
            continue
    except:

        break

    desti=driver.find_element_by_css_selector(".kv-grid-table > tbody:nth-child(2) > tr:nth-child("+str(i+1)+") >td:nth-child(11)").text

    arri=driver.find_element_by_css_selector(".kv-grid-table > tbody:nth-child(2) > tr:nth-child("+str(i+1)+") >td:nth-child(12)").text

    driver.find_element_by_css_selector(".kv-grid-table > tbody:nth-child(2) > tr:nth-child("+str(i+1)+") >td:nth-child(16) > a:nth-child(1)").click()

    time.sleep(5)


    ### Here it is inside specific destination page ###

    table=driver.find_element_by_css_selector("#delete-destination-periods-form > table:nth-child(2)")

    rows=table.find_elements_by_css_selector("tr")

    for x in rows[1:] :

        dep=x.find_element_by_css_selector("td:nth-child(1)").text

        arr=x.find_element_by_css_selector("td:nth-child(2)").text

        found=False

        for i in xrange(0,len(Dest)):


            if (Dest[i].split("-")[0]==desti and Dest[i].split("-")[1]==arri and dep.strip()==Start[i].strip() and arr.strip()==End[i].strip()): 

                found=True
                
                break


            ### If there will be at least one match loop for this date will end, if none match then it will be clicked the delete button ##
        if not found :
            x.find_element_by_css_selector("td> label:nth-child(1)>input:nth-child(1)").click()



        driver.find_element_by_css_selector("button.btn:nth-child(3)").click()

        time.sleep(4)



        

driver.get("http://electratours.orangecay.com:9001/destination/index.html")

time.sleep(4)




















