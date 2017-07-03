# -*- coding: UTF-8 -*-
import sys
import glob, os
import arrow




reload(sys)
sys.setdefaultencoding("utf8")


print ("Checking Dates for flights. Choose Destinations")

while(True):
    
    print ("From: \n1)Praha \n2)Brno")
    
    k=raw_input('Press Selection Number:')
    
    if (int(k)>(2) or int(k)<=0):
        continue
    else:
        break



if(int(k)==1):

    airport="PRG"

    while(True):
        
        print ("To \n 1)Corfu \n 2)Rhodos \n 3)Heraklion \n 4)Zakynthos \n 5)Kos")
        
        d=raw_input('Press Selection Number:')
        
        if (int(d)>(5) or int(d)<=0):
            continue
        else:
            break

else:

    airport="BRQ"

    while(True):
        
        print ("To \n 1)Corfu \n 2)Rhodos \n 3)Heraklion \n 4)Zakynthos")
        
        d=raw_input('Press Selection Number:')
        
        if (int(d)>(4) or int(d)<=0):
            continue
        else:
            break

if int(d)==1:
    dest="CFU"
elif int(d)==2:
    dest="RHO"
elif int(d)==3:
    dest="HER"
elif int(d)==4:
    dest="ZTH"
else:
    dest="KGS"


while(True):
    
    print ("Type the number of days you want the lenght of the trip")
    
    day=raw_input('Press Selection Number:')
    
    if (int(day)>(200) or int(k)<=0):
        continue
    else:
        break

with open("AirTickets.csv", "r") as db:
    lines=db.readlines()
    lines.pop(0)
    for y in lines:


        y=y.split(",")

        dep=y[0].split("-")[0]
        arr=y[0].split("-")[1]

        if dep=="HER":
            break

        if dep!=airport:
            continue

        if arr!=dest:
            continue

        for z in lines:

            z=z.split(",")

            dep1=z[0].split("-")[0]
            arr1=z[0].split("-")[1]

            if (dep==arr1 and arr==dep1 ):

                ##So far destinations match and now we are checking for the date range ##

                day1=arrow.get(y[1].replace(".","-"),"DD-MM-YYYY")
                day2=arrow.get(z[1].replace(".","-"),"DD-MM-YYYY")

                if ((day2-day1).days==int(day)):
                    print y[1].strip()+" "+z[1].strip() 





        
        

        
