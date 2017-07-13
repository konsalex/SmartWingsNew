# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import arrow
import os,datetime
import time



def month_converter(month):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    if months.index(month) <= 8:
        return ("0"+ str(months.index(month) + 1))

    else:
        return str(months.index(month) + 1)



def calcDates(dest,dates,today,t,z):

    tod=today.format('DD-MM-YYYY')
    
    url="http://bookings.smartwings.com/en/index.php?AIRLINES=QS&PRICER_PREF=SCP2&next=1&DEP_0="+t+"&ARR_0="+z+"+&JOURNEY_TYPE=OW&FULL_DATE_0="+tod+"&FULL_DATE_1=&ADTCOUNT=4&CHDCOUNT=0&INFCOUNT=0&PROMOCODE="
            
    driver.get(url)
         
    time.sleep(15)

    try:
        error_message=driver.find_element(By.ID,'warningMessage')
        
        if error_message.is_displayed() :
        
            print "Error Found "
            
            today=today.replace(days=+3)

            calcDates(dest,dates,today,t,z)

            return (dest,dates)

    except:
        print "Continue"



    for x in xrange(0,10):

        timeout = time.time() + 30 # 30 seconds from now  Εδω κανονικά πρέπει να βάλω condition για το warning message

        while True and time.time() < timeout:
            try:
                driver.find_element(By.ID,'calendarContainer0')
                break
            except:
                continue

        time.sleep(5)

        try:
            dates_test=driver.find_elements(By.CLASS_NAME,'scpday')  ## Ελέγχω αν έχει prices at all
        except:
            continue

        d=[]
        for x in dates_test : d.append(x.text);

        for y in d:

            if ("\n") in y:

                date=str(y[0])+str(y[1])+"-"+str(month_converter(y[3:6]))+"-2017"

                if date not in dates:

                    dest.append(t+"-"+z)

                    dates.append(date)


        try:
            driver.find_element(By.CLASS_NAME,'days_r').click()
        except:
            print "Error Found "
            
            if x==0:
                today=today.replace(days=+3)

                calcDates(dest,dates,today,t,z)

                return (dest,dates)
            else:
                return (dest,dates)
            

        

        time.sleep(10)

    return (dest,dates)





driver = webdriver.Firefox()

driver.maximize_window()

wait = WebDriverWait(driver, 1300)

today=arrow.utcnow()

#From=["PRG","BRQ"]
From=["BRQ"]
TO=["RHO"]

#TO=["CFU","RHO","ZTH","KGS","HER"]

dest=[]

dates=[]

with open("AirTickets.csv", "wb") as AirTickets:

    writer=csv.writer(AirTickets)

    writer.writerows(zip(["Destination"],["Day"]))

    for t in From:

        for z in TO:
        
            if (t=="BRQ" and z=="KGS"):
                
                continue

            calcDates(dest,dates,today,t,z)
            writer.writerows(zip(dest,dates))
            del(dest[:])
            del(dates[:])
            
            

    for t in TO:
        
        for z in From:
            
            if (t=="KGS" and z=="BRQ"):
            
                continue
            
            calcDates(dest,dates,today,t,z)
            writer.writerows(zip(dest,dates))
            del(dest[:])
            del(dates[:])
            
    


driver.quit()









