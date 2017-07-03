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
    return months.index(month) + 1


### Create current day Folder ###

driver = webdriver.Firefox()

driver.maximize_window()

wait = WebDriverWait(driver, 1300)

today=arrow.utcnow().format('DD-MM-YYYY')


url="http://bookings.smartwings.com/en/index.php?AIRLINES=QS&PRICER_PREF=SCP2&next=1&DEP_0=PRG&ARR_0=RHO&JOURNEY_TYPE=OW&FULL_DATE_0="+today+"&FULL_DATE_1=&ADTCOUNT=4&CHDCOUNT=0&INFCOUNT=0&PROMOCODE="


with open("AirTickets.csv", "wb") as AirTickets:
    
    writer=csv.writer(AirTickets)

    writer.writerows(zip(["Destination"],["Day"]))

    driver.get(url)
    time.sleep(15)

    dest=[]
    dates=[]

    for x in xrange(0,4):

        try:
            dates_test=driver.find_elements(By.CLASS_NAME,'scpday')  ## Ελέγχω αν έχει prices at all
        except:
            continue

        d=[]
        for x in dates_test : d.append(x.text);

        for y in d:

            if ("\n") in y:

                date=str(y[0])+str(y[1])+"."+str(month_converter(y[3:6]))+".2017"

                if date not in dates:

                    dest.append("PR")

                    dates.append(date)

                

        driver.find_element(By.CLASS_NAME,'days_r').click()

        time.sleep(10)

    print dates





'''
        timeout = time.time() + (60*3) ## Runs for 3 minutes or 120secs

        while True:

            price=True

            warn=True

            highlighted=True

            errorTable=True
            
            try:
                driver.find_element(By.ID,'warningMessage')
            except:
                warn=False

            try:
                driver.find_element(By.CLASS_NAME,'summary')
            except:
                price=False

            try:
                driver.find_element(By.CLASS_NAME,'highlighted')
            except:
                highlighted=False

            try:
                driver.find_element(By.ID,'calendarContainer0empty2')
            except:
                errorTable=False



            if time.time() > timeout:

                driver.save_screenshot(mydir+'./Screenshots/'+departure[x]+'.png')
                                
                writer.writerows(zip(["Brno"],["Heraklion"],[departure[x]+arrival[x]],["No Availability"],["Timed Out"]))
                
                break

            if warn :

                driver.save_screenshot(mydir+'./Screenshots/'+departure[x]+'.png')

                writer.writerows(zip(["Brno"],["Heraklion"],[departure[x]+arrival[x]],["No Availability"],["Warning Message"]))

                print "Warning Message appeared"

                time.sleep(5)

                break

            if price and driver.find_element(By.CLASS_NAME,'summary').is_displayed() :

                driver.save_screenshot(mydir+'./Screenshots/'+departure[x]+'.png')

                writer.writerows(zip(["Brno"],["Heraklion"],[departure[x]+arrival[x]],["Availability"],[""]))

                print "Price is available"

                time.sleep(5)

                break

            if (errorTable and driver.find_element(By.ID,'calendarContainer0empty2').is_displayed()) :

                driver.save_screenshot(mydir+'./Screenshots/'+departure[x]+'.png')

                writer.writerows(zip(["Brno"],["Heraklion"],[departure[x]+arrival[x]],["No Availability"],["No tickets found"]))

                print "Error in one table"

                time.sleep(5)

                break

            if highlighted :

                try:

                    time.sleep(4)

                    driver.find_element(By.CLASS_NAME,'summary')

                    if driver.find_element(By.ID,'priceBoxContainer').is_displayed():

                        print "Prices Found"

                        writer.writerows(zip(["Brno"],["Heraklion"],[departure[x]+arrival[x]],["Availability"],[""]))

                        driver.save_screenshot(mydir+'./Screenshots/'+departure[x]+'.png')

                        break

                    elif(len(driver.find_elements(By.CLASS_NAME,'highlighted')==1) and (not (driver.find_element(By.ID,'loadingBox_container').is_displayed()))) :
                        
                        driver.save_screenshot(mydir+'./Screenshots/'+departure[x]+'.png')

                        writer.writerows(zip(["Brno"],["Heraklion"],[departure[x]+arrival[x]],["No Availability"],["Only one highlighted"]))

                        print "Only one highlighted 1st"

                        break

                    else:
                        continue

                except:

                    if ((driver.find_element(By.ID,'calendarContainer0empty2').is_displayed()) or (len(driver.find_elements(By.CLASS_NAME,'highlighted'))==1)) and (not (driver.find_element(By.ID,'loadingBox_container').is_displayed())) :

                        driver.save_screenshot(mydir+'./Screenshots/'+departure[x]+'.png')

                        writer.writerows(zip(["Brno"],["Heraklion"],[departure[x]+arrival[x]],["No Availability"],["Only one highlighted"]))

                        print "Only one highlighted 2nd"

                        break

                    else:
                        continue
                        
                        
driver.quit()


'''
