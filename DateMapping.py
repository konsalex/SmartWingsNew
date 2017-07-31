# -*- coding: UTF-8 -*-
import sys
import glob, os
import arrow
import csv

reload(sys)
sys.setdefaultencoding("utf8")



db=open('AirTickets.csv')
    
lines=db.readlines()

db.close()

lines.pop(0)

if lines[-1]=="ok":
    
    lines.pop(-1)
else:
    quit()

with open("dateDest.csv", "wb") as db:

    writer=csv.writer(db)

    writer.writerows(zip(["Destination"],["Start"],["End"]))

    for y in lines:


        y=y.split(",")

        dep=y[0].split("-")[0]
        arr=y[0].split("-")[1]

        

        if dep!="PRG" and dep!="BRQ":
            break


        for z in lines:

            z=z.split(",")

            dep1=z[0].split("-")[0]
            arr1=z[0].split("-")[1]

            if (dep==arr1 and arr==dep1):

                ##So far destinations match and now we are checking for the date range ##

                day1=arrow.get(y[1].replace(".","-"),"DD-MM-YYYY")
                day2=arrow.get(z[1].replace(".","-"),"DD-MM-YYYY")

                if ((day2-day1).days>=3 and (day2-day1).days<=22):
                    
                    start=(y[1].split("-")[2].strip()+"-"+y[1].split("-")[1]+"-"+y[1].split("-")[0]).strip()
                    
                    end=(z[1].split("-")[2].strip()+"-"+z[1].split("-")[1]+"-"+z[1].split("-")[0]).strip()

                    writer.writerows(zip([dep+"-"+arr],[start],[end]))





